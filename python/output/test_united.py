import pmp_manip as p
import third as t
import helpers as h

t.ThirdProject(
    stage=t.ThirdStage(
        scripts=[],
        comments=[],
        costumes=[
            t.ThirdVectorCostume(
                name='empty',
                file_extension='svg',
                rotation_center=(240, 180),
                content='<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" height="2" version="1.1" viewBox="-1 -1 2 2" width="2">\n  <!-- Exported by Scratch - http://scratch.mit.edu/ -->\n</svg>',
            ),
        ],
        sounds=[],
        costume_index=0,
        volume=100,
    ),
    sprites=[
        t.ThirdSprite(
            scripts=[
                t.ThirdScript(
                    blocks=[
                        h.event.whenflagclicked(),
                        h.gceTestRunner.test_scope(
                            name='TypeChecker',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    name='My Types',
                                    substack=[
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                value=h.gceFuncsScopes.create_function_named(name='myFn', substack=[]),
                                                type='Function (GCE)',
                                            ),
                                        ),
                                        h.jwProto.label_command(label='Methods can not be accessed from a reporter'),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                value=h.gceOOP.create_class_named(name='MyClass', substack=[]),
                                                type='Class (GCE)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                value=h.gceOOP.create_instance(
                                                    class_=h.gceOOP.create_class_named(name='MyClass', substack=[]),
                                                    posargs='[]',
                                                ),
                                                type='Class Instance (GCE)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(value=h.gceFuncsScopes.nothing(), type='Nothing (GCE)'),
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='Common/Safe JS data types',
                                    substack=[
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                value=h.SPjavascriptV2.js_reporter(code='return undefined'),
                                                type='JavaScript Undefined',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                value=h.SPjavascriptV2.js_reporter(code='return null'),
                                                type='JavaScript Null',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(value=h.operator.true_boolean(), type='Boolean'),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(value='777', type='Number'),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(value='hello', type='String'),
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='Custom Extension Types',
                                    substack=[
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                value=h.agBuffer.new_buffer(length='1'),
                                                type='Buffer (AndrewGaming587)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                value=h.agBuffer.create_pointer(
                                                    index='0',
                                                    endian=False,
                                                    buffer=h.agBuffer.new_buffer(length='1'),
                                                    type='Uint8',
                                                ),
                                                type='Buffer Pointer (AndrewGaming587)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(value=h.ddeDateFormat.current_date(), type='Date (Old Version) (ddededodediamante)'),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(value=h.ddeDateFormatV2.current_date(), type='Date (ddededodediamante)'),
                                        ),
                                        h.jwProto.label_command(label="You can't access a div effect type from any reporter"),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                value=h.divIterator.iter_builder(state='', substack=[]),
                                                type='Iterator (Div)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(value=h.dogeiscutObject.blank(), type='Object (DogeisCut)'),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                value=h.dogeiscutRegularExpressions.regex(pattern='(.*)', flags='gm'),
                                                type='Regular Expression (DogeisCut)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(value=h.dogeiscutSet.blank(), type='Set (DogeisCut)'),
                                        ),
                                        h.jwProto.label_command(label="You can't access a timer type from any reporter"),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(value=h.jwArray.blank(), type='Array (jwklong)'),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                value=h.jwColor.new_color(color='#ff0000'),
                                                type='Color (jwklong)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(value=h.jwDate.now(), type='Date (jwklong)'),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                value=h.jwLambda.new_lambda(substack=[]),
                                                type='Lambda (jwklong)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                value=h.jwNum.add(a='1', b='2'),
                                                type='Number (jwklong)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(value=h.jwTargets.this(), type='Target (jwklong)'),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                value=h.jwVector.new_vector(x='1', y='2'),
                                                type='Vector (jwklong)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                value=h.jwXML.new_node(name='test'),
                                                type='XML (jwklong)',
                                            ),
                                        ),
                                        h.jwProto.label_function(
                                            label="For this to work please create a canvas variable e.g. 'myCanvasVar', then enable the condition",
                                            substack=[
                                                h.control.if_(
                                                    condition=False,
                                                    then=[
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceFuncsScopes.typeof_value_is_menu(value='<put the canvas variable block here>', type='Canvas (RedMan13)'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.assert_(
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                value=h.fruitsPaintUtils.get_colour(colour_name='orange'),
                                                type='Paint Utils Colour (Fruits555000)',
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            name='Cast',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    name='toArray',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceFuncsScopes.set_scope_var(name='my var', value='hello'),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='var list',
                                                    value=h.gceFuncsScopes.all_variables(kind='all scopes'),
                                                ),
                                                h.gceTestRunner.assert_type(
                                                    value=h.gceFuncsScopes.get_scope_var(name='var list'),
                                                    expected='Array (jwklong)',
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceFuncsScopes.get_scope_var(name='var list'),
                                                    b='["my var"]',
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='toObject',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(name='MyClass', substack=[]),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='instance var',
                                                    value=h.gceOOP.create_instance(
                                                        class_=h.gceOOP.create_class_named(name='MyClass', substack=[]),
                                                        posargs='[]',
                                                    ),
                                                ),
                                                h.gceOOP.set_attribute(
                                                    instance=h.gceFuncsScopes.get_scope_var(name='instance var'),
                                                    name='my attribute',
                                                    value='hello',
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='attributes',
                                                    value=h.gceOOP.get_all_attributes(
                                                        instance=h.gceFuncsScopes.get_scope_var(name='instance var'),
                                                    ),
                                                ),
                                                h.gceTestRunner.assert_type(
                                                    value=h.gceFuncsScopes.get_scope_var(name='attributes'),
                                                    expected='Object (DogeisCut)',
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceFuncsScopes.get_scope_var(name='attributes'),
                                                    b='{"my attribute":"hello"}',
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='toClass && toClassInstance && toFunction',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(name='MyClass', substack=[]),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceOOP.get_superclass(
                                                        class_=h.gceOOP.create_subclass_named(name='Sub', superclass='MyClass', substack=[]),
                                                    ),
                                                    b="<Class 'MyClass'>",
                                                ),
                                                h.gceTestRunner.assert_throws_contains(
                                                    msg='but got no input value',
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            expr=h.gceOOP.get_superclass(
                                                                class_=h.SPjavascriptV2.js_reporter(code='return undefined'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_throws_contains(
                                                    msg='but got no input value',
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            expr=h.gceOOP.get_superclass(
                                                                class_=h.SPjavascriptV2.js_reporter(code='return null'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceOOP.get_superclass(class_='MyClass'),
                                                    b="<Class 'Superclass'>",
                                                ),
                                                h.gceOOP.create_class_at(name='513', substack=[]),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceOOP.get_superclass(class_='513'),
                                                    b="<Class 'Superclass'>",
                                                ),
                                                h.gceTestRunner.assert_throws_contains(
                                                    msg='but got no input value',
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            expr=h.gceOOP.get_superclass(
                                                                class_=h.SPjavascriptV2.js_reporter(code='return null'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_throws(
                                                    substack=[
                                                        h.gceOOP.create_subclass_at(
                                                            name='Sub2',
                                                            superclass=h.gceFuncsScopes.create_function_named(name='myFunction', substack=[]),
                                                            substack=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            name='Scoped Variables Blocks',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    name='set/get/exists',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Set and read a local variable',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='myVar', kind='all scopes'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='myVar', kind='local scope'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='myVar', kind='global scope'),
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(name='myVar', value='hello'),
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.get_scope_var(name='myVar'),
                                                            b='hello',
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='myVar', kind='all scopes'),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='myVar', kind='local scope'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='myVar', kind='global scope'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='delete var',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Delete removes the variable from the current scope',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(name='tmp', value='to-delete'),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='tmp', kind='all scopes'),
                                                        ),
                                                        h.gceFuncsScopes.delete_scope_var(name='tmp'),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='tmp', kind='all scopes'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='tmp', kind='local scope'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='tmp', kind='global scope'),
                                                        ),
                                                        h.gceTestRunner.assert_throws(
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    expr=h.gceFuncsScopes.get_scope_var(name='tmp'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='all variables + local scope',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='List variables by kind and verify nested local scope behavior',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(name='a', value='1'),
                                                        h.gceFuncsScopes.set_scope_var(name='b', value='2'),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceFuncsScopes.all_variables(kind='all scopes'),
                                                            b='["a","b"]',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceFuncsScopes.all_variables(kind='local scope'),
                                                            b='["a","b"]',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceFuncsScopes.all_variables(kind='global scope'),
                                                            b='[]',
                                                        ),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            substack=[
                                                                h.gceTestRunner.test_scope(
                                                                    name='In a fresh local scope, inherited names are visible in all scopes',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_unstrict_equal(
                                                                            a=h.gceFuncsScopes.all_variables(kind='all scopes'),
                                                                            b='["a","b"]',
                                                                        ),
                                                                        h.gceTestRunner.assert_unstrict_equal(
                                                                            a=h.gceFuncsScopes.all_variables(kind='local scope'),
                                                                            b='[]',
                                                                        ),
                                                                        h.gceTestRunner.assert_unstrict_equal(
                                                                            a=h.gceFuncsScopes.all_variables(kind='global scope'),
                                                                            b='[]',
                                                                        ),
                                                                        h.gceFuncsScopes.set_scope_var(name='c', value='3'),
                                                                        h.gceTestRunner.assert_unstrict_equal(
                                                                            a=h.gceFuncsScopes.all_variables(kind='all scopes'),
                                                                            b='["a","b","c"]',
                                                                        ),
                                                                        h.gceTestRunner.assert_unstrict_equal(
                                                                            a=h.gceFuncsScopes.all_variables(kind='local scope'),
                                                                            b='["c"]',
                                                                        ),
                                                                        h.gceTestRunner.assert_unstrict_equal(
                                                                            a=h.gceFuncsScopes.all_variables(kind='global scope'),
                                                                            b='[]',
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='c', kind='local scope'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='c', kind='all scopes'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='allVariables with globals and locals simultaneously',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='kind_global and kind_local see only their own tier; kind_all sees both',
                                            substack=[
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(name='globalX', value='gx'),
                                                        h.gceFuncsScopes.set_scope_var(name='globalY', value='gy'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(name='localZ', value='lz'),
                                                                h.gceTestRunner.test_scope(
                                                                    name='kind_global sees globals only',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_text_in_value(
                                                                            text='globalX',
                                                                            value=h.gceFuncsScopes.all_variables(kind='global scope'),
                                                                        ),
                                                                        h.gceTestRunner.assert_text_in_value(
                                                                            text='globalY',
                                                                            value=h.gceFuncsScopes.all_variables(kind='global scope'),
                                                                        ),
                                                                        h.gceTestRunner.assert_text_not_in_value(
                                                                            text='localZ',
                                                                            value=h.gceFuncsScopes.all_variables(kind='global scope'),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceTestRunner.test_scope(
                                                                    name='kind_local sees locals only',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_text_in_value(
                                                                            text='localZ',
                                                                            value=h.gceFuncsScopes.all_variables(kind='local scope'),
                                                                        ),
                                                                        h.gceTestRunner.assert_text_not_in_value(
                                                                            text='globalX',
                                                                            value=h.gceFuncsScopes.all_variables(kind='local scope'),
                                                                        ),
                                                                        h.gceTestRunner.assert_text_not_in_value(
                                                                            text='globalY',
                                                                            value=h.gceFuncsScopes.all_variables(kind='local scope'),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceTestRunner.test_scope(
                                                                    name='kind_all sees both globals and locals',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_text_in_value(
                                                                            text='globalX',
                                                                            value=h.gceFuncsScopes.all_variables(kind='all scopes'),
                                                                        ),
                                                                        h.gceTestRunner.assert_text_in_value(
                                                                            text='globalY',
                                                                            value=h.gceFuncsScopes.all_variables(kind='all scopes'),
                                                                        ),
                                                                        h.gceTestRunner.assert_text_in_value(
                                                                            text='localZ',
                                                                            value=h.gceFuncsScopes.all_variables(kind='all scopes'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='bind global + non-local',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Bind global in an inner scope and mutate it',
                                            substack=[
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(name='globalCounter', value='0'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            substack=[
                                                                h.gceFuncsScopes.bind_var_to_scope(kind='global', name='globalCounter'),
                                                                h.gceFuncsScopes.set_scope_var(name='globalCounter', value='1'),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.get_scope_var(name='globalCounter'),
                                                            b='1',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Bind non-local variable in nested local scopes and mutate it',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(name='outerLocal', value='A'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            substack=[
                                                                h.gceFuncsScopes.bind_var_to_scope(kind='non-local', name='outerLocal'),
                                                                h.gceFuncsScopes.set_scope_var(name='outerLocal', value='B'),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.get_scope_var(name='outerLocal'),
                                                            b='B',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='shadowing: inner scope shadows outer name',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='get_scope_var resolves to innermost definition',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(name='x', value='outer'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(name='x', value='inner'),
                                                                h.gceTestRunner.test_scope(
                                                                    name='Inner scope sees the inner value',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_strict_equal(
                                                                            a=h.gceFuncsScopes.get_scope_var(name='x'),
                                                                            b='inner',
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='After inner scope exits, outer value is restored',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.gceFuncsScopes.get_scope_var(name='x'),
                                                                    b='outer',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='bind then delete',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Delete a bound global variable from an inner scope',
                                            substack=[
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(name='toDelete', value='exists'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            substack=[
                                                                h.gceFuncsScopes.bind_var_to_scope(kind='global', name='toDelete'),
                                                                h.gceFuncsScopes.delete_scope_var(name='toDelete'),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Variable is gone from globals after delete',
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    condition=h.gceFuncsScopes.scope_var_exists(name='toDelete', kind='global scope'),
                                                                ),
                                                                h.gceTestRunner.assert_not(
                                                                    condition=h.gceFuncsScopes.scope_var_exists(name='toDelete', kind='all scopes'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Delete a bound non-local variable from an inner scope',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(name='outerVar', value='exists'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            substack=[
                                                                h.gceFuncsScopes.bind_var_to_scope(kind='non-local', name='outerVar'),
                                                                h.gceFuncsScopes.delete_scope_var(name='outerVar'),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Variable is gone from outer scope after delete',
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    condition=h.gceFuncsScopes.scope_var_exists(name='outerVar', kind='all scopes'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='bind error paths',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Binding a missing global/non-local variable should throw',
                                            substack=[
                                                h.gceTestRunner.assert_throws(
                                                    substack=[
                                                        h.gceFuncsScopes.bind_var_to_scope(kind='global', name='missingGlobal'),
                                                    ],
                                                ),
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            substack=[
                                                                h.gceFuncsScopes.bind_var_to_scope(kind='non-local', name='missingNonLocal'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='createVarScope cleanup on error',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='exitUserScope must run even if an error is thrown inside the scope',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(name='outerVar', value='present'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(name='innerVar', value='value'),
                                                                h.gceTestRunner.assert_throws(
                                                                    substack=[
                                                                        h.gceFuncsScopes.execute_expression(
                                                                            expr=h.gceFuncsScopes.get_scope_var(name='__missing_var__'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Inner variable should be gone after error',
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    condition=h.gceFuncsScopes.scope_var_exists(name='innerVar', kind='all scopes'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Outer variable should still exist',
                                                            substack=[
                                                                h.gceTestRunner.assert_(
                                                                    condition=h.gceFuncsScopes.scope_var_exists(name='outerVar', kind='all scopes'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='scopeVarExists with 3-level nesting',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Verify kindLocal, kindAll, kindGlobal across 3 scopes',
                                            substack=[
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(name='globalVar', value='g'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(name='level1', value='L1'),
                                                                h.gceFuncsScopes.create_var_scope(
                                                                    substack=[
                                                                        h.gceFuncsScopes.set_scope_var(name='level2', value='L2'),
                                                                        h.gceFuncsScopes.create_var_scope(
                                                                            substack=[
                                                                                h.gceFuncsScopes.set_scope_var(name='level3', value='L3'),
                                                                                h.gceTestRunner.test_scope(
                                                                                    name='Innermost: level3 is local, others are not',
                                                                                    substack=[
                                                                                        h.gceTestRunner.assert_(
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(name='level3', kind='local scope'),
                                                                                        ),
                                                                                        h.gceTestRunner.assert_not(
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(name='level1', kind='local scope'),
                                                                                        ),
                                                                                        h.gceTestRunner.assert_not(
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(name='level2', kind='local scope'),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                h.gceTestRunner.test_scope(
                                                                                    name='All three are visible via kindAll',
                                                                                    substack=[
                                                                                        h.gceTestRunner.assert_(
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(name='level1', kind='all scopes'),
                                                                                        ),
                                                                                        h.gceTestRunner.assert_(
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(name='level2', kind='all scopes'),
                                                                                        ),
                                                                                        h.gceTestRunner.assert_(
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(name='level3', kind='all scopes'),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                h.gceTestRunner.test_scope(
                                                                                    name='Global is visible via kindGlobal and kindAll',
                                                                                    substack=[
                                                                                        h.gceTestRunner.assert_(
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(name='globalVar', kind='global scope'),
                                                                                        ),
                                                                                        h.gceTestRunner.assert_(
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(name='globalVar', kind='all scopes'),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                h.gceTestRunner.test_scope(
                                                                                    name='Local vars are NOT global',
                                                                                    substack=[
                                                                                        h.gceTestRunner.assert_not(
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(name='level3', kind='global scope'),
                                                                                        ),
                                                                                        h.gceTestRunner.assert_not(
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(name='level2', kind='global scope'),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceTestRunner.test_scope(
                                                                    name='level2 and level3 gone after exiting their scopes',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_not(
                                                                            condition=h.gceFuncsScopes.scope_var_exists(name='level2', kind='all scopes'),
                                                                        ),
                                                                        h.gceTestRunner.assert_not(
                                                                            condition=h.gceFuncsScopes.scope_var_exists(name='level3', kind='all scopes'),
                                                                        ),
                                                                        h.gceTestRunner.assert_(
                                                                            condition=h.gceFuncsScopes.scope_var_exists(name='level1', kind='local scope'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='runWithSeparateGlobals',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Outer locals are not visible inside',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(name='outerLocal', value='outer'),
                                                        h.gceFuncsScopes.run_with_separate_globals(
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    condition=h.gceFuncsScopes.scope_var_exists(name='outerLocal', kind='all scopes'),
                                                                ),
                                                                h.gceTestRunner.assert_not(
                                                                    condition=h.gceFuncsScopes.scope_var_exists(name='outerLocal', kind='local scope'),
                                                                ),
                                                                h.gceTestRunner.assert_not(
                                                                    condition=h.gceFuncsScopes.scope_var_exists(name='outerLocal', kind='global scope'),
                                                                ),
                                                                h.gceTestRunner.assert_throws(
                                                                    substack=[
                                                                        h.gceFuncsScopes.execute_expression(
                                                                            expr=h.gceFuncsScopes.get_scope_var(name='outerLocal'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Outer globals are not visible inside',
                                            substack=[
                                                h.gceFuncsScopes.set_scope_var(name='outerGlobal', value='outerGlobalValue'),
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='outerGlobal', kind='all scopes'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='outerGlobal', kind='global scope'),
                                                        ),
                                                        h.gceTestRunner.assert_throws(
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    expr=h.gceFuncsScopes.get_scope_var(name='outerGlobal'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceFuncsScopes.delete_scope_var(name='outerGlobal'),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Writes inside do not affect outer locals',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(name='sharedName', value='before'),
                                                        h.gceFuncsScopes.run_with_separate_globals(
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(name='sharedName', value='inside'),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.gceFuncsScopes.get_scope_var(name='sharedName'),
                                                                    b='inside',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.get_scope_var(name='sharedName'),
                                                            b='before',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Writes inside do not affect outer globals',
                                            substack=[
                                                h.gceFuncsScopes.set_scope_var(name='sharedGlobal', value='globalBefore'),
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(name='sharedGlobal', value='globalInside'),
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.get_scope_var(name='sharedGlobal'),
                                                            b='globalInside',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_strict_equal(
                                                    a=h.gceFuncsScopes.get_scope_var(name='sharedGlobal'),
                                                    b='globalBefore',
                                                ),
                                                h.gceFuncsScopes.delete_scope_var(name='sharedGlobal'),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Inner globals and locals start empty',
                                            substack=[
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceFuncsScopes.all_variables(kind='all scopes'),
                                                            b='[]',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceFuncsScopes.all_variables(kind='global scope'),
                                                            b='[]',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceFuncsScopes.all_variables(kind='local scope'),
                                                            b='[]',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Variables created inside are gone after block exits',
                                            substack=[
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(name='innerOnly', value='value'),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_not(
                                                    condition=h.gceFuncsScopes.scope_var_exists(name='innerOnly', kind='all scopes'),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Cleanup happens even if an error is thrown inside',
                                            substack=[
                                                h.gceTestRunner.assert_throws(
                                                    substack=[
                                                        h.gceFuncsScopes.run_with_separate_globals(
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(name='innerError', value='value'),
                                                                h.gceFuncsScopes.execute_expression(
                                                                    expr=h.gceFuncsScopes.get_scope_var(name='__missing__'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_not(
                                                    condition=h.gceFuncsScopes.scope_var_exists(name='innerError', kind='all scopes'),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Nested runWithSeparateGlobals are fully independent',
                                            substack=[
                                                h.gceFuncsScopes.set_scope_var(name='outerG', value='OG'),
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(name='middleG', value='MG'),
                                                        h.gceFuncsScopes.run_with_separate_globals(
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    condition=h.gceFuncsScopes.scope_var_exists(name='outerG', kind='all scopes'),
                                                                ),
                                                                h.gceTestRunner.assert_not(
                                                                    condition=h.gceFuncsScopes.scope_var_exists(name='middleG', kind='all scopes'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='middleG', kind='global scope'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='outerG', kind='all scopes'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_(
                                                    condition=h.gceFuncsScopes.scope_var_exists(name='outerG', kind='global scope'),
                                                ),
                                                h.gceTestRunner.assert_not(
                                                    condition=h.gceFuncsScopes.scope_var_exists(name='middleG', kind='all scopes'),
                                                ),
                                                h.gceFuncsScopes.delete_scope_var(name='outerG'),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            name='Function Blocks',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    name='basic function',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    name='Define a simple function that returns a constant',
                                                    substack=[
                                                        h.gceFuncsScopes.create_function_at(
                                                            name='myFunc',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(value='hello'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Call the function with no arguments',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.call_function(func='myFunc', posargs='[]'),
                                                            b='hello',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='function with args',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    name='Configure and define function with two arguments',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(argnames='["greeting", "name"]', argdefaults='[]'),
                                                        h.gceFuncsScopes.create_function_at(
                                                            name='greet',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    value=h.operator.join3(
                                                                        string1=h.gceFuncsScopes.get_scope_var(name='greeting'),
                                                                        string2=' ',
                                                                        string3=h.gceFuncsScopes.get_scope_var(name='name'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Call with two arguments passed as array',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.call_function(func='greet', posargs='["Hello", "Ada"]'),
                                                            b='Hello Ada',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='default arguments',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    name='Configure function with required arg and default trailing arg',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(argnames='["person", "greeting"]', argdefaults='["Hi"]'),
                                                        h.gceFuncsScopes.create_function_at(
                                                            name='sayHi',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    value=h.operator.join3(
                                                                        string1=h.gceFuncsScopes.get_scope_var(name='greeting'),
                                                                        string2=' ',
                                                                        string3=h.gceFuncsScopes.get_scope_var(name='person'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Call with only first arg (second uses default Hi)',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.call_function(func='sayHi', posargs='["Bob"]'),
                                                            b='Hi Bob',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Call with both args (overrides default)',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.call_function(func='sayHi', posargs='["Bob", "Hey"]'),
                                                            b='Hey Bob',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='return behavior',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    name='Function returns early inside an if-block; later return must not run',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(argnames='["flag"]', argdefaults='[]'),
                                                        h.gceFuncsScopes.create_function_at(
                                                            name='conditional',
                                                            substack=[
                                                                h.control.if_(
                                                                    condition=h.operator.equals(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='flag'),
                                                                        operand2='yes',
                                                                    ),
                                                                    then=[
                                                                        h.gceFuncsScopes.return_value(value='early'),
                                                                    ],
                                                                ),
                                                                h.gceFuncsScopes.return_value(value='late'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='When condition is true, early return fires',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.call_function(func='conditional', posargs='["yes"]'),
                                                            b='early',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='When condition is false, falls through to second return',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.call_function(func='conditional', posargs='["no"]'),
                                                            b='late',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='closures',
                                    substack=[
                                        h.gceFuncsScopes.run_with_separate_globals(
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    name='Outer function accepts prefix, returns inner function that closes over it',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(argnames='["prefix"]', argdefaults='[]'),
                                                        h.gceFuncsScopes.create_function_at(
                                                            name='makeGreeter',
                                                            substack=[
                                                                h.gceTestRunner.test_scope(
                                                                    name='Configure inner function arg before defining it',
                                                                    substack=[
                                                                        h.gceFuncsScopes.configure_next_function_args(argnames='["name"]', argdefaults='[]'),
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.gceFuncsScopes.create_function_named(
                                                                                name='greeter',
                                                                                substack=[
                                                                                    h.gceFuncsScopes.return_value(
                                                                                        value=h.operator.join3(
                                                                                            string1=h.gceFuncsScopes.get_scope_var(name='prefix'),
                                                                                            string2=', ',
                                                                                            string3=h.gceFuncsScopes.get_scope_var(name='name'),
                                                                                        ),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Each call to makeGreeter produces an independent greeter',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='hiGreeter',
                                                            value=h.gceFuncsScopes.call_function(func='makeGreeter', posargs='["Hi"]'),
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='heyGreeter',
                                                            value=h.gceFuncsScopes.call_function(func='makeGreeter', posargs='["Hey"]'),
                                                        ),
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.call_function(func='hiGreeter', posargs='["Ada"]'),
                                                            b='Hi, Ada',
                                                        ),
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.call_function(func='heyGreeter', posargs='["Ada"]'),
                                                            b='Hey, Ada',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Captured prefix is independent per closure instance',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.call_function(func='hiGreeter', posargs='["Bob"]'),
                                                            b='Hi, Bob',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='create function named',
                                    substack=[
                                        h.gceFuncsScopes.run_with_separate_globals(
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    name='Create a function as a reporter block (returns the function)',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='myFunc',
                                                            value=h.gceFuncsScopes.create_function_named(
                                                                name='anonFunc',
                                                                substack=[
                                                                    h.gceFuncsScopes.return_value(value='from-anon'),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Call the stored function',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.call_function(func='myFunc', posargs='[]'),
                                                            b='from-anon',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='error: wrong arg count',
                                    substack=[
                                        h.gceFuncsScopes.run_with_separate_globals(
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    name='Function that accepts no arguments',
                                                    substack=[
                                                        h.gceFuncsScopes.create_function_at(
                                                            name='noArgs',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(value='done'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Calling with extra arguments should throw',
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    expr=h.gceFuncsScopes.call_function(func='noArgs', posargs='["extra"]'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Function that requires one argument',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(argnames='["required"]', argdefaults='[]'),
                                                        h.gceFuncsScopes.create_function_at(
                                                            name='oneArg',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    value=h.gceFuncsScopes.get_scope_var(name='required'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Calling with no arguments should throw',
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    expr=h.gceFuncsScopes.call_function(func='oneArg', posargs='[]'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='var scope inside function body',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    name='createVarScope inside a function is isolated per call',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(argnames='["val"]', argdefaults='[]'),
                                                        h.gceFuncsScopes.create_function_at(
                                                            name='withScope',
                                                            substack=[
                                                                h.gceFuncsScopes.create_var_scope(
                                                                    substack=[
                                                                        h.gceFuncsScopes.set_scope_var(
                                                                            name='inner',
                                                                            value=h.gceFuncsScopes.get_scope_var(name='val'),
                                                                        ),
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.gceFuncsScopes.get_scope_var(name='inner'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='First call',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.call_function(func='withScope', posargs='["first"]'),
                                                            b='first',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Second call: inner var is fresh each call',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceFuncsScopes.call_function(func='withScope', posargs='["second"]'),
                                                            b='second',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Inner scope var is not visible outside the function',
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.scope_var_exists(name='inner', kind='all scopes'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            name='Utilities Blocks',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    name='nothing',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Nothing is its own type',
                                            substack=[
                                                h.gceTestRunner.assert_(
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(value=h.gceFuncsScopes.nothing(), type='Nothing (GCE)'),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Nothing equals itself via string comparison',
                                            substack=[
                                                h.gceTestRunner.assert_unstrict_equal(a=h.gceFuncsScopes.nothing(), b=h.gceFuncsScopes.nothing()),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Nothing is identical to itself (same singleton)',
                                            substack=[
                                                h.gceTestRunner.assert_(
                                                    condition=h.gceFuncsScopes.check_identity(value1=h.gceFuncsScopes.nothing(), value2=h.gceFuncsScopes.nothing()),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Nothing is not identical to any other value',
                                            substack=[
                                                h.gceTestRunner.assert_not(
                                                    condition=h.gceFuncsScopes.check_identity(value1=h.gceFuncsScopes.nothing(), value2='0'),
                                                ),
                                                h.gceTestRunner.assert_not(
                                                    condition=h.gceFuncsScopes.check_identity(value1=h.gceFuncsScopes.nothing(), value2=''),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='typeofValue',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Primitive types',
                                            substack=[
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceFuncsScopes.typeof_value(value='hello'),
                                                    b=h.gceFuncsScopes.typeof_value_selection(type='String'),
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceFuncsScopes.typeof_value(value='42'),
                                                    b=h.gceFuncsScopes.typeof_value_selection(type='Number'),
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceFuncsScopes.typeof_value(value=h.operator.true_boolean()),
                                                    b=h.gceFuncsScopes.typeof_value_selection(type='Boolean'),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='GCE types',
                                            substack=[
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceFuncsScopes.typeof_value(value=h.gceFuncsScopes.nothing()),
                                                    b=h.gceFuncsScopes.typeof_value_selection(type='Nothing (GCE)'),
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceFuncsScopes.typeof_value(
                                                        value=h.gceFuncsScopes.create_function_named(
                                                            name='f',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(value='x'),
                                                            ],
                                                        ),
                                                    ),
                                                    b=h.gceFuncsScopes.typeof_value_selection(type='Function (GCE)'),
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceFuncsScopes.typeof_value(
                                                        value=h.gceOOP.create_class_named(name='MyClass', substack=[]),
                                                    ),
                                                    b=h.gceFuncsScopes.typeof_value_selection(type='Class (GCE)'),
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceFuncsScopes.typeof_value(
                                                        value=h.gceOOP.create_instance(
                                                            class_=h.gceOOP.create_class_named(name='MyClass', substack=[]),
                                                            posargs='[]',
                                                        ),
                                                    ),
                                                    b=h.gceFuncsScopes.typeof_value_selection(type='Class Instance (GCE)'),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='typeofValueIsMenu',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Correct type returns true',
                                            substack=[
                                                h.gceTestRunner.assert_(
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(value='hello', type='String'),
                                                ),
                                                h.gceTestRunner.assert_(
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(value='42', type='Number'),
                                                ),
                                                h.gceTestRunner.assert_(
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(value=h.operator.true_boolean(), type='Boolean'),
                                                ),
                                                h.gceTestRunner.assert_(
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(value=h.gceFuncsScopes.nothing(), type='Nothing (GCE)'),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Wrong type returns false',
                                            substack=[
                                                h.gceTestRunner.assert_not(
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(value='hello', type='Number'),
                                                ),
                                                h.gceTestRunner.assert_not(
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(value='42', type='String'),
                                                ),
                                                h.gceTestRunner.assert_not(
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(value=h.gceFuncsScopes.nothing(), type='String'),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='typeofValueIsMenu is consistent with typeofValue',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='fn',
                                                            value=h.gceFuncsScopes.create_function_named(
                                                                name='g',
                                                                substack=[
                                                                    h.gceFuncsScopes.return_value(value='y'),
                                                                ],
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                                value=h.gceFuncsScopes.get_scope_var(name='fn'),
                                                                type='Function (GCE)',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                                value=h.gceFuncsScopes.get_scope_var(name='fn'),
                                                                type='Class (GCE)',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='typeofValueSelection',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='The reporter returns the menu value as a string',
                                            substack=[
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceFuncsScopes.typeof_value_selection(type='String'),
                                                    b='String',
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceFuncsScopes.typeof_value_selection(type='Nothing (GCE)'),
                                                    b='Nothing (GCE)',
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceFuncsScopes.typeof_value_selection(type='Function (GCE)'),
                                                    b='Function (GCE)',
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Result matches typeofValue output',
                                            substack=[
                                                h.gceTestRunner.assert_(
                                                    condition=h.operator.equals(
                                                        operand1=h.gceFuncsScopes.typeof_value(value=h.gceFuncsScopes.nothing()),
                                                        operand2=h.gceFuncsScopes.typeof_value_selection(type='Nothing (GCE)'),
                                                    ),
                                                ),
                                                h.gceTestRunner.assert_(
                                                    condition=h.operator.equals(
                                                        operand1=h.gceFuncsScopes.typeof_value(value='test'),
                                                        operand2=h.gceFuncsScopes.typeof_value_selection(type='String'),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='objectAsString',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Primitive values stringify as-is',
                                            substack=[
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceFuncsScopes.object_as_string(value='hello'),
                                                    b='hello',
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    a=h.gceFuncsScopes.object_as_string(value='42'),
                                                    b='42',
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Nothing stringifies to its representation',
                                            substack=[
                                                h.gceTestRunner.assert_does_not_throw(
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            expr=h.gceFuncsScopes.object_as_string(value=h.gceFuncsScopes.nothing()),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Instance without as-string method: no error, returns some string',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(name='Plain', substack=[]),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='inst',
                                                            value=h.gceOOP.create_instance(class_='Plain', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.assert_does_not_throw(
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    expr=h.gceFuncsScopes.object_as_string(
                                                                        value=h.gceFuncsScopes.get_scope_var(name='inst'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                                value=h.gceFuncsScopes.object_as_string(
                                                                    value=h.gceFuncsScopes.get_scope_var(name='inst'),
                                                                ),
                                                                type='String',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Instance WITH as-string method: calls the method',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='Stringable',
                                                            substack=[
                                                                h.gceOOP.define_special_method(
                                                                    special_method='as string',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='custom-string'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='inst',
                                                            value=h.gceOOP.create_instance(class_='Stringable', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceFuncsScopes.object_as_string(
                                                                value=h.gceFuncsScopes.get_scope_var(name='inst'),
                                                            ),
                                                            b='custom-string',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='checkIdentity',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Two separate instances of the same class are NOT identical',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(name='MyClass', substack=[]),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='a',
                                                            value=h.gceOOP.create_instance(class_='MyClass', posargs='[]'),
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='b',
                                                            value=h.gceOOP.create_instance(class_='MyClass', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.check_identity(
                                                                value1=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                value2=h.gceFuncsScopes.get_scope_var(name='b'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='The same instance stored in two variables IS identical',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(name='MyClass', substack=[]),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='a',
                                                            value=h.gceOOP.create_instance(class_='MyClass', posargs='[]'),
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='b',
                                                            value=h.gceFuncsScopes.get_scope_var(name='a'),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceFuncsScopes.check_identity(
                                                                value1=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                value2=h.gceFuncsScopes.get_scope_var(name='b'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Nothing is identical to itself',
                                            substack=[
                                                h.gceTestRunner.assert_(
                                                    condition=h.gceFuncsScopes.check_identity(value1=h.gceFuncsScopes.nothing(), value2=h.gceFuncsScopes.nothing()),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Nothing is not identical to a function',
                                            substack=[
                                                h.gceTestRunner.assert_not(
                                                    condition=h.gceFuncsScopes.check_identity(
                                                        value1=h.gceFuncsScopes.nothing(),
                                                        value2=h.gceFuncsScopes.create_function_named(
                                                            name='h',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(value='z'),
                                                            ],
                                                        ),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Two separately created functions are NOT identical',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='f1',
                                                            value=h.gceFuncsScopes.create_function_named(
                                                                name='fn1',
                                                                substack=[
                                                                    h.gceFuncsScopes.return_value(value='r'),
                                                                ],
                                                            ),
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='f2',
                                                            value=h.gceFuncsScopes.create_function_named(
                                                                name='fn2',
                                                                substack=[
                                                                    h.gceFuncsScopes.return_value(value='r'),
                                                                ],
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceFuncsScopes.check_identity(
                                                                value1=h.gceFuncsScopes.get_scope_var(name='f1'),
                                                                value2=h.gceFuncsScopes.get_scope_var(name='f2'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Primitive strings identical',
                                            substack=[
                                                h.gceTestRunner.assert_(
                                                    condition=h.gceFuncsScopes.check_identity(value1='hello', value2='hello'),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='executeExpression',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Evaluate a reporter block as a command (no error)',
                                            substack=[
                                                h.gceTestRunner.assert_does_not_throw(
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(expr=h.gceFuncsScopes.nothing()),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='executeExpression propagates errors from its subexpression',
                                            substack=[
                                                h.gceTestRunner.assert_throws(
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            expr=h.gceFuncsScopes.get_scope_var(name='__missing__'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='executeExpression can evaluate any reporter',
                                            substack=[
                                                h.gceTestRunner.assert_does_not_throw(
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            expr=h.gceFuncsScopes.typeof_value(value='test'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_does_not_throw(
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            expr=h.gceFuncsScopes.object_as_string(value='hello'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='executeExpression can call a function and discard the return value',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceFuncsScopes.create_function_at(
                                                            name='noopFn',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(value='done'),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_does_not_throw(
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    expr=h.gceFuncsScopes.call_function(func='noopFn', posargs='[]'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            name='Class Definition and Inheritance Blocks',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    name='createClassAt',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Class is accessible by name and typeof is Class (GCE)',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(name='MyClass', substack=[]),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceFuncsScopes.typeof_value(
                                                                value=h.gceFuncsScopes.get_scope_var(name='MyClass'),
                                                            ),
                                                            b=h.gceFuncsScopes.typeof_value_selection(type='Class (GCE)'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Can create an instance immediately',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    name='inst',
                                                                    value=h.gceOOP.create_instance(class_='MyClass', posargs='[]'),
                                                                ),
                                                                h.gceTestRunner.assert_(
                                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                                        value=h.gceFuncsScopes.get_scope_var(name='inst'),
                                                                        type='Class Instance (GCE)',
                                                                    ),
                                                                ),
                                                                h.gceTestRunner.assert_(
                                                                    condition=h.gceOOP.is_instance(
                                                                        potential_instance=h.gceFuncsScopes.get_scope_var(name='inst'),
                                                                        class_='MyClass',
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Class with methods and init defined inline',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='Counter',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(argnames='["start"]', argdefaults='["0"]'),
                                                                h.gceOOP.define_special_method(
                                                                    special_method='init',
                                                                    substack=[
                                                                        h.gceOOP.set_attribute(
                                                                            instance=h.gceOOP.self_value(),
                                                                            name='count',
                                                                            value=h.gceFuncsScopes.get_scope_var(name='start'),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_instance_method(
                                                                    name='value',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.gceOOP.get_attribute(name='count', instance=h.gceOOP.self_value()),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='c',
                                                            value=h.gceOOP.create_instance(class_='Counter', posargs='["5"]'),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_method(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                name='value',
                                                                posargs='[]',
                                                            ),
                                                            b='5',
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Default arg: no args uses default 0',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    name='d',
                                                                    value=h.gceOOP.create_instance(class_='Counter', posargs='[]'),
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.call_method(
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='d'),
                                                                        name='value',
                                                                        posargs='[]',
                                                                    ),
                                                                    b='0',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='createClassNamed (reporter)',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Create class inline as a reporter value, store and use it',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='Dyn',
                                                            value=h.gceOOP.create_class_named(
                                                                name='DynClass',
                                                                substack=[
                                                                    h.gceOOP.define_instance_method(
                                                                        name='ping',
                                                                        substack=[
                                                                            h.gceFuncsScopes.return_value(value='pong'),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Stored value is a Class (GCE)',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceFuncsScopes.typeof_value(
                                                                        value=h.gceFuncsScopes.get_scope_var(name='Dyn'),
                                                                    ),
                                                                    b=h.gceFuncsScopes.typeof_value_selection(type='Class (GCE)'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Class can be instantiated',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    name='inst',
                                                                    value=h.gceOOP.create_instance(
                                                                        class_=h.gceFuncsScopes.get_scope_var(name='Dyn'),
                                                                        posargs='[]',
                                                                    ),
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.call_method(
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='inst'),
                                                                        name='ping',
                                                                        posargs='[]',
                                                                    ),
                                                                    b='pong',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='currentClass',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='currentClass inside createClassAt returns the class being defined',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='Stamped',
                                                            substack=[
                                                                h.gceOOP.set_class_variable(class_=h.gceOOP.current_class(), name='tag', value='stamped-value'),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Class variable set via currentClass is accessible by name',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_class_variable(name='tag', class_='Stamped'),
                                                                    b='stamped-value',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='currentClass inside createClassNamed also works',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='NC',
                                                            value=h.gceOOP.create_class_named(
                                                                name='NamedCls',
                                                                substack=[
                                                                    h.gceOOP.set_class_variable(class_=h.gceOOP.current_class(), name='info', value='from-named'),
                                                                ],
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.get_class_variable(
                                                                name='info',
                                                                class_=h.gceFuncsScopes.get_scope_var(name='NC'),
                                                            ),
                                                            b='from-named',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='currentClass inside onClass returns the correct class',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(name='Extendable', substack=[]),
                                                        h.gceOOP.on_class(
                                                            class_='Extendable',
                                                            substack=[
                                                                h.gceOOP.set_class_variable(class_=h.gceOOP.current_class(), name='addedTag', value='via-on-class'),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.get_class_variable(name='addedTag', class_='Extendable'),
                                                            b='via-on-class',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='createSubclassAt',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    name='Animal',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            name='breathe',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(value='breathing'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceOOP.create_subclass_at(
                                                    name='Dog',
                                                    superclass='Animal',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            name='bark',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(value='woof'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='isSubclass reflects the relationship',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_subclass(subclass='Dog', superclass='Animal'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceOOP.is_subclass(subclass='Animal', superclass='Dog'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='getSuperclass of Dog is Animal',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='Animal',
                                                            value=h.gceOOP.get_superclass(class_='Dog'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Dog instance can call both inherited and own methods',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='d',
                                                            value=h.gceOOP.create_instance(class_='Dog', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_method(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='d'),
                                                                name='breathe',
                                                                posargs='[]',
                                                            ),
                                                            b='breathing',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_method(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='d'),
                                                                name='bark',
                                                                posargs='[]',
                                                            ),
                                                            b='woof',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='currentClass inside subclass body returns the subclass',
                                                    substack=[
                                                        h.gceOOP.create_subclass_at(
                                                            name='Puppy',
                                                            superclass='Dog',
                                                            substack=[
                                                                h.gceOOP.set_class_variable(class_=h.gceOOP.current_class(), name='size', value='small'),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.get_class_variable(name='size', class_='Puppy'),
                                                            b='small',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='isSubclass is transitive',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_subclass(subclass='Puppy', superclass='Animal'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='createSubclassNamed (reporter)',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    name='BaseR',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            name='base',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(value='from-base'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='Sub',
                                                    value=h.gceOOP.create_subclass_named(
                                                        name='SubNamed',
                                                        superclass='BaseR',
                                                        substack=[
                                                            h.gceOOP.define_instance_method(
                                                                name='child',
                                                                substack=[
                                                                    h.gceFuncsScopes.return_value(value='from-child'),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Stored value is a Class (GCE)',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceFuncsScopes.typeof_value(
                                                                value=h.gceFuncsScopes.get_scope_var(name='Sub'),
                                                            ),
                                                            b=h.gceFuncsScopes.typeof_value_selection(type='Class (GCE)'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='isSubclass works for reporter-created subclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_subclass(
                                                                subclass=h.gceFuncsScopes.get_scope_var(name='Sub'),
                                                                superclass='BaseR',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Instance inherits from base and has own method',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='inst',
                                                            value=h.gceOOP.create_instance(
                                                                class_=h.gceFuncsScopes.get_scope_var(name='Sub'),
                                                                posargs='[]',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_method(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='inst'),
                                                                name='base',
                                                                posargs='[]',
                                                            ),
                                                            b='from-base',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_method(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='inst'),
                                                                name='child',
                                                                posargs='[]',
                                                            ),
                                                            b='from-child',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='isSubclass',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(name='A', substack=[]),
                                                h.gceOOP.create_subclass_at(name='B', superclass='A', substack=[]),
                                                h.gceOOP.create_subclass_at(name='C', superclass='B', substack=[]),
                                                h.gceTestRunner.test_scope(
                                                    name='Direct and transitive subclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_subclass(subclass='B', superclass='A'),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_subclass(subclass='C', superclass='A'),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_subclass(subclass='C', superclass='B'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Reverse is false',
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceOOP.is_subclass(subclass='A', superclass='B'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceOOP.is_subclass(subclass='A', superclass='C'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='A class is kinda a subclass of itself',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_subclass(subclass='A', superclass='A'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='getSuperclass',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(name='Root', substack=[]),
                                                h.gceOOP.create_subclass_at(name='Branch', superclass='Root', substack=[]),
                                                h.gceTestRunner.test_scope(
                                                    name='Superclass of Branch is Root',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='Root',
                                                            value=h.gceOOP.get_superclass(class_='Branch'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name="Root's superclass is the built-in Superclass",
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='Superclass',
                                                            value=h.gceOOP.get_superclass(class_='Root'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Superclass of the built-in Superclass is Nothing',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                                value=h.gceOOP.get_superclass(
                                                                    class_=h.gceOOP.get_superclass(class_='Root'),
                                                                ),
                                                                type='Nothing (GCE)',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Missing class throws',
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    expr=h.gceOOP.get_superclass(class_='__no_such_class__'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='onClass: add instance method',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Define class with no methods, then add one via onClass',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(name='Greeter', substack=[]),
                                                        h.gceOOP.on_class(
                                                            class_='Greeter',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(argnames='["name"]', argdefaults='[]'),
                                                                h.gceOOP.define_instance_method(
                                                                    name='hello',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.operator.join(
                                                                                string1='Hello, ',
                                                                                string2=h.gceFuncsScopes.get_scope_var(name='name'),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='g',
                                                            value=h.gceOOP.create_instance(class_='Greeter', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Method added via onClass is callable',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.call_method(
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='g'),
                                                                        name='hello',
                                                                        posargs='["World"]',
                                                                    ),
                                                                    b='Hello, World',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='onClass: add static method',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(name='Util', substack=[]),
                                                h.gceOOP.on_class(
                                                    class_='Util',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(argnames='["x"]', argdefaults='[]'),
                                                        h.gceOOP.define_static_method(
                                                            name='double',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    value=h.operator.multiply(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='x'),
                                                                        operand2='2',
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Static method added via onClass is callable',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_static_method(class_='Util', name='double', posargs='["7"]'),
                                                            b='14',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='onClass: currentClass inside body',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='currentClass used inside onClass body sets a class variable',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(name='Tagged', substack=[]),
                                                        h.gceOOP.on_class(
                                                            class_='Tagged',
                                                            substack=[
                                                                h.gceOOP.set_class_variable(class_=h.gceOOP.current_class(), name='source', value='on-class'),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.get_class_variable(name='source', class_='Tagged'),
                                                            b='on-class',
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Multiple onClass calls accumulate class variables',
                                                            substack=[
                                                                h.gceOOP.on_class(
                                                                    class_='Tagged',
                                                                    substack=[
                                                                        h.gceOOP.set_class_variable(class_=h.gceOOP.current_class(), name='extra', value='second'),
                                                                    ],
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_class_variable(name='source', class_='Tagged'),
                                                                    b='on-class',
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_class_variable(name='extra', class_='Tagged'),
                                                                    b='second',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='onClass: visible in propertyNamesOfClass',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Method added via onClass appears in property list',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(name='Widget', substack=[]),
                                                        h.gceTestRunner.test_scope(
                                                            name='No methods yet',
                                                            substack=[
                                                                h.gceTestRunner.assert_text_not_in_value(
                                                                    text='render',
                                                                    value=h.gceOOP.property_names_of_class(property='instance method', class_='Widget'),
                                                                ),
                                                                h.gceOOP.on_class(
                                                                    class_='Widget',
                                                                    substack=[
                                                                        h.gceOOP.define_instance_method(
                                                                            name='render',
                                                                            substack=[
                                                                                h.gceFuncsScopes.return_value(value='rendered'),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Method now listed after onClass',
                                                            substack=[
                                                                h.gceTestRunner.assert_text_in_value(
                                                                    text='render',
                                                                    value=h.gceOOP.property_names_of_class(property='instance method', class_='Widget'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='onClass: cleanup on error',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='class def scope cleanup runs even when body throws',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(name='Safe', substack=[]),
                                                        h.gceTestRunner.assert_throws(
                                                            substack=[
                                                                h.gceOOP.on_class(
                                                                    class_='Safe',
                                                                    substack=[
                                                                        h.gceFuncsScopes.execute_expression(
                                                                            expr=h.gceFuncsScopes.get_scope_var(name='__missing__'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='After the error, onClass on same class still works',
                                                            substack=[
                                                                h.gceTestRunner.assert_does_not_throw(
                                                                    substack=[
                                                                        h.gceOOP.on_class(
                                                                            class_='Safe',
                                                                            substack=[
                                                                                h.gceOOP.define_instance_method(
                                                                                    name='ok',
                                                                                    substack=[
                                                                                        h.gceFuncsScopes.return_value(value='ok'),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.call_method(
                                                                        instance=h.gceOOP.create_instance(class_='Safe', posargs='[]'),
                                                                        name='ok',
                                                                        posargs='[]',
                                                                    ),
                                                                    b='ok',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            name='Instance Methods',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    name='basic method call',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Define class with methods, call them on an instance',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='Greeter',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(argnames='["name"]', argdefaults='[]'),
                                                                h.gceOOP.define_instance_method(
                                                                    name='greet',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.operator.join3(
                                                                                string1='Hello, ',
                                                                                string2=h.gceFuncsScopes.get_scope_var(name='name'),
                                                                                string3='!',
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_instance_method(
                                                                    name='getType',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.gceFuncsScopes.typeof_value(value=h.gceOOP.self_value()),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_instance_method(
                                                                    name='getAttr',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.gceOOP.get_attribute(name='label', instance=h.gceOOP.self_value()),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='g',
                                                            value=h.gceOOP.create_instance(class_='Greeter', posargs='[]'),
                                                        ),
                                                        h.gceOOP.set_attribute(
                                                            instance=h.gceFuncsScopes.get_scope_var(name='g'),
                                                            name='label',
                                                            value='test-label',
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Method with arg',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.call_method(
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='g'),
                                                                        name='greet',
                                                                        posargs='["World"]',
                                                                    ),
                                                                    b='Hello, World!',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Same method with different arg',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.call_method(
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='g'),
                                                                        name='greet',
                                                                        posargs='["Alice"]',
                                                                    ),
                                                                    b='Hello, Alice!',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='No-arg method returns correct type string',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.call_method(
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='g'),
                                                                        name='getType',
                                                                        posargs='[]',
                                                                    ),
                                                                    b=h.gceFuncsScopes.typeof_value_selection(type='Class Instance (GCE)'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Method reads self attribute',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.call_method(
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='g'),
                                                                        name='getAttr',
                                                                        posargs='[]',
                                                                    ),
                                                                    b='test-label',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='self is the correct instance',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Two instances with different attribute values',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='Box',
                                                            substack=[
                                                                h.gceOOP.define_instance_method(
                                                                    name='describe',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.operator.join(
                                                                                string1='Box-',
                                                                                string2=h.gceOOP.get_attribute(name='id', instance=h.gceOOP.self_value()),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='b1',
                                                            value=h.gceOOP.create_instance(class_='Box', posargs='[]'),
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='b2',
                                                            value=h.gceOOP.create_instance(class_='Box', posargs='[]'),
                                                        ),
                                                        h.gceOOP.set_attribute(
                                                            instance=h.gceFuncsScopes.get_scope_var(name='b1'),
                                                            name='id',
                                                            value='AAA',
                                                        ),
                                                        h.gceOOP.set_attribute(
                                                            instance=h.gceFuncsScopes.get_scope_var(name='b2'),
                                                            name='id',
                                                            value='BBB',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_method(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='b1'),
                                                                name='describe',
                                                                posargs='[]',
                                                            ),
                                                            b='Box-AAA',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_method(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='b2'),
                                                                name='describe',
                                                                posargs='[]',
                                                            ),
                                                            b='Box-BBB',
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='self is distinct for each instance',
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    condition=h.gceFuncsScopes.check_identity(
                                                                        value1=h.gceFuncsScopes.get_scope_var(name='b1'),
                                                                        value2=h.gceFuncsScopes.get_scope_var(name='b2'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='error cases',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Calling an undefined method throws',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(name='Empty', substack=[]),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='e',
                                                            value=h.gceOOP.create_instance(class_='Empty', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.assert_throws(
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    expr=h.gceOOP.call_method(
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='e'),
                                                                        name='nonExistent',
                                                                        posargs='[]',
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Calling a method on a non-instance throws',
                                            substack=[
                                                h.gceTestRunner.assert_throws(
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            expr=h.gceOOP.call_method(instance='not-an-instance', name='anyMethod', posargs='[]'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='method with yield point',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Method body that includes sayforsecs (yielding block) returns correctly and waits',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='Speaker',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(argnames='["msg"]', argdefaults='[]'),
                                                                h.gceOOP.define_instance_method(
                                                                    name='speak',
                                                                    substack=[
                                                                        h.looks.sayforsecs(
                                                                            message=h.gceFuncsScopes.get_scope_var(name='msg'),
                                                                            seconds='0.5',
                                                                        ),
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.operator.join(
                                                                                string1='said: ',
                                                                                string2=h.gceFuncsScopes.get_scope_var(name='msg'),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='s',
                                                            value=h.gceOOP.create_instance(class_='Speaker', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Return value is correct after yield',
                                                            substack=[
                                                                h.sensing.resettimer(),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.call_method(
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='s'),
                                                                        name='speak',
                                                                        posargs='["hello"]',
                                                                    ),
                                                                    b='said: hello',
                                                                ),
                                                                h.gceTestRunner.test_scope(
                                                                    name='At least 0.4s elapsed (sayforsecs 0.5s actually waited)',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_(
                                                                            condition=h.operator.gt(operand1=h.sensing.timer(), operand2='0.4'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Second call also returns correctly and also waits',
                                                            substack=[
                                                                h.sensing.resettimer(),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.call_method(
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='s'),
                                                                        name='speak',
                                                                        posargs='["world"]',
                                                                    ),
                                                                    b='said: world',
                                                                ),
                                                                h.gceTestRunner.test_scope(
                                                                    name='At least 0.4s elapsed on second call too',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_(
                                                                            condition=h.operator.gt(operand1=h.sensing.timer(), operand2='0.4'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            name='Special Method: init',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    name='init sets attributes from args',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Define class whose init sets x and y from positional args',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='Point',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(argnames='["x","y"]', argdefaults='[]'),
                                                                h.gceOOP.define_special_method(
                                                                    special_method='init',
                                                                    substack=[
                                                                        h.gceOOP.set_attribute(
                                                                            instance=h.gceOOP.self_value(),
                                                                            name='x',
                                                                            value=h.gceFuncsScopes.get_scope_var(name='x'),
                                                                        ),
                                                                        h.gceOOP.set_attribute(
                                                                            instance=h.gceOOP.self_value(),
                                                                            name='y',
                                                                            value=h.gceFuncsScopes.get_scope_var(name='y'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='p',
                                                            value=h.gceOOP.create_instance(class_='Point', posargs='["3","4"]'),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.get_attribute(
                                                                name='x',
                                                                instance=h.gceFuncsScopes.get_scope_var(name='p'),
                                                            ),
                                                            b='3',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.get_attribute(
                                                                name='y',
                                                                instance=h.gceFuncsScopes.get_scope_var(name='p'),
                                                            ),
                                                            b='4',
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Second instance has independent values',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    name='q',
                                                                    value=h.gceOOP.create_instance(class_='Point', posargs='["10","20"]'),
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='x',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='q'),
                                                                    ),
                                                                    b='10',
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='y',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='q'),
                                                                    ),
                                                                    b='20',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='First instance unchanged after second is created',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='x',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='p'),
                                                                    ),
                                                                    b='3',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='init with default args',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Defaults fill in when args omitted',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='Color',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(argnames='["r","g","b"]', argdefaults='["0","0","0"]'),
                                                                h.gceOOP.define_special_method(
                                                                    special_method='init',
                                                                    substack=[
                                                                        h.gceOOP.set_attribute(
                                                                            instance=h.gceOOP.self_value(),
                                                                            name='r',
                                                                            value=h.gceFuncsScopes.get_scope_var(name='r'),
                                                                        ),
                                                                        h.gceOOP.set_attribute(
                                                                            instance=h.gceOOP.self_value(),
                                                                            name='g',
                                                                            value=h.gceFuncsScopes.get_scope_var(name='g'),
                                                                        ),
                                                                        h.gceOOP.set_attribute(
                                                                            instance=h.gceOOP.self_value(),
                                                                            name='b',
                                                                            value=h.gceFuncsScopes.get_scope_var(name='b'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='All defaults: r=0, g=0, b=0',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    name='black',
                                                                    value=h.gceOOP.create_instance(class_='Color', posargs='[]'),
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='r',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='black'),
                                                                    ),
                                                                    b='0',
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='g',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='black'),
                                                                    ),
                                                                    b='0',
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='b',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='black'),
                                                                    ),
                                                                    b='0',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Partial override: r=255',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    name='red',
                                                                    value=h.gceOOP.create_instance(class_='Color', posargs='["255"]'),
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='r',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='red'),
                                                                    ),
                                                                    b='255',
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='g',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='red'),
                                                                    ),
                                                                    b='0',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Full args',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    name='custom',
                                                                    value=h.gceOOP.create_instance(class_='Color', posargs='["10","20","30"]'),
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='b',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='custom'),
                                                                    ),
                                                                    b='30',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='subclass init calls super init',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Subclass init calls callSuperInitMethod',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='Shape',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(argnames='["color"]', argdefaults='[]'),
                                                                h.gceOOP.define_special_method(
                                                                    special_method='init',
                                                                    substack=[
                                                                        h.gceOOP.set_attribute(
                                                                            instance=h.gceOOP.self_value(),
                                                                            name='color',
                                                                            value=h.gceFuncsScopes.get_scope_var(name='color'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.create_subclass_at(
                                                            name='Circle',
                                                            superclass='Shape',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(argnames='["radius","color"]', argdefaults='[]'),
                                                                h.gceOOP.define_special_method(
                                                                    special_method='init',
                                                                    substack=[
                                                                        h.gceFuncsScopes.execute_expression(
                                                                            expr=h.gceOOP.call_super_init_method(posargs='["blue"]'),
                                                                        ),
                                                                        h.gceOOP.set_attribute(
                                                                            instance=h.gceOOP.self_value(),
                                                                            name='radius',
                                                                            value=h.gceFuncsScopes.get_scope_var(name='radius'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='c',
                                                            value=h.gceOOP.create_instance(class_='Circle', posargs='["5","ignored"]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='radius set by Circle init',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='radius',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                    ),
                                                                    b='5',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='color set by super (Shape) init with hardcoded value',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='color',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                    ),
                                                                    b='blue',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            name='Inheritance and Super',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    name='isSubclass',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(name='A', substack=[]),
                                                h.gceOOP.create_subclass_at(name='B', superclass='A', substack=[]),
                                                h.gceOOP.create_subclass_at(name='C', superclass='B', substack=[]),
                                                h.gceTestRunner.test_scope(
                                                    name='Direct subclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_subclass(subclass='B', superclass='A'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Transitive subclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_subclass(subclass='C', superclass='A'),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_subclass(subclass='C', superclass='B'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Reverse is false',
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceOOP.is_subclass(subclass='A', superclass='B'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceOOP.is_subclass(subclass='A', superclass='C'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='A class is a subclass of itself',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_subclass(subclass='A', superclass='A'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='isInstance with inheritance',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(name='Vehicle', substack=[]),
                                                h.gceOOP.create_subclass_at(name='Car', superclass='Vehicle', substack=[]),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='v',
                                                    value=h.gceOOP.create_instance(class_='Vehicle', posargs='[]'),
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='c',
                                                    value=h.gceOOP.create_instance(class_='Car', posargs='[]'),
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Instance is instance of own class',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_instance(
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(name='v'),
                                                                class_='Vehicle',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_instance(
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                class_='Car',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Subclass instance is instance of superclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_instance(
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                class_='Vehicle',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Superclass instance is NOT instance of subclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceOOP.is_instance(
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(name='v'),
                                                                class_='Car',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='method override and super',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    name='Animal',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            name='speak',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(value='generic sound'),
                                                            ],
                                                        ),
                                                        h.gceOOP.define_instance_method(
                                                            name='breathe',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(value='breathing'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceOOP.create_subclass_at(
                                                    name='Dog',
                                                    superclass='Animal',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            name='speak',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    value=h.operator.join(
                                                                        string1=h.gceOOP.call_super_method(name='speak', posargs='[]'),
                                                                        string2=' (but louder)',
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='a',
                                                    value=h.gceOOP.create_instance(class_='Animal', posargs='[]'),
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='d',
                                                    value=h.gceOOP.create_instance(class_='Dog', posargs='[]'),
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Overridden method returns augmented result',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_method(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='d'),
                                                                name='speak',
                                                                posargs='[]',
                                                            ),
                                                            b='generic sound (but louder)',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Parent method still returns original',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_method(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                name='speak',
                                                                posargs='[]',
                                                            ),
                                                            b='generic sound',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Inherited (non-overridden) method works on subclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_method(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='d'),
                                                                name='breathe',
                                                                posargs='[]',
                                                            ),
                                                            b='breathing',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='getSuperclass',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(name='Base', substack=[]),
                                                h.gceOOP.create_subclass_at(name='Child', superclass='Base', substack=[]),
                                                h.gceTestRunner.test_scope(
                                                    name='Superclass of Child is Base',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='Base',
                                                            value=h.gceOOP.get_superclass(class_='Child'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Superclass of Base is built-in Superclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='Superclass',
                                                            value=h.gceOOP.get_superclass(class_='Base'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='getSuperclass on a missing class name throws',
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    expr=h.gceOOP.get_superclass(class_='__no_such_class__'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            name='Getters and Setters',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    name='setter transforms and stores, getter retrieves',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name="Setter prepends 'set:'; getter appends ':get'",
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='Box',
                                                            substack=[
                                                                h.gceOOP.define_setter(
                                                                    name='size',
                                                                    substack=[
                                                                        h.gceOOP.set_attribute(
                                                                            instance=h.gceOOP.self_value(),
                                                                            name='_size',
                                                                            value=h.operator.join(string1='set:', string2=h.gceOOP.define_setter_value()),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_getter(
                                                                    name='size',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.operator.join(
                                                                                string1=h.gceOOP.get_attribute(name='_size', instance=h.gceOOP.self_value()),
                                                                                string2=':get',
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='b',
                                                            value=h.gceOOP.create_instance(class_='Box', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='setAttribute goes through setter',
                                                            substack=[
                                                                h.gceOOP.set_attribute(
                                                                    instance=h.gceFuncsScopes.get_scope_var(name='b'),
                                                                    name='size',
                                                                    value='42',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Raw _size attribute reflects setter transformation',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='_size',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='b'),
                                                                    ),
                                                                    b='set:42',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='getAttribute goes through getter',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='size',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='b'),
                                                                    ),
                                                                    b='set:42:get',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Update via setter replaces stored value',
                                                            substack=[
                                                                h.gceOOP.set_attribute(
                                                                    instance=h.gceFuncsScopes.get_scope_var(name='b'),
                                                                    name='size',
                                                                    value='hello',
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='_size',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='b'),
                                                                    ),
                                                                    b='set:hello',
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='size',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='b'),
                                                                    ),
                                                                    b='set:hello:get',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='getter-only attribute',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Getter for computed read-only value',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='Circle',
                                                            substack=[
                                                                h.gceOOP.define_getter(
                                                                    name='doubled',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.operator.multiply(
                                                                                operand1=h.gceOOP.get_attribute(name='_val', instance=h.gceOOP.self_value()),
                                                                                operand2='2',
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='c',
                                                            value=h.gceOOP.create_instance(class_='Circle', posargs='[]'),
                                                        ),
                                                        h.gceOOP.set_attribute(
                                                            instance=h.gceFuncsScopes.get_scope_var(name='c'),
                                                            name='_val',
                                                            value='7',
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='getter doubles _val',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='doubled',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                    ),
                                                                    b='14',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Raw _val unaffected',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.gceOOP.get_attribute(
                                                                        name='_val',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                    ),
                                                                    b='7',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='attributes without getter/setter bypass directly',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='setAttribute and getAttribute on plain attributes',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(name='Plain', substack=[]),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='p',
                                                            value=h.gceOOP.create_instance(class_='Plain', posargs='[]'),
                                                        ),
                                                        h.gceOOP.set_attribute(
                                                            instance=h.gceFuncsScopes.get_scope_var(name='p'),
                                                            name='x',
                                                            value='99',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.get_attribute(
                                                                name='x',
                                                                instance=h.gceFuncsScopes.get_scope_var(name='p'),
                                                            ),
                                                            b='99',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            name='Operator Methods',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    name='left add operator',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Custom class with left add: returns val + operand',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='MyNum',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(argnames='["val"]', argdefaults='[]'),
                                                                h.gceOOP.define_special_method(
                                                                    special_method='init',
                                                                    substack=[
                                                                        h.gceOOP.set_attribute(
                                                                            instance=h.gceOOP.self_value(),
                                                                            name='val',
                                                                            value=h.gceFuncsScopes.get_scope_var(name='val'),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='left add',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.operator.add(
                                                                                operand1=h.gceOOP.get_attribute(name='val', instance=h.gceOOP.self_value()),
                                                                                operand2=h.gceOOP.operator_operator_value(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='left subtract',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.operator.subtract(
                                                                                operand1=h.gceOOP.get_attribute(name='val', instance=h.gceOOP.self_value()),
                                                                                operand2=h.gceOOP.operator_operator_value(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='n',
                                                            value=h.gceOOP.create_instance(class_='MyNum', posargs='["10"]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='left add: 10 + 5 = 15',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.operator.add(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='n'),
                                                                        operand2='5',
                                                                    ),
                                                                    b='15',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='left add: 10 + 0 = 10',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.operator.add(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='n'),
                                                                        operand2='0',
                                                                    ),
                                                                    b='10',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='left subtract: 10 - 3 = 7',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.operator.subtract(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='n'),
                                                                        operand2='3',
                                                                    ),
                                                                    b='7',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='equals operator',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Custom equals: compares val attribute',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='Token',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(argnames='["id"]', argdefaults='[]'),
                                                                h.gceOOP.define_special_method(
                                                                    special_method='init',
                                                                    substack=[
                                                                        h.gceOOP.set_attribute(
                                                                            instance=h.gceOOP.self_value(),
                                                                            name='id',
                                                                            value=h.gceFuncsScopes.get_scope_var(name='id'),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='equals',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.operator.equals(
                                                                                operand1=h.gceOOP.get_attribute(name='id', instance=h.gceOOP.self_value()),
                                                                                operand2=h.gceOOP.operator_operator_value(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='tok',
                                                            value=h.gceOOP.create_instance(class_='Token', posargs='["abc"]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Equals the stored id',
                                                            substack=[
                                                                h.gceTestRunner.assert_(
                                                                    condition=h.operator.equals(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='tok'),
                                                                        operand2='abc',
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Does not equal a different value',
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    condition=h.operator.equals(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='tok'),
                                                                        operand2='xyz',
                                                                    ),
                                                                ),
                                                                h.gceTestRunner.assert_not(
                                                                    condition=h.operator.equals(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='tok'),
                                                                        operand2='',
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='reverse operations',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Right-side method is used when left operand has no matching method',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='RightOnly',
                                                            substack=[
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='right add',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.operator.join(string1='R+', string2=h.gceOOP.operator_operator_value()),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='r',
                                                            value=h.gceOOP.create_instance(class_='RightOnly', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='plain_number + instance: triggers right add',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.operator.add(
                                                                        operand1='7',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(name='r'),
                                                                    ),
                                                                    b='R+7',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Comparison reverse: op.greater triggers right-side less-than method',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='CompRight',
                                                            substack=[
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='less than',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            value=h.operator.lt(
                                                                                operand1=h.gceOOP.operator_operator_value(),
                                                                                operand2=h.gceOOP.get_attribute(name='threshold', instance=h.gceOOP.self_value()),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='c',
                                                            value=h.gceOOP.create_instance(class_='CompRight', posargs='[]'),
                                                        ),
                                                        h.gceOOP.set_attribute(
                                                            instance=h.gceFuncsScopes.get_scope_var(name='c'),
                                                            name='threshold',
                                                            value='10',
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name="5 > c: triggers c's less-than with operator_value=5; 5<10 is true",
                                                            substack=[
                                                                h.gceTestRunner.assert_(
                                                                    condition=h.operator.gt(
                                                                        operand1='5',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='15 > c: operator_value=15; 15<10 is false',
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    condition=h.operator.gt(
                                                                        operand1='15',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='all operator kinds',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Arithmetic operator kinds: each left/right variant is callable',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='ArithOps',
                                                            substack=[
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='left add',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='L+'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='right add',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='R+'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='left subtract',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='L-'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='right subtract',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='R-'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='left multiply',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='L*'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='right multiply',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='R*'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='left divide',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='L/'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='right divide',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='R/'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='left power',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='L^'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='right power',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='R^'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='left mod',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='L%'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='right mod',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='R%'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='a',
                                                            value=h.gceOOP.create_instance(class_='ArithOps', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Left-side arithmetic methods',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.operator.add(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                        operand2='0',
                                                                    ),
                                                                    b='L+',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.operator.subtract(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                        operand2='0',
                                                                    ),
                                                                    b='L-',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.operator.multiply(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                        operand2='1',
                                                                    ),
                                                                    b='L*',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.operator.divide(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                        operand2='1',
                                                                    ),
                                                                    b='L/',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.operator.power(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                        operand2='1',
                                                                    ),
                                                                    b='L^',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.operator.mod(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                        operand2='1',
                                                                    ),
                                                                    b='L%',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Right-side arithmetic methods (plain number on left)',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.operator.add(
                                                                        operand1='0',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                    ),
                                                                    b='R+',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.operator.subtract(
                                                                        operand1='0',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                    ),
                                                                    b='R-',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.operator.multiply(
                                                                        operand1='1',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                    ),
                                                                    b='R*',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.operator.divide(
                                                                        operand1='1',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                    ),
                                                                    b='R/',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.operator.power(
                                                                        operand1='1',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                    ),
                                                                    b='R^',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    a=h.operator.mod(
                                                                        operand1='1',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                    ),
                                                                    b='R%',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Comparison operator kinds: each kind is callable',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='CompOps',
                                                            substack=[
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='equals',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value=h.operator.true_boolean()),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='not equals',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value=h.operator.true_boolean()),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='greater than',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value=h.operator.true_boolean()),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='greater or equal',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value=h.operator.true_boolean()),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='less than',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value=h.operator.true_boolean()),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    operator_kind='less or equal',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value=h.operator.true_boolean()),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='c',
                                                            value=h.gceOOP.create_instance(class_='CompOps', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.operator.equals(
                                                                operand1=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                operand2='x',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.operator.notequal(
                                                                operand1=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                operand2='x',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.operator.gt(
                                                                operand1=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                operand2='x',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.operator.gtorequal(
                                                                operand1=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                operand2='x',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.operator.lt(
                                                                operand1=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                operand2='x',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.operator.ltorequal(
                                                                operand1=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                operand2='x',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            name='Static Methods',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    name='define and call a static method',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    name='MathUtils',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(argnames='["x"]', argdefaults='[]'),
                                                        h.gceOOP.define_static_method(
                                                            name='square',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    value=h.operator.multiply(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='x'),
                                                                        operand2=h.gceFuncsScopes.get_scope_var(name='x'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.configure_next_function_args(argnames='["a","b"]', argdefaults='[]'),
                                                        h.gceOOP.define_static_method(
                                                            name='add',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    value=h.operator.add(
                                                                        operand1=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                        operand2=h.gceFuncsScopes.get_scope_var(name='b'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='callStaticMethod: square(4) = 16',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceOOP.call_static_method(class_='MathUtils', name='square', posargs='["4"]'),
                                                            b='16',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='callStaticMethod: square(0) = 0',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceOOP.call_static_method(class_='MathUtils', name='square', posargs='["0"]'),
                                                            b='0',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='callStaticMethod: add(3, 7) = 10',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            a=h.gceOOP.call_static_method(class_='MathUtils', name='add', posargs='["3","7"]'),
                                                            b='10',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='getStaticMethodFunc + callFunction',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    name='Fmt',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(argnames='["val"]', argdefaults='[]'),
                                                        h.gceOOP.define_static_method(
                                                            name='wrap',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    value=h.operator.join3(
                                                                        string1='[',
                                                                        string2=h.gceFuncsScopes.get_scope_var(name='val'),
                                                                        string3=']',
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='getStaticMethodFunc returns a callable function',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            name='wrapFn',
                                                            value=h.gceOOP.get_static_method_func(name='wrap', class_='Fmt'),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceFuncsScopes.typeof_value(
                                                                value=h.gceFuncsScopes.get_scope_var(name='wrapFn'),
                                                            ),
                                                            b=h.gceFuncsScopes.typeof_value_selection(type='Function (GCE)'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='callFunction on retrieved static method',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceFuncsScopes.call_function(func='wrapFn', posargs='["hello"]'),
                                                            b='[hello]',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Both callStaticMethod and callFunction give same result',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_static_method(class_='Fmt', name='wrap', posargs='["world"]'),
                                                            b=h.gceFuncsScopes.call_function(func='wrapFn', posargs='["world"]'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='error cases',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(name='Solo', substack=[]),
                                                h.gceTestRunner.test_scope(
                                                    name='Calling a non-existent static method throws',
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    expr=h.gceOOP.call_static_method(class_='Solo', name='missing', posargs='[]'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            name='Class Variables',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    name='set and get class variable',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(name='Counter', substack=[]),
                                                h.gceTestRunner.test_scope(
                                                    name='Set and read a class variable',
                                                    substack=[
                                                        h.gceOOP.set_class_variable(class_='Counter', name='count', value='0'),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.get_class_variable(name='count', class_='Counter'),
                                                            b='0',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Update the class variable',
                                                    substack=[
                                                        h.gceOOP.set_class_variable(class_='Counter', name='count', value='42'),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.get_class_variable(name='count', class_='Counter'),
                                                            b='42',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Multiple class variables coexist',
                                                    substack=[
                                                        h.gceOOP.set_class_variable(class_='Counter', name='name', value='MyCounter'),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.get_class_variable(name='name', class_='Counter'),
                                                            b='MyCounter',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Reading first variable unchanged',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.get_class_variable(name='count', class_='Counter'),
                                                            b='42',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='propertyNamesOfClass reflects class variables',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    name='Config',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            name='doWork',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(value='done'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceOOP.set_class_variable(class_='Config', name='version', value='1'),
                                                h.gceOOP.set_class_variable(class_='Config', name='author', value='test'),
                                                h.gceTestRunner.test_scope(
                                                    name='Class variable names listed',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='version',
                                                            value=h.gceOOP.property_names_of_class(property='class variable', class_='Config'),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='author',
                                                            value=h.gceOOP.property_names_of_class(property='class variable', class_='Config'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Method names NOT in class variable list',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            text='doWork',
                                                            value=h.gceOOP.property_names_of_class(property='class variable', class_='Config'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Instance method names listed correctly',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='doWork',
                                                            value=h.gceOOP.property_names_of_class(property='instance method', class_='Config'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Class variable names NOT in instance method list',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            text='version',
                                                            value=h.gceOOP.property_names_of_class(property='instance method', class_='Config'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='delete class variable',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(name='Bag', substack=[]),
                                                h.gceOOP.set_class_variable(class_='Bag', name='keep', value='yes'),
                                                h.gceOOP.set_class_variable(class_='Bag', name='remove', value='no'),
                                                h.gceTestRunner.test_scope(
                                                    name='Both exist before delete',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='keep',
                                                            value=h.gceOOP.property_names_of_class(property='class variable', class_='Bag'),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='remove',
                                                            value=h.gceOOP.property_names_of_class(property='class variable', class_='Bag'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Delete one',
                                                    substack=[
                                                        h.gceOOP.delete_class_variable(class_='Bag', name='remove'),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Deleted variable throws on get',
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    expr=h.gceOOP.get_class_variable(name='remove', class_='Bag'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Deleted variable absent from property names',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            text='remove',
                                                            value=h.gceOOP.property_names_of_class(property='class variable', class_='Bag'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Other variable unaffected',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='keep',
                                                            value=h.gceOOP.property_names_of_class(property='class variable', class_='Bag'),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.get_class_variable(name='keep', class_='Bag'),
                                                            b='yes',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='class variables are shared across instances',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    name='Shared',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            name='getVar',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    value=h.gceOOP.get_class_variable(name='shared', class_='Shared'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceOOP.set_class_variable(class_='Shared', name='shared', value='initial'),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='i1',
                                                    value=h.gceOOP.create_instance(class_='Shared', posargs='[]'),
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='i2',
                                                    value=h.gceOOP.create_instance(class_='Shared', posargs='[]'),
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Both instances see the same class variable',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_method(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='i1'),
                                                                name='getVar',
                                                                posargs='[]',
                                                            ),
                                                            b='initial',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_method(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='i2'),
                                                                name='getVar',
                                                                posargs='[]',
                                                            ),
                                                            b='initial',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Update class variable - both instances see new value',
                                                    substack=[
                                                        h.gceOOP.set_class_variable(class_='Shared', name='shared', value='updated'),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_method(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='i1'),
                                                                name='getVar',
                                                                posargs='[]',
                                                            ),
                                                            b='updated',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.call_method(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='i2'),
                                                                name='getVar',
                                                                posargs='[]',
                                                            ),
                                                            b='updated',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            name='Introspection',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    name='getAttribute and setAttribute (direct)',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    name='Person',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(argnames='["name"]', argdefaults='[]'),
                                                        h.gceOOP.define_special_method(
                                                            special_method='init',
                                                            substack=[
                                                                h.gceOOP.set_attribute(
                                                                    instance=h.gceOOP.self_value(),
                                                                    name='name',
                                                                    value=h.gceFuncsScopes.get_scope_var(name='name'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.define_instance_method(
                                                            name='greet',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    value=h.operator.join(
                                                                        string1='Hi, ',
                                                                        string2=h.gceOOP.get_attribute(name='name', instance=h.gceOOP.self_value()),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceOOP.create_subclass_at(name='Employee', superclass='Person', substack=[]),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='p',
                                                    value=h.gceOOP.create_instance(class_='Person', posargs='["Bob"]'),
                                                ),
                                                h.gceOOP.set_attribute(
                                                    instance=h.gceFuncsScopes.get_scope_var(name='p'),
                                                    name='age',
                                                    value='30',
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Attribute set via init',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.get_attribute(
                                                                name='name',
                                                                instance=h.gceFuncsScopes.get_scope_var(name='p'),
                                                            ),
                                                            b='Bob',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Attribute set after creation',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.get_attribute(
                                                                name='age',
                                                                instance=h.gceFuncsScopes.get_scope_var(name='p'),
                                                            ),
                                                            b='30',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Overwrite attribute',
                                                    substack=[
                                                        h.gceOOP.set_attribute(
                                                            instance=h.gceFuncsScopes.get_scope_var(name='p'),
                                                            name='name',
                                                            value='Robert',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            a=h.gceOOP.get_attribute(
                                                                name='name',
                                                                instance=h.gceFuncsScopes.get_scope_var(name='p'),
                                                            ),
                                                            b='Robert',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Missing attribute throws',
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    expr=h.gceOOP.get_attribute(
                                                                        name='missing',
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='p'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='getClassOfInstance',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(name='Cat', substack=[]),
                                                h.gceOOP.create_subclass_at(name='Kitten', superclass='Cat', substack=[]),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='c',
                                                    value=h.gceOOP.create_instance(class_='Cat', posargs='[]'),
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='k',
                                                    value=h.gceOOP.create_instance(class_='Kitten', posargs='[]'),
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='getClassOfInstance contains the class name',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='Cat',
                                                            value=h.gceOOP.get_class_of_instance(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='c'),
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='Kitten',
                                                            value=h.gceOOP.get_class_of_instance(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='k'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Cat instance does NOT report Kitten',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            text='Kitten',
                                                            value=h.gceOOP.get_class_of_instance(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='c'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='isInstance',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(name='Fruit', substack=[]),
                                                h.gceOOP.create_subclass_at(name='Apple', superclass='Fruit', substack=[]),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='f',
                                                    value=h.gceOOP.create_instance(class_='Fruit', posargs='[]'),
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='a',
                                                    value=h.gceOOP.create_instance(class_='Apple', posargs='[]'),
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Instance of own class',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_instance(
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(name='f'),
                                                                class_='Fruit',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_instance(
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                class_='Apple',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Subclass instance is instance of superclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            condition=h.gceOOP.is_instance(
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(name='a'),
                                                                class_='Fruit',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Superclass instance is NOT instance of subclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceOOP.is_instance(
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(name='f'),
                                                                class_='Apple',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Non-instance values return false',
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceOOP.is_instance(potential_instance='hello', class_='Fruit'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            condition=h.gceOOP.is_instance(potential_instance=h.gceFuncsScopes.nothing(), class_='Fruit'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='propertyNamesOfClass',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    name='Widget',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            name='render',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(value='rendered'),
                                                            ],
                                                        ),
                                                        h.gceOOP.define_static_method(
                                                            name='create',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(value='widget'),
                                                            ],
                                                        ),
                                                        h.gceOOP.define_getter(
                                                            name='width',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    value=h.gceOOP.get_attribute(name='_w', instance=h.gceOOP.self_value()),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.define_setter(
                                                            name='height',
                                                            substack=[
                                                                h.gceOOP.set_attribute(instance=h.gceOOP.self_value(), name='_h', value=h.gceOOP.define_setter_value()),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceOOP.set_class_variable(class_='Widget', name='version', value='2'),
                                                h.gceTestRunner.test_scope(
                                                    name='Instance methods',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='render',
                                                            value=h.gceOOP.property_names_of_class(property='instance method', class_='Widget'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            text='create',
                                                            value=h.gceOOP.property_names_of_class(property='instance method', class_='Widget'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Static methods',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='create',
                                                            value=h.gceOOP.property_names_of_class(property='static method', class_='Widget'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            text='render',
                                                            value=h.gceOOP.property_names_of_class(property='static method', class_='Widget'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Getter methods',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='width',
                                                            value=h.gceOOP.property_names_of_class(property='getter method', class_='Widget'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            text='height',
                                                            value=h.gceOOP.property_names_of_class(property='getter method', class_='Widget'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Setter methods',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='height',
                                                            value=h.gceOOP.property_names_of_class(property='setter method', class_='Widget'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            text='width',
                                                            value=h.gceOOP.property_names_of_class(property='setter method', class_='Widget'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Class variables',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='version',
                                                            value=h.gceOOP.property_names_of_class(property='class variable', class_='Widget'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='propertyNamesOfClass edge cases',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            name='Empty class has no own instance methods (beyond built-in)',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(name='Empty', substack=[]),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            text='render',
                                                            value=h.gceOOP.property_names_of_class(property='instance method', class_='Empty'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            text='create',
                                                            value=h.gceOOP.property_names_of_class(property='static method', class_='Empty'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            text='version',
                                                            value=h.gceOOP.property_names_of_class(property='class variable', class_='Empty'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Subclass without own methods still sees inherited methods',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='Parent',
                                                            substack=[
                                                                h.gceOOP.define_instance_method(
                                                                    name='inherited',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='from-parent'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_static_method(
                                                                    name='parentStatic',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='static-from-parent'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.create_subclass_at(name='ChildNoMethods', superclass='Parent', substack=[]),
                                                        h.gceTestRunner.test_scope(
                                                            name='Inherited instance method visible on child',
                                                            substack=[
                                                                h.gceTestRunner.assert_text_in_value(
                                                                    text='inherited',
                                                                    value=h.gceOOP.property_names_of_class(property='instance method', class_='ChildNoMethods'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Inherited static method visible on child',
                                                            substack=[
                                                                h.gceTestRunner.assert_text_in_value(
                                                                    text='parentStatic',
                                                                    value=h.gceOOP.property_names_of_class(property='static method', class_='ChildNoMethods'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name="Parent's own methods also still visible on parent",
                                                            substack=[
                                                                h.gceTestRunner.assert_text_in_value(
                                                                    text='inherited',
                                                                    value=h.gceOOP.property_names_of_class(property='instance method', class_='Parent'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            name='Overriding a method replaces it, not duplicates it',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='Base2',
                                                            substack=[
                                                                h.gceOOP.define_instance_method(
                                                                    name='greet',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='base-greet'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.create_subclass_at(
                                                            name='Child2',
                                                            superclass='Base2',
                                                            substack=[
                                                                h.gceOOP.define_instance_method(
                                                                    name='greet',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='child-greet'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name="greet appears in child's instance methods",
                                                            substack=[
                                                                h.gceTestRunner.assert_text_in_value(
                                                                    text='greet',
                                                                    value=h.gceOOP.property_names_of_class(property='instance method', class_='Child2'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            name='Override is active — child instance calls child version',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    name='c',
                                                                    value=h.gceOOP.create_instance(class_='Child2', posargs='[]'),
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    a=h.gceOOP.call_method(
                                                                        instance=h.gceFuncsScopes.get_scope_var(name='c'),
                                                                        name='greet',
                                                                        posargs='[]',
                                                                    ),
                                                                    b='child-greet',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='getAllAttributes',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(name='Data', substack=[]),
                                                h.gceFuncsScopes.set_scope_var(
                                                    name='d',
                                                    value=h.gceOOP.create_instance(class_='Data', posargs='[]'),
                                                ),
                                                h.gceOOP.set_attribute(
                                                    instance=h.gceFuncsScopes.get_scope_var(name='d'),
                                                    name='x',
                                                    value='1',
                                                ),
                                                h.gceOOP.set_attribute(
                                                    instance=h.gceFuncsScopes.get_scope_var(name='d'),
                                                    name='y',
                                                    value='2',
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='getAllAttributes includes all set attributes',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='x',
                                                            value=h.gceOOP.get_all_attributes(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='d'),
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='y',
                                                            value=h.gceOOP.get_all_attributes(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='d'),
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='1',
                                                            value=h.gceOOP.get_all_attributes(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='d'),
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='2',
                                                            value=h.gceOOP.get_all_attributes(
                                                                instance=h.gceFuncsScopes.get_scope_var(name='d'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='propertyNamesOfClass: special method dropdown',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    name='Nameable',
                                                    substack=[
                                                        h.gceOOP.define_special_method(special_method='init', substack=[]),
                                                        h.gceOOP.define_special_method(
                                                            special_method='as string',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(value='nameable'),
                                                            ],
                                                        ),
                                                        h.gceOOP.define_operator_method(
                                                            operator_kind='left add',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    value=h.operator.join(string1='L+', string2=h.gceOOP.operator_operator_value()),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.define_operator_method(
                                                            operator_kind='not equals',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(value=h.operator.true_boolean()),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name="init appears as 'init' in special method list",
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='init',
                                                            value=h.gceOOP.property_names_of_class(property='special method', class_='Nameable'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name="as string appears as 'as string' in special method list",
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='as string',
                                                            value=h.gceOOP.property_names_of_class(property='special method', class_='Nameable'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Special methods do NOT appear in instance method list',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            text='init',
                                                            value=h.gceOOP.property_names_of_class(property='instance method', class_='Nameable'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            text='as string',
                                                            value=h.gceOOP.property_names_of_class(property='instance method', class_='Nameable'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Operator methods appear as public names in operator method list',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='left add',
                                                            value=h.gceOOP.property_names_of_class(property='operator method', class_='Nameable'),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='not equals',
                                                            value=h.gceOOP.property_names_of_class(property='operator method', class_='Nameable'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Operator methods do NOT appear in instance or special method list',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            text='left add',
                                                            value=h.gceOOP.property_names_of_class(property='instance method', class_='Nameable'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            text='left add',
                                                            value=h.gceOOP.property_names_of_class(property='special method', class_='Nameable'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    name='propertyNamesOfClass: special method inheritance',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    name='Empty class always has init from common superclass',
                                                    substack=[
                                                        h.gceOOP.create_class_at(name='BareClass', substack=[]),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='init',
                                                            value=h.gceOOP.property_names_of_class(property='special method', class_='BareClass'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Class with only as string still inherits init',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='AsStringOnly',
                                                            substack=[
                                                                h.gceOOP.define_special_method(
                                                                    special_method='as string',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='str'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='init',
                                                            value=h.gceOOP.property_names_of_class(property='special method', class_='AsStringOnly'),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='as string',
                                                            value=h.gceOOP.property_names_of_class(property='special method', class_='AsStringOnly'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Subclass inherits special methods from parent',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='SpBase',
                                                            substack=[
                                                                h.gceOOP.define_special_method(
                                                                    special_method='as string',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='base'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.create_subclass_at(name='SpChild', superclass='SpBase', substack=[]),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='as string',
                                                            value=h.gceOOP.property_names_of_class(property='special method', class_='SpChild'),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='init',
                                                            value=h.gceOOP.property_names_of_class(property='special method', class_='SpChild'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    name='Subclass overriding as string replaces, not duplicates',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            name='SpBase2',
                                                            substack=[
                                                                h.gceOOP.define_special_method(
                                                                    special_method='as string',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='base2'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.create_subclass_at(
                                                            name='SpChild2',
                                                            superclass='SpBase2',
                                                            substack=[
                                                                h.gceOOP.define_special_method(
                                                                    special_method='as string',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(value='child2'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            text='as string',
                                                            value=h.gceOOP.property_names_of_class(property='special method', class_='SpChild2'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    row=None,
                    col=None,
                ),
            ],
            comments=[],
            costumes=[
                t.ThirdVectorCostume(
                    name='empty',
                    file_extension='svg',
                    rotation_center=(240, 180),
                    content='<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" height="2" version="1.1" viewBox="-1 -1 2 2" width="2">\n  <!-- Exported by Scratch - http://scratch.mit.edu/ -->\n</svg>',
                ),
            ],
            sounds=[],
            costume_index=0,
            volume=100,
            name='Test',
            local_variables=[],
            local_lists=[],
            local_monitors=[],
            is_visible=True,
            position=(0, 0),
            size=100,
            direction=90,
            is_draggable=False,
            rotation_style=p.SRSpriteRotationStyle.ALL_AROUND,
            uuid=t.UUID('619ce835-4bfe-4eef-a7d1-eca9503e97e9'),
        ),
    ],
    sprite_layer_stack=[
        t.UUID('95624954-17e8-4863-adef-72fd8d5652e7'),
    ],
    global_variables=[],
    global_lists=[],
    global_monitors=[],
    extensions=[
        p.SRBuiltinExtension(id='jwProto'),
        p.SRCustomExtension(id='dogeiscutSet', url='https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutSet.js'),
        p.SRBuiltinExtension(id='jwLambda'),
        p.SRCustomExtension(id='gceOOP', url='http://localhost:5173/extensions/gceOOP.js'),
        p.SRCustomExtension(id='agBuffer', url='https://extensions.penguinmod.com/extensions/AndrewGaming587/agBuffer.js'),
        p.SRBuiltinExtension(id='jwVector'),
        p.SRBuiltinExtension(id='jwDate'),
        p.SRCustomExtension(id='divIterator', url='https://extensions.penguinmod.com/extensions/Div/divIterators.js'),
        p.SRCustomExtension(id='ddeDateFormatV2', url='https://extensions.penguinmod.com/extensions/ddededodediamante/dateFormatV2.js'),
        p.SRCustomExtension(id='fruitsPaintUtils', url='https://extensions.penguinmod.com/extensions/Fruits555000/PaintUtils.js'),
        p.SRBuiltinExtension(id='jwTargets'),
        p.SRBuiltinExtension(id='jwColor'),
        p.SRCustomExtension(id='gceTestRunner', url='http://localhost:5173/extensions/gceTestRunner.js'),
        p.SRBuiltinExtension(id='jwXML'),
        p.SRCustomExtension(id='dogeiscutObject', url='https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutObject.js'),
        p.SRBuiltinExtension(id='SPjavascriptV2'),
        p.SRBuiltinExtension(id='jwNum'),
        p.SRBuiltinExtension(id='newCanvas'),
        p.SRCustomExtension(id='divAlgEffects', url='https://extensions.penguinmod.com/extensions/Div/divAlgEffects.js'),
        p.SRCustomExtension(id='dogeiscutRegularExpressions', url='https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutRegularExpressions.js'),
        p.SRBuiltinExtension(id='jwArray'),
        p.SRCustomExtension(id='steve0greatnesstimers', url='https://extensions.penguinmod.com/extensions/steve0greatness/timers.js'),
        p.SRCustomExtension(id='gceFuncsScopes', url='http://localhost:5173/extensions/gceFuncsScopes.js'),
        p.SRCustomExtension(id='ddeDateFormat', url='https://extensions.penguinmod.com/extensions/ddededodediamante/dateFormat.js'),
    ],
)