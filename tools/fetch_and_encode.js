#!/usr/bin/env node
// tools/fetch_and_encode.js
// Usage: node tools/fetch_and_encode.js <url> <callbackName> [--base64]

const http = require('http')
const https = require('https')
const { URL } = require('url')

function fetchText(url) {
  return new Promise((resolve, reject) => {
    const u = new URL(url)
    const lib = u.protocol === 'https:' ? https : http
    const req = lib.get(u, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        resolve(fetchText(new URL(res.headers.location, u).toString()))
        return
      }
      if (res.statusCode < 200 || res.statusCode >= 400) {
        reject(new Error(`Request failed: ${res.statusCode}`))
        return
      }
      res.setEncoding('utf8')
      let data = ''
      res.on('data', chunk => data += chunk)
      res.on('end', () => resolve(data))
    })
    req.on('error', reject)
  })
}

function makeDataUrl(text, options = {}) {
  const { base64 = false, mime = 'text/javascript', charset = 'utf-8' } = options
  if (base64) {
    const b64 = Buffer.from(text, 'utf8').toString('base64')
    return `data:${mime};charset=${charset};base64,${b64}`
  } else {
    const encoded = encodeURIComponent(text)
    return `data:${mime};charset=${charset},${encoded}`
  }
}

async function main() {
  const [,, url, callbackName, flag] = process.argv
  if (!url) {
    console.error('Usage: node tools/fetch_and_encode.js <url> <callbackName> [--base64]')
    process.exit(2)
  }
  const cb = callbackName || 'handleData'
  const base64 = flag === '--base64' || flag === '-b'
  try {
    const text = await fetchText(url)
    const dataUrl = makeDataUrl(text, { base64 })
    const call = `${cb}(${JSON.stringify(dataUrl)});`
    console.log(call)
  } catch (err) {
    console.error('Error:', err.message)
    process.exit(1)
  }
}

if (require.main === module) main()
