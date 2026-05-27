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
                        h.event.whenflagclicked(OPCODE='&events::when green flag clicked'),
                        h.gceTestRunner.test_scope(
                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                            name='TypeChecker',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='My Types',
                                    substack=[
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.gceFuncsScopes.create_function_named(OPCODE='&gceFuncsScopes::create function named (NAME) {SUBSTACK}', name='myFn', substack=[]),
                                                type='Function (GCE)',
                                            ),
                                        ),
                                        h.jwProto.label_command(OPCODE='&jwProto::// (LABEL) {{id=jwProto_labelCommand}}', label='Methods can not be accessed from a reporter'),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.gceOOP.create_class_named(OPCODE='&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}', name='MyClass', substack=[]),
                                                type='Class (GCE)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.gceOOP.create_instance(
                                                    OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)',
                                                    class_=h.gceOOP.create_class_named(OPCODE='&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}', name='MyClass', substack=[]),
                                                    posargs='[]',
                                                ),
                                                type='Class Instance (GCE)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                type='Nothing (GCE)',
                                            ),
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='Common/Safe JS data types',
                                    substack=[
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.SPjavascriptV2.js_reporter(OPCODE='&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsReporter}}', code='return undefined'),
                                                type='JavaScript Undefined',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.SPjavascriptV2.js_reporter(OPCODE='&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsReporter}}', code='return null'),
                                                type='JavaScript Null',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.operator.true_boolean(OPCODE='&operators::true'),
                                                type='Boolean',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?', value='777', type='Number'),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?', value='hello', type='String'),
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='Custom Extension Types',
                                    substack=[
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.agBuffer.new_buffer(OPCODE='&agBuffer::create new array buffer of size (LENGTH)', length='1'),
                                                type='Buffer (AndrewGaming587)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.agBuffer.create_pointer(
                                                    OPCODE='&agBuffer::create ([TYPE]) pointer for (BUFFER) at (INDEX) <ENDIAN>',
                                                    index='0',
                                                    endian=False,
                                                    buffer=h.agBuffer.new_buffer(OPCODE='&agBuffer::create new array buffer of size (LENGTH)', length='1'),
                                                    type='Uint8',
                                                ),
                                                type='Buffer Pointer (AndrewGaming587)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.ddeDateFormat.current_date(OPCODE='&ddeDateFormat::current date'),
                                                type='Date (Old Version) (ddededodediamante)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.ddeDateFormatV2.current_date(OPCODE='&ddeDateFormatV2::current date'),
                                                type='Date (ddededodediamante)',
                                            ),
                                        ),
                                        h.jwProto.label_command(OPCODE='&jwProto::// (LABEL) {{id=jwProto_labelCommand}}', label="You can't access a div effect type from any reporter"),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.divIterator.iter_builder(OPCODE='&divIterator::iterator builder with {:S:} = (STATE) {SUBSTACK}', state='', substack=[]),
                                                type='Iterator (Div)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.dogeiscutObject.blank(OPCODE='&dogeiscutObject::blank object'),
                                                type='Object (DogeisCut)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.dogeiscutRegularExpressions.regex(OPCODE='&dogeiscutRegularExpressions::regular expression (PATTERN) (FLAGS)', pattern='(.*)', flags='gm'),
                                                type='Regular Expression (DogeisCut)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.dogeiscutSet.blank(OPCODE='&dogeiscutSet::blank set'),
                                                type='Set (DogeisCut)',
                                            ),
                                        ),
                                        h.jwProto.label_command(OPCODE='&jwProto::// (LABEL) {{id=jwProto_labelCommand}}', label="You can't access a timer type from any reporter"),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.jwArray.blank(OPCODE='&jwArray::blank array'),
                                                type='Array (jwklong)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.jwColor.new_color(OPCODE='&jwColor::new color (COLOR)', color='#ff0000'),
                                                type='Color (jwklong)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.jwDate.now(OPCODE='&jwDate::now'),
                                                type='Date (jwklong)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.jwLambda.new_lambda(OPCODE='&jwLambda::new lambda {:ARG:} {SUBSTACK}', substack=[]),
                                                type='Lambda (jwklong)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.jwNum.add(OPCODE='&jwNum::(A) + (B)', a='1', b='2'),
                                                type='Number (jwklong)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.jwTargets.this(OPCODE='&jwTargets::this target'),
                                                type='Target (jwklong)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.jwVector.new_vector(OPCODE='&jwVector::new vector x: (X) y: (Y)', x='1', y='2'),
                                                type='Vector (jwklong)',
                                            ),
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.jwXML.new_node(OPCODE='&jwXML::new node (NAME)', name='test'),
                                                type='XML (jwklong)',
                                            ),
                                        ),
                                        h.jwProto.label_function(
                                            OPCODE='&jwProto::// (LABEL) {SUBSTACK}',
                                            label="For this to work please create a canvas variable e.g. 'myCanvasVar', then enable the condition",
                                            substack=[
                                                h.control.if_(
                                                    OPCODE='&control::if <CONDITION> then {THEN}',
                                                    condition=False,
                                                    then=[
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceFuncsScopes.typeof_value_is_menu(OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?', value='<put the canvas variable block here>', type='Canvas (RedMan13)'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.assert_(
                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                value=h.fruitsPaintUtils.get_colour(OPCODE='&fruitsPaintUtils::get colour from colour name (COLOUR_NAME)', colour_name='orange'),
                                                type='Paint Utils Colour (Fruits555000)',
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                            name='Cast',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='toArray',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='my var', value='hello'),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='var list',
                                                    value=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='all scopes'),
                                                ),
                                                h.gceTestRunner.assert_type(
                                                    OPCODE='&gceTestRunner::assert type of (VALUE) is ([EXPECTED])',
                                                    value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='var list'),
                                                    expected='Array (jwklong)',
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='var list'),
                                                    b='["my var"]',
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='toObject',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='MyClass', substack=[]),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='instance var',
                                                    value=h.gceOOP.create_instance(
                                                        OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)',
                                                        class_=h.gceOOP.create_class_named(OPCODE='&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}', name='MyClass', substack=[]),
                                                        posargs='[]',
                                                    ),
                                                ),
                                                h.gceOOP.set_attribute(
                                                    OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                    instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='instance var'),
                                                    name='my attribute',
                                                    value='hello',
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='attributes',
                                                    value=h.gceOOP.get_all_attributes(
                                                        OPCODE='&gceOOP::all attributes of (INSTANCE)',
                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='instance var'),
                                                    ),
                                                ),
                                                h.gceTestRunner.assert_type(
                                                    OPCODE='&gceTestRunner::assert type of (VALUE) is ([EXPECTED])',
                                                    value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='attributes'),
                                                    expected='Object (DogeisCut)',
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='attributes'),
                                                    b='{"my attribute":"hello"}',
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='toClass && toClassInstance && toFunction',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='MyClass', substack=[]),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceOOP.get_superclass(
                                                        OPCODE='&gceOOP::get superclass of (CLASS)',
                                                        class_=h.gceOOP.create_subclass_named(
                                                            OPCODE='&gceOOP::create subclass named (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                            name='Sub',
                                                            superclass='MyClass',
                                                            substack=[],
                                                        ),
                                                    ),
                                                    b="<Class 'MyClass'>",
                                                ),
                                                h.gceTestRunner.assert_throws_contains(
                                                    OPCODE='&gceTestRunner::assert throws error containing (MSG) {SUBSTACK}',
                                                    msg='but got no input value',
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                            expr=h.gceOOP.get_superclass(
                                                                OPCODE='&gceOOP::get superclass of (CLASS)',
                                                                class_=h.SPjavascriptV2.js_reporter(OPCODE='&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsReporter}}', code='return undefined'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_throws_contains(
                                                    OPCODE='&gceTestRunner::assert throws error containing (MSG) {SUBSTACK}',
                                                    msg='but got no input value',
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                            expr=h.gceOOP.get_superclass(
                                                                OPCODE='&gceOOP::get superclass of (CLASS)',
                                                                class_=h.SPjavascriptV2.js_reporter(OPCODE='&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsReporter}}', code='return null'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceOOP.get_superclass(OPCODE='&gceOOP::get superclass of (CLASS)', class_='MyClass'),
                                                    b="<Class 'Superclass'>",
                                                ),
                                                h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='513', substack=[]),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceOOP.get_superclass(OPCODE='&gceOOP::get superclass of (CLASS)', class_='513'),
                                                    b="<Class 'Superclass'>",
                                                ),
                                                h.gceTestRunner.assert_throws_contains(
                                                    OPCODE='&gceTestRunner::assert throws error containing (MSG) {SUBSTACK}',
                                                    msg='but got no input value',
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                            expr=h.gceOOP.get_superclass(
                                                                OPCODE='&gceOOP::get superclass of (CLASS)',
                                                                class_=h.SPjavascriptV2.js_reporter(OPCODE='&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsReporter}}', code='return null'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_throws(
                                                    OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_subclass_at(
                                                            OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                            name='Sub2',
                                                            superclass=h.gceFuncsScopes.create_function_named(OPCODE='&gceFuncsScopes::create function named (NAME) {SUBSTACK}', name='myFunction', substack=[]),
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
                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                            name='Scoped Variables Blocks',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='set/get/exists',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Set and read a local variable',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='myVar', kind='all scopes'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='myVar', kind='local scope'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='myVar', kind='global scope'),
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='myVar', value='hello'),
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='myVar'),
                                                            b='hello',
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='myVar', kind='all scopes'),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='myVar', kind='local scope'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='myVar', kind='global scope'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='delete var',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Delete removes the variable from the current scope',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='tmp', value='to-delete'),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='tmp', kind='all scopes'),
                                                        ),
                                                        h.gceFuncsScopes.delete_scope_var(OPCODE='&gceFuncsScopes::delete var (NAME) in current scope', name='tmp'),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='tmp', kind='all scopes'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='tmp', kind='local scope'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='tmp', kind='global scope'),
                                                        ),
                                                        h.gceTestRunner.assert_throws(
                                                            OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                    expr=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='tmp'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='all variables + local scope',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='List variables by kind and verify nested local scope behavior',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='a', value='1'),
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='b', value='2'),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='all scopes'),
                                                            b='["a","b"]',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='local scope'),
                                                            b='["a","b"]',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='global scope'),
                                                            b='[]',
                                                        ),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                            substack=[
                                                                h.gceTestRunner.test_scope(
                                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                                    name='In a fresh local scope, inherited names are visible in all scopes',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_unstrict_equal(
                                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                            a=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='all scopes'),
                                                                            b='["a","b"]',
                                                                        ),
                                                                        h.gceTestRunner.assert_unstrict_equal(
                                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                            a=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='local scope'),
                                                                            b='[]',
                                                                        ),
                                                                        h.gceTestRunner.assert_unstrict_equal(
                                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                            a=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='global scope'),
                                                                            b='[]',
                                                                        ),
                                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='c', value='3'),
                                                                        h.gceTestRunner.assert_unstrict_equal(
                                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                            a=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='all scopes'),
                                                                            b='["a","b","c"]',
                                                                        ),
                                                                        h.gceTestRunner.assert_unstrict_equal(
                                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                            a=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='local scope'),
                                                                            b='["c"]',
                                                                        ),
                                                                        h.gceTestRunner.assert_unstrict_equal(
                                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                            a=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='global scope'),
                                                                            b='[]',
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='c', kind='local scope'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='c', kind='all scopes'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='allVariables with globals and locals simultaneously',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='kind_global and kind_local see only their own tier; kind_all sees both',
                                            substack=[
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='globalX', value='gx'),
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='globalY', value='gy'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='localZ', value='lz'),
                                                                h.gceTestRunner.test_scope(
                                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                                    name='kind_global sees globals only',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_text_in_value(
                                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                                            text='globalX',
                                                                            value=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='global scope'),
                                                                        ),
                                                                        h.gceTestRunner.assert_text_in_value(
                                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                                            text='globalY',
                                                                            value=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='global scope'),
                                                                        ),
                                                                        h.gceTestRunner.assert_text_not_in_value(
                                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                                            text='localZ',
                                                                            value=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='global scope'),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceTestRunner.test_scope(
                                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                                    name='kind_local sees locals only',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_text_in_value(
                                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                                            text='localZ',
                                                                            value=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='local scope'),
                                                                        ),
                                                                        h.gceTestRunner.assert_text_not_in_value(
                                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                                            text='globalX',
                                                                            value=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='local scope'),
                                                                        ),
                                                                        h.gceTestRunner.assert_text_not_in_value(
                                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                                            text='globalY',
                                                                            value=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='local scope'),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceTestRunner.test_scope(
                                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                                    name='kind_all sees both globals and locals',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_text_in_value(
                                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                                            text='globalX',
                                                                            value=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='all scopes'),
                                                                        ),
                                                                        h.gceTestRunner.assert_text_in_value(
                                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                                            text='globalY',
                                                                            value=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='all scopes'),
                                                                        ),
                                                                        h.gceTestRunner.assert_text_in_value(
                                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                                            text='localZ',
                                                                            value=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='all scopes'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='bind global + non-local',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Bind global in an inner scope and mutate it',
                                            substack=[
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='globalCounter', value='0'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.bind_var_to_scope(OPCODE='&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope', kind='global', name='globalCounter'),
                                                                h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='globalCounter', value='1'),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='globalCounter'),
                                                            b='1',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Bind non-local variable in nested local scopes and mutate it',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='outerLocal', value='A'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.bind_var_to_scope(OPCODE='&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope', kind='non-local', name='outerLocal'),
                                                                h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='outerLocal', value='B'),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='outerLocal'),
                                                            b='B',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='shadowing: inner scope shadows outer name',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='get_scope_var resolves to innermost definition',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='x', value='outer'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='x', value='inner'),
                                                                h.gceTestRunner.test_scope(
                                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                                    name='Inner scope sees the inner value',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_strict_equal(
                                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                            a=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='x'),
                                                                            b='inner',
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='After inner scope exits, outer value is restored',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='x'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='bind then delete',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Delete a bound global variable from an inner scope',
                                            substack=[
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='toDelete', value='exists'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.bind_var_to_scope(OPCODE='&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope', kind='global', name='toDelete'),
                                                                h.gceFuncsScopes.delete_scope_var(OPCODE='&gceFuncsScopes::delete var (NAME) in current scope', name='toDelete'),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Variable is gone from globals after delete',
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                    condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='toDelete', kind='global scope'),
                                                                ),
                                                                h.gceTestRunner.assert_not(
                                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                    condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='toDelete', kind='all scopes'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Delete a bound non-local variable from an inner scope',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='outerVar', value='exists'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.bind_var_to_scope(OPCODE='&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope', kind='non-local', name='outerVar'),
                                                                h.gceFuncsScopes.delete_scope_var(OPCODE='&gceFuncsScopes::delete var (NAME) in current scope', name='outerVar'),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Variable is gone from outer scope after delete',
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                    condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='outerVar', kind='all scopes'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='bind error paths',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Binding a missing global/non-local variable should throw',
                                            substack=[
                                                h.gceTestRunner.assert_throws(
                                                    OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.bind_var_to_scope(OPCODE='&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope', kind='global', name='missingGlobal'),
                                                    ],
                                                ),
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.bind_var_to_scope(OPCODE='&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope', kind='non-local', name='missingNonLocal'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='createVarScope cleanup on error',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='exitUserScope must run even if an error is thrown inside the scope',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='outerVar', value='present'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='innerVar', value='value'),
                                                                h.gceTestRunner.assert_throws(
                                                                    OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                                    substack=[
                                                                        h.gceFuncsScopes.execute_expression(
                                                                            OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                            expr=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='__missing_var__'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Inner variable should be gone after error',
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                    condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='innerVar', kind='all scopes'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Outer variable should still exist',
                                                            substack=[
                                                                h.gceTestRunner.assert_(
                                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                                    condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='outerVar', kind='all scopes'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='scopeVarExists with 3-level nesting',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Verify kindLocal, kindAll, kindGlobal across 3 scopes',
                                            substack=[
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='globalVar', value='g'),
                                                        h.gceFuncsScopes.create_var_scope(
                                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='level1', value='L1'),
                                                                h.gceFuncsScopes.create_var_scope(
                                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                                    substack=[
                                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='level2', value='L2'),
                                                                        h.gceFuncsScopes.create_var_scope(
                                                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                                            substack=[
                                                                                h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='level3', value='L3'),
                                                                                h.gceTestRunner.test_scope(
                                                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                                                    name='Innermost: level3 is local, others are not',
                                                                                    substack=[
                                                                                        h.gceTestRunner.assert_(
                                                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='level3', kind='local scope'),
                                                                                        ),
                                                                                        h.gceTestRunner.assert_not(
                                                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='level1', kind='local scope'),
                                                                                        ),
                                                                                        h.gceTestRunner.assert_not(
                                                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='level2', kind='local scope'),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                h.gceTestRunner.test_scope(
                                                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                                                    name='All three are visible via kindAll',
                                                                                    substack=[
                                                                                        h.gceTestRunner.assert_(
                                                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='level1', kind='all scopes'),
                                                                                        ),
                                                                                        h.gceTestRunner.assert_(
                                                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='level2', kind='all scopes'),
                                                                                        ),
                                                                                        h.gceTestRunner.assert_(
                                                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='level3', kind='all scopes'),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                h.gceTestRunner.test_scope(
                                                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                                                    name='Global is visible via kindGlobal and kindAll',
                                                                                    substack=[
                                                                                        h.gceTestRunner.assert_(
                                                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='globalVar', kind='global scope'),
                                                                                        ),
                                                                                        h.gceTestRunner.assert_(
                                                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='globalVar', kind='all scopes'),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                h.gceTestRunner.test_scope(
                                                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                                                    name='Local vars are NOT global',
                                                                                    substack=[
                                                                                        h.gceTestRunner.assert_not(
                                                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='level3', kind='global scope'),
                                                                                        ),
                                                                                        h.gceTestRunner.assert_not(
                                                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='level2', kind='global scope'),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceTestRunner.test_scope(
                                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                                    name='level2 and level3 gone after exiting their scopes',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_not(
                                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='level2', kind='all scopes'),
                                                                        ),
                                                                        h.gceTestRunner.assert_not(
                                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='level3', kind='all scopes'),
                                                                        ),
                                                                        h.gceTestRunner.assert_(
                                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='level1', kind='local scope'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='runWithSeparateGlobals',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Outer locals are not visible inside',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='outerLocal', value='outer'),
                                                        h.gceFuncsScopes.run_with_separate_globals(
                                                            OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                    condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='outerLocal', kind='all scopes'),
                                                                ),
                                                                h.gceTestRunner.assert_not(
                                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                    condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='outerLocal', kind='local scope'),
                                                                ),
                                                                h.gceTestRunner.assert_not(
                                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                    condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='outerLocal', kind='global scope'),
                                                                ),
                                                                h.gceTestRunner.assert_throws(
                                                                    OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                                    substack=[
                                                                        h.gceFuncsScopes.execute_expression(
                                                                            OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                            expr=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='outerLocal'),
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
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Outer globals are not visible inside',
                                            substack=[
                                                h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='outerGlobal', value='outerGlobalValue'),
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='outerGlobal', kind='all scopes'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='outerGlobal', kind='global scope'),
                                                        ),
                                                        h.gceTestRunner.assert_throws(
                                                            OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                    expr=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='outerGlobal'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceFuncsScopes.delete_scope_var(OPCODE='&gceFuncsScopes::delete var (NAME) in current scope', name='outerGlobal'),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Writes inside do not affect outer locals',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='sharedName', value='before'),
                                                        h.gceFuncsScopes.run_with_separate_globals(
                                                            OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='sharedName', value='inside'),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='sharedName'),
                                                                    b='inside',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='sharedName'),
                                                            b='before',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Writes inside do not affect outer globals',
                                            substack=[
                                                h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='sharedGlobal', value='globalBefore'),
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='sharedGlobal', value='globalInside'),
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='sharedGlobal'),
                                                            b='globalInside',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_strict_equal(
                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                    a=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='sharedGlobal'),
                                                    b='globalBefore',
                                                ),
                                                h.gceFuncsScopes.delete_scope_var(OPCODE='&gceFuncsScopes::delete var (NAME) in current scope', name='sharedGlobal'),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Inner globals and locals start empty',
                                            substack=[
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='all scopes'),
                                                            b='[]',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='global scope'),
                                                            b='[]',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceFuncsScopes.all_variables(OPCODE='&gceFuncsScopes::all variables in ([KIND])', kind='local scope'),
                                                            b='[]',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Variables created inside are gone after block exits',
                                            substack=[
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='innerOnly', value='value'),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_not(
                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                    condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='innerOnly', kind='all scopes'),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Cleanup happens even if an error is thrown inside',
                                            substack=[
                                                h.gceTestRunner.assert_throws(
                                                    OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.run_with_separate_globals(
                                                            OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='innerError', value='value'),
                                                                h.gceFuncsScopes.execute_expression(
                                                                    OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                    expr=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='__missing__'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_not(
                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                    condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='innerError', kind='all scopes'),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Nested runWithSeparateGlobals are fully independent',
                                            substack=[
                                                h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='outerG', value='OG'),
                                                h.gceFuncsScopes.run_with_separate_globals(
                                                    OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope', name='middleG', value='MG'),
                                                        h.gceFuncsScopes.run_with_separate_globals(
                                                            OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                    condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='outerG', kind='all scopes'),
                                                                ),
                                                                h.gceTestRunner.assert_not(
                                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                    condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='middleG', kind='all scopes'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='middleG', kind='global scope'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='outerG', kind='all scopes'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_(
                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                    condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='outerG', kind='global scope'),
                                                ),
                                                h.gceTestRunner.assert_not(
                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                    condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='middleG', kind='all scopes'),
                                                ),
                                                h.gceFuncsScopes.delete_scope_var(OPCODE='&gceFuncsScopes::delete var (NAME) in current scope', name='outerG'),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                            name='Function Blocks',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='basic function',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Define a simple function that returns a constant',
                                                    substack=[
                                                        h.gceFuncsScopes.create_function_at(
                                                            OPCODE='&gceFuncsScopes::create function at var (NAME) {SUBSTACK}',
                                                            name='myFunc',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='hello'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Call the function with no arguments',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='myFunc', posargs='[]'),
                                                            b='hello',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='function with args',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Configure and define function with two arguments',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["greeting", "name"]', argdefaults='[]'),
                                                        h.gceFuncsScopes.create_function_at(
                                                            OPCODE='&gceFuncsScopes::create function at var (NAME) {SUBSTACK}',
                                                            name='greet',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                    value=h.operator.join3(
                                                                        OPCODE='&operators::join (STRING1) (STRING2) (STRING3)',
                                                                        string1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='greeting'),
                                                                        string2=' ',
                                                                        string3=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='name'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Call with two arguments passed as array',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='greet', posargs='["Hello", "Ada"]'),
                                                            b='Hello Ada',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='default arguments',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Configure function with required arg and default trailing arg',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["person", "greeting"]', argdefaults='["Hi"]'),
                                                        h.gceFuncsScopes.create_function_at(
                                                            OPCODE='&gceFuncsScopes::create function at var (NAME) {SUBSTACK}',
                                                            name='sayHi',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                    value=h.operator.join3(
                                                                        OPCODE='&operators::join (STRING1) (STRING2) (STRING3)',
                                                                        string1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='greeting'),
                                                                        string2=' ',
                                                                        string3=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='person'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Call with only first arg (second uses default Hi)',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='sayHi', posargs='["Bob"]'),
                                                            b='Hi Bob',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Call with both args (overrides default)',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='sayHi', posargs='["Bob", "Hey"]'),
                                                            b='Hey Bob',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='return behavior',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Function returns early inside an if-block; later return must not run',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["flag"]', argdefaults='[]'),
                                                        h.gceFuncsScopes.create_function_at(
                                                            OPCODE='&gceFuncsScopes::create function at var (NAME) {SUBSTACK}',
                                                            name='conditional',
                                                            substack=[
                                                                h.control.if_(
                                                                    OPCODE='&control::if <CONDITION> then {THEN}',
                                                                    condition=h.operator.equals(
                                                                        OPCODE='&operators::(OPERAND1) = (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='flag'),
                                                                        operand2='yes',
                                                                    ),
                                                                    then=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='early'),
                                                                    ],
                                                                ),
                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='late'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='When condition is true, early return fires',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='conditional', posargs='["yes"]'),
                                                            b='early',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='When condition is false, falls through to second return',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='conditional', posargs='["no"]'),
                                                            b='late',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='closures',
                                    substack=[
                                        h.gceFuncsScopes.run_with_separate_globals(
                                            OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Outer function accepts prefix, returns inner function that closes over it',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["prefix"]', argdefaults='[]'),
                                                        h.gceFuncsScopes.create_function_at(
                                                            OPCODE='&gceFuncsScopes::create function at var (NAME) {SUBSTACK}',
                                                            name='makeGreeter',
                                                            substack=[
                                                                h.gceTestRunner.test_scope(
                                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                                    name='Configure inner function arg before defining it',
                                                                    substack=[
                                                                        h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["name"]', argdefaults='[]'),
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.gceFuncsScopes.create_function_named(
                                                                                OPCODE='&gceFuncsScopes::create function named (NAME) {SUBSTACK}',
                                                                                name='greeter',
                                                                                substack=[
                                                                                    h.gceFuncsScopes.return_value(
                                                                                        OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                                        value=h.operator.join3(
                                                                                            OPCODE='&operators::join (STRING1) (STRING2) (STRING3)',
                                                                                            string1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='prefix'),
                                                                                            string2=', ',
                                                                                            string3=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='name'),
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
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Each call to makeGreeter produces an independent greeter',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='hiGreeter',
                                                            value=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='makeGreeter', posargs='["Hi"]'),
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='heyGreeter',
                                                            value=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='makeGreeter', posargs='["Hey"]'),
                                                        ),
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='hiGreeter', posargs='["Ada"]'),
                                                            b='Hi, Ada',
                                                        ),
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='heyGreeter', posargs='["Ada"]'),
                                                            b='Hey, Ada',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Captured prefix is independent per closure instance',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='hiGreeter', posargs='["Bob"]'),
                                                            b='Hi, Bob',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='create function named',
                                    substack=[
                                        h.gceFuncsScopes.run_with_separate_globals(
                                            OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Create a function as a reporter block (returns the function)',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='myFunc',
                                                            value=h.gceFuncsScopes.create_function_named(
                                                                OPCODE='&gceFuncsScopes::create function named (NAME) {SUBSTACK}',
                                                                name='anonFunc',
                                                                substack=[
                                                                    h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='from-anon'),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Call the stored function',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='myFunc', posargs='[]'),
                                                            b='from-anon',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='error: wrong arg count',
                                    substack=[
                                        h.gceFuncsScopes.run_with_separate_globals(
                                            OPCODE='&gceFuncsScopes::run with separate globals {SUBSTACK}',
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Function that accepts no arguments',
                                                    substack=[
                                                        h.gceFuncsScopes.create_function_at(
                                                            OPCODE='&gceFuncsScopes::create function at var (NAME) {SUBSTACK}',
                                                            name='noArgs',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='done'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Calling with extra arguments should throw',
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                    expr=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='noArgs', posargs='["extra"]'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Function that requires one argument',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["required"]', argdefaults='[]'),
                                                        h.gceFuncsScopes.create_function_at(
                                                            OPCODE='&gceFuncsScopes::create function at var (NAME) {SUBSTACK}',
                                                            name='oneArg',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                    value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='required'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Calling with no arguments should throw',
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                    expr=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='oneArg', posargs='[]'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='var scope inside function body',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='createVarScope inside a function is isolated per call',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["val"]', argdefaults='[]'),
                                                        h.gceFuncsScopes.create_function_at(
                                                            OPCODE='&gceFuncsScopes::create function at var (NAME) {SUBSTACK}',
                                                            name='withScope',
                                                            substack=[
                                                                h.gceFuncsScopes.create_var_scope(
                                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                                    substack=[
                                                                        h.gceFuncsScopes.set_scope_var(
                                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                                            name='inner',
                                                                            value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='val'),
                                                                        ),
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='inner'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='First call',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='withScope', posargs='["first"]'),
                                                            b='first',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Second call: inner var is fresh each call',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='withScope', posargs='["second"]'),
                                                            b='second',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Inner scope var is not visible outside the function',
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.scope_var_exists(OPCODE='&gceFuncsScopes::var (NAME) exists in [KIND]?', name='inner', kind='all scopes'),
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
                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                            name='Utilities Blocks',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='nothing',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Nothing is its own type',
                                            substack=[
                                                h.gceTestRunner.assert_(
                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                        OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                        value=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                        type='Nothing (GCE)',
                                                    ),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Nothing equals itself via string comparison',
                                            substack=[
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                    b=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Nothing is identical to itself (same singleton)',
                                            substack=[
                                                h.gceTestRunner.assert_(
                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                    condition=h.gceFuncsScopes.check_identity(
                                                        OPCODE='&gceFuncsScopes::(VALUE1) is (VALUE2) ?',
                                                        value1=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                        value2=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Nothing is not identical to any other value',
                                            substack=[
                                                h.gceTestRunner.assert_not(
                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                    condition=h.gceFuncsScopes.check_identity(
                                                        OPCODE='&gceFuncsScopes::(VALUE1) is (VALUE2) ?',
                                                        value1=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                        value2='0',
                                                    ),
                                                ),
                                                h.gceTestRunner.assert_not(
                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                    condition=h.gceFuncsScopes.check_identity(
                                                        OPCODE='&gceFuncsScopes::(VALUE1) is (VALUE2) ?',
                                                        value1=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                        value2='',
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='typeofValue',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Primitive types',
                                            substack=[
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceFuncsScopes.typeof_value(OPCODE='&gceFuncsScopes::typeof (VALUE)', value='hello'),
                                                    b=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='String'),
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceFuncsScopes.typeof_value(OPCODE='&gceFuncsScopes::typeof (VALUE)', value='42'),
                                                    b=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='Number'),
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceFuncsScopes.typeof_value(
                                                        OPCODE='&gceFuncsScopes::typeof (VALUE)',
                                                        value=h.operator.true_boolean(OPCODE='&operators::true'),
                                                    ),
                                                    b=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='Boolean'),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='GCE types',
                                            substack=[
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceFuncsScopes.typeof_value(
                                                        OPCODE='&gceFuncsScopes::typeof (VALUE)',
                                                        value=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                    ),
                                                    b=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='Nothing (GCE)'),
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceFuncsScopes.typeof_value(
                                                        OPCODE='&gceFuncsScopes::typeof (VALUE)',
                                                        value=h.gceFuncsScopes.create_function_named(
                                                            OPCODE='&gceFuncsScopes::create function named (NAME) {SUBSTACK}',
                                                            name='f',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='x'),
                                                            ],
                                                        ),
                                                    ),
                                                    b=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='Function (GCE)'),
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceFuncsScopes.typeof_value(
                                                        OPCODE='&gceFuncsScopes::typeof (VALUE)',
                                                        value=h.gceOOP.create_class_named(OPCODE='&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}', name='MyClass', substack=[]),
                                                    ),
                                                    b=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='Class (GCE)'),
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceFuncsScopes.typeof_value(
                                                        OPCODE='&gceFuncsScopes::typeof (VALUE)',
                                                        value=h.gceOOP.create_instance(
                                                            OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)',
                                                            class_=h.gceOOP.create_class_named(OPCODE='&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}', name='MyClass', substack=[]),
                                                            posargs='[]',
                                                        ),
                                                    ),
                                                    b=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='Class Instance (GCE)'),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='typeofValueIsMenu',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Correct type returns true',
                                            substack=[
                                                h.gceTestRunner.assert_(
                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?', value='hello', type='String'),
                                                ),
                                                h.gceTestRunner.assert_(
                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?', value='42', type='Number'),
                                                ),
                                                h.gceTestRunner.assert_(
                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                        OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                        value=h.operator.true_boolean(OPCODE='&operators::true'),
                                                        type='Boolean',
                                                    ),
                                                ),
                                                h.gceTestRunner.assert_(
                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                        OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                        value=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                        type='Nothing (GCE)',
                                                    ),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Wrong type returns false',
                                            substack=[
                                                h.gceTestRunner.assert_not(
                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?', value='hello', type='Number'),
                                                ),
                                                h.gceTestRunner.assert_not(
                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?', value='42', type='String'),
                                                ),
                                                h.gceTestRunner.assert_not(
                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                        OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                        value=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                        type='String',
                                                    ),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='typeofValueIsMenu is consistent with typeofValue',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='fn',
                                                            value=h.gceFuncsScopes.create_function_named(
                                                                OPCODE='&gceFuncsScopes::create function named (NAME) {SUBSTACK}',
                                                                name='g',
                                                                substack=[
                                                                    h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='y'),
                                                                ],
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                                value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='fn'),
                                                                type='Function (GCE)',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                                value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='fn'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='typeofValueSelection',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='The reporter returns the menu value as a string',
                                            substack=[
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='String'),
                                                    b='String',
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='Nothing (GCE)'),
                                                    b='Nothing (GCE)',
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='Function (GCE)'),
                                                    b='Function (GCE)',
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Result matches typeofValue output',
                                            substack=[
                                                h.gceTestRunner.assert_(
                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                    condition=h.operator.equals(
                                                        OPCODE='&operators::(OPERAND1) = (OPERAND2)',
                                                        operand1=h.gceFuncsScopes.typeof_value(
                                                            OPCODE='&gceFuncsScopes::typeof (VALUE)',
                                                            value=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                        ),
                                                        operand2=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='Nothing (GCE)'),
                                                    ),
                                                ),
                                                h.gceTestRunner.assert_(
                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                    condition=h.operator.equals(
                                                        OPCODE='&operators::(OPERAND1) = (OPERAND2)',
                                                        operand1=h.gceFuncsScopes.typeof_value(OPCODE='&gceFuncsScopes::typeof (VALUE)', value='test'),
                                                        operand2=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='String'),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='objectAsString',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Primitive values stringify as-is',
                                            substack=[
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceFuncsScopes.object_as_string(OPCODE='&gceFuncsScopes::(VALUE) as string', value='hello'),
                                                    b='hello',
                                                ),
                                                h.gceTestRunner.assert_unstrict_equal(
                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                    a=h.gceFuncsScopes.object_as_string(OPCODE='&gceFuncsScopes::(VALUE) as string', value='42'),
                                                    b='42',
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Nothing stringifies to its representation',
                                            substack=[
                                                h.gceTestRunner.assert_does_not_throw(
                                                    OPCODE='&gceTestRunner::assert does not throw error {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                            expr=h.gceFuncsScopes.object_as_string(
                                                                OPCODE='&gceFuncsScopes::(VALUE) as string',
                                                                value=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Instance without as-string method: no error, returns some string',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Plain', substack=[]),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='inst',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Plain', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.assert_does_not_throw(
                                                            OPCODE='&gceTestRunner::assert does not throw error {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                    expr=h.gceFuncsScopes.object_as_string(
                                                                        OPCODE='&gceFuncsScopes::(VALUE) as string',
                                                                        value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='inst'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                                value=h.gceFuncsScopes.object_as_string(
                                                                    OPCODE='&gceFuncsScopes::(VALUE) as string',
                                                                    value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='inst'),
                                                                ),
                                                                type='String',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Instance WITH as-string method: calls the method',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='Stringable',
                                                            substack=[
                                                                h.gceOOP.define_special_method(
                                                                    OPCODE='&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}',
                                                                    special_method='as string',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='custom-string'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='inst',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Stringable', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceFuncsScopes.object_as_string(
                                                                OPCODE='&gceFuncsScopes::(VALUE) as string',
                                                                value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='inst'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='checkIdentity',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Two separate instances of the same class are NOT identical',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='MyClass', substack=[]),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='a',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='MyClass', posargs='[]'),
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='b',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='MyClass', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.check_identity(
                                                                OPCODE='&gceFuncsScopes::(VALUE1) is (VALUE2) ?',
                                                                value1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                value2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='The same instance stored in two variables IS identical',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='MyClass', substack=[]),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='a',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='MyClass', posargs='[]'),
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='b',
                                                            value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceFuncsScopes.check_identity(
                                                                OPCODE='&gceFuncsScopes::(VALUE1) is (VALUE2) ?',
                                                                value1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                value2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Nothing is identical to itself',
                                            substack=[
                                                h.gceTestRunner.assert_(
                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                    condition=h.gceFuncsScopes.check_identity(
                                                        OPCODE='&gceFuncsScopes::(VALUE1) is (VALUE2) ?',
                                                        value1=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                        value2=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Nothing is not identical to a function',
                                            substack=[
                                                h.gceTestRunner.assert_not(
                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                    condition=h.gceFuncsScopes.check_identity(
                                                        OPCODE='&gceFuncsScopes::(VALUE1) is (VALUE2) ?',
                                                        value1=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                        value2=h.gceFuncsScopes.create_function_named(
                                                            OPCODE='&gceFuncsScopes::create function named (NAME) {SUBSTACK}',
                                                            name='h',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='z'),
                                                            ],
                                                        ),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Two separately created functions are NOT identical',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='f1',
                                                            value=h.gceFuncsScopes.create_function_named(
                                                                OPCODE='&gceFuncsScopes::create function named (NAME) {SUBSTACK}',
                                                                name='fn1',
                                                                substack=[
                                                                    h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='r'),
                                                                ],
                                                            ),
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='f2',
                                                            value=h.gceFuncsScopes.create_function_named(
                                                                OPCODE='&gceFuncsScopes::create function named (NAME) {SUBSTACK}',
                                                                name='fn2',
                                                                substack=[
                                                                    h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='r'),
                                                                ],
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceFuncsScopes.check_identity(
                                                                OPCODE='&gceFuncsScopes::(VALUE1) is (VALUE2) ?',
                                                                value1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='f1'),
                                                                value2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='f2'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Primitive strings identical',
                                            substack=[
                                                h.gceTestRunner.assert_(
                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                    condition=h.gceFuncsScopes.check_identity(OPCODE='&gceFuncsScopes::(VALUE1) is (VALUE2) ?', value1='hello', value2='hello'),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='executeExpression',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Evaluate a reporter block as a command (no error)',
                                            substack=[
                                                h.gceTestRunner.assert_does_not_throw(
                                                    OPCODE='&gceTestRunner::assert does not throw error {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                            expr=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='executeExpression propagates errors from its subexpression',
                                            substack=[
                                                h.gceTestRunner.assert_throws(
                                                    OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                            expr=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='__missing__'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='executeExpression can evaluate any reporter',
                                            substack=[
                                                h.gceTestRunner.assert_does_not_throw(
                                                    OPCODE='&gceTestRunner::assert does not throw error {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                            expr=h.gceFuncsScopes.typeof_value(OPCODE='&gceFuncsScopes::typeof (VALUE)', value='test'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.assert_does_not_throw(
                                                    OPCODE='&gceTestRunner::assert does not throw error {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                            expr=h.gceFuncsScopes.object_as_string(OPCODE='&gceFuncsScopes::(VALUE) as string', value='hello'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='executeExpression can call a function and discard the return value',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.create_function_at(
                                                            OPCODE='&gceFuncsScopes::create function at var (NAME) {SUBSTACK}',
                                                            name='noopFn',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='done'),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_does_not_throw(
                                                            OPCODE='&gceTestRunner::assert does not throw error {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                    expr=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='noopFn', posargs='[]'),
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
                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                            name='Class Definition and Inheritance Blocks',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='createClassAt',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Class is accessible by name and typeof is Class (GCE)',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='MyClass', substack=[]),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceFuncsScopes.typeof_value(
                                                                OPCODE='&gceFuncsScopes::typeof (VALUE)',
                                                                value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='MyClass'),
                                                            ),
                                                            b=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='Class (GCE)'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Can create an instance immediately',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                                    name='inst',
                                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='MyClass', posargs='[]'),
                                                                ),
                                                                h.gceTestRunner.assert_(
                                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                                    condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                                        OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                                        value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='inst'),
                                                                        type='Class Instance (GCE)',
                                                                    ),
                                                                ),
                                                                h.gceTestRunner.assert_(
                                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                                    condition=h.gceOOP.is_instance(
                                                                        OPCODE='&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?',
                                                                        potential_instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='inst'),
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
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Class with methods and init defined inline',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='Counter',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["start"]', argdefaults='["0"]'),
                                                                h.gceOOP.define_special_method(
                                                                    OPCODE='&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}',
                                                                    special_method='init',
                                                                    substack=[
                                                                        h.gceOOP.set_attribute(
                                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                                            instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                            name='count',
                                                                            value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='start'),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_instance_method(
                                                                    OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                                    name='value',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.gceOOP.get_attribute(
                                                                                OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                                name='count',
                                                                                instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='c',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Counter', posargs='["5"]'),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_method(
                                                                OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
                                                                name='value',
                                                                posargs='[]',
                                                            ),
                                                            b='5',
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Default arg: no args uses default 0',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                                    name='d',
                                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Counter', posargs='[]'),
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.call_method(
                                                                        OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='d'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='createClassNamed (reporter)',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Create class inline as a reporter value, store and use it',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='Dyn',
                                                            value=h.gceOOP.create_class_named(
                                                                OPCODE='&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}',
                                                                name='DynClass',
                                                                substack=[
                                                                    h.gceOOP.define_instance_method(
                                                                        OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                                        name='ping',
                                                                        substack=[
                                                                            h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='pong'),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Stored value is a Class (GCE)',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceFuncsScopes.typeof_value(
                                                                        OPCODE='&gceFuncsScopes::typeof (VALUE)',
                                                                        value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='Dyn'),
                                                                    ),
                                                                    b=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='Class (GCE)'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Class can be instantiated',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                                    name='inst',
                                                                    value=h.gceOOP.create_instance(
                                                                        OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)',
                                                                        class_=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='Dyn'),
                                                                        posargs='[]',
                                                                    ),
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.call_method(
                                                                        OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='inst'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='currentClass',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='currentClass inside createClassAt returns the class being defined',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='Stamped',
                                                            substack=[
                                                                h.gceOOP.set_class_variable(
                                                                    OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                                    class_=h.gceOOP.current_class(OPCODE='&gceOOP::current class'),
                                                                    name='tag',
                                                                    value='stamped-value',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Class variable set via currentClass is accessible by name',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_class_variable(OPCODE='&gceOOP::on (CLASS) get class var (NAME)', name='tag', class_='Stamped'),
                                                                    b='stamped-value',
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='currentClass inside createClassNamed also works',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='NC',
                                                            value=h.gceOOP.create_class_named(
                                                                OPCODE='&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}',
                                                                name='NamedCls',
                                                                substack=[
                                                                    h.gceOOP.set_class_variable(
                                                                        OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                                        class_=h.gceOOP.current_class(OPCODE='&gceOOP::current class'),
                                                                        name='info',
                                                                        value='from-named',
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.get_class_variable(
                                                                OPCODE='&gceOOP::on (CLASS) get class var (NAME)',
                                                                name='info',
                                                                class_=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='NC'),
                                                            ),
                                                            b='from-named',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='currentClass inside onClass returns the correct class',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Extendable', substack=[]),
                                                        h.gceOOP.on_class(
                                                            OPCODE='&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}',
                                                            class_='Extendable',
                                                            substack=[
                                                                h.gceOOP.set_class_variable(
                                                                    OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                                    class_=h.gceOOP.current_class(OPCODE='&gceOOP::current class'),
                                                                    name='addedTag',
                                                                    value='via-on-class',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.get_class_variable(OPCODE='&gceOOP::on (CLASS) get class var (NAME)', name='addedTag', class_='Extendable'),
                                                            b='via-on-class',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='createSubclassAt',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                    name='Animal',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='breathe',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='breathing'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceOOP.create_subclass_at(
                                                    OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                    name='Dog',
                                                    superclass='Animal',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='bark',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='woof'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='isSubclass reflects the relationship',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?', subclass='Dog', superclass='Animal'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?', subclass='Animal', superclass='Dog'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='getSuperclass of Dog is Animal',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='Animal',
                                                            value=h.gceOOP.get_superclass(OPCODE='&gceOOP::get superclass of (CLASS)', class_='Dog'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Dog instance can call both inherited and own methods',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='d',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Dog', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_method(
                                                                OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='d'),
                                                                name='breathe',
                                                                posargs='[]',
                                                            ),
                                                            b='breathing',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_method(
                                                                OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='d'),
                                                                name='bark',
                                                                posargs='[]',
                                                            ),
                                                            b='woof',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='currentClass inside subclass body returns the subclass',
                                                    substack=[
                                                        h.gceOOP.create_subclass_at(
                                                            OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                            name='Puppy',
                                                            superclass='Dog',
                                                            substack=[
                                                                h.gceOOP.set_class_variable(
                                                                    OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                                    class_=h.gceOOP.current_class(OPCODE='&gceOOP::current class'),
                                                                    name='size',
                                                                    value='small',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.get_class_variable(OPCODE='&gceOOP::on (CLASS) get class var (NAME)', name='size', class_='Puppy'),
                                                            b='small',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='isSubclass is transitive',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?', subclass='Puppy', superclass='Animal'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='createSubclassNamed (reporter)',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                    name='BaseR',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='base',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='from-base'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='Sub',
                                                    value=h.gceOOP.create_subclass_named(
                                                        OPCODE='&gceOOP::create subclass named (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                        name='SubNamed',
                                                        superclass='BaseR',
                                                        substack=[
                                                            h.gceOOP.define_instance_method(
                                                                OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                                name='child',
                                                                substack=[
                                                                    h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='from-child'),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Stored value is a Class (GCE)',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceFuncsScopes.typeof_value(
                                                                OPCODE='&gceFuncsScopes::typeof (VALUE)',
                                                                value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='Sub'),
                                                            ),
                                                            b=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='Class (GCE)'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='isSubclass works for reporter-created subclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(
                                                                OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?',
                                                                subclass=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='Sub'),
                                                                superclass='BaseR',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Instance inherits from base and has own method',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='inst',
                                                            value=h.gceOOP.create_instance(
                                                                OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)',
                                                                class_=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='Sub'),
                                                                posargs='[]',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_method(
                                                                OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='inst'),
                                                                name='base',
                                                                posargs='[]',
                                                            ),
                                                            b='from-base',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_method(
                                                                OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='inst'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='isSubclass',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='A', substack=[]),
                                                h.gceOOP.create_subclass_at(
                                                    OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                    name='B',
                                                    superclass='A',
                                                    substack=[],
                                                ),
                                                h.gceOOP.create_subclass_at(
                                                    OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                    name='C',
                                                    superclass='B',
                                                    substack=[],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Direct and transitive subclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?', subclass='B', superclass='A'),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?', subclass='C', superclass='A'),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?', subclass='C', superclass='B'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Reverse is false',
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?', subclass='A', superclass='B'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?', subclass='A', superclass='C'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='A class is kinda a subclass of itself',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?', subclass='A', superclass='A'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='getSuperclass',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Root', substack=[]),
                                                h.gceOOP.create_subclass_at(
                                                    OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                    name='Branch',
                                                    superclass='Root',
                                                    substack=[],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Superclass of Branch is Root',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='Root',
                                                            value=h.gceOOP.get_superclass(OPCODE='&gceOOP::get superclass of (CLASS)', class_='Branch'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name="Root's superclass is the built-in Superclass",
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='Superclass',
                                                            value=h.gceOOP.get_superclass(OPCODE='&gceOOP::get superclass of (CLASS)', class_='Root'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Superclass of the built-in Superclass is Nothing',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceFuncsScopes.typeof_value_is_menu(
                                                                OPCODE='&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?',
                                                                value=h.gceOOP.get_superclass(
                                                                    OPCODE='&gceOOP::get superclass of (CLASS)',
                                                                    class_=h.gceOOP.get_superclass(OPCODE='&gceOOP::get superclass of (CLASS)', class_='Root'),
                                                                ),
                                                                type='Nothing (GCE)',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Missing class throws',
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                    expr=h.gceOOP.get_superclass(OPCODE='&gceOOP::get superclass of (CLASS)', class_='__no_such_class__'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='onClass: add instance method',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Define class with no methods, then add one via onClass',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Greeter', substack=[]),
                                                        h.gceOOP.on_class(
                                                            OPCODE='&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}',
                                                            class_='Greeter',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["name"]', argdefaults='[]'),
                                                                h.gceOOP.define_instance_method(
                                                                    OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                                    name='hello',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.join(
                                                                                OPCODE='&operators::join (STRING1) (STRING2)',
                                                                                string1='Hello, ',
                                                                                string2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='name'),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='g',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Greeter', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Method added via onClass is callable',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.call_method(
                                                                        OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='g'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='onClass: add static method',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Util', substack=[]),
                                                h.gceOOP.on_class(
                                                    OPCODE='&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}',
                                                    class_='Util',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["x"]', argdefaults='[]'),
                                                        h.gceOOP.define_static_method(
                                                            OPCODE='&gceOOP::define static method (NAME) {SUBSTACK}',
                                                            name='double',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                    value=h.operator.multiply(
                                                                        OPCODE='&operators::(OPERAND1) * (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='x'),
                                                                        operand2='2',
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Static method added via onClass is callable',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_static_method(
                                                                OPCODE='&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)',
                                                                class_='Util',
                                                                name='double',
                                                                posargs='["7"]',
                                                            ),
                                                            b='14',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='onClass: currentClass inside body',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='currentClass used inside onClass body sets a class variable',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Tagged', substack=[]),
                                                        h.gceOOP.on_class(
                                                            OPCODE='&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}',
                                                            class_='Tagged',
                                                            substack=[
                                                                h.gceOOP.set_class_variable(
                                                                    OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                                    class_=h.gceOOP.current_class(OPCODE='&gceOOP::current class'),
                                                                    name='source',
                                                                    value='on-class',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.get_class_variable(OPCODE='&gceOOP::on (CLASS) get class var (NAME)', name='source', class_='Tagged'),
                                                            b='on-class',
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Multiple onClass calls accumulate class variables',
                                                            substack=[
                                                                h.gceOOP.on_class(
                                                                    OPCODE='&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}',
                                                                    class_='Tagged',
                                                                    substack=[
                                                                        h.gceOOP.set_class_variable(
                                                                            OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                                            class_=h.gceOOP.current_class(OPCODE='&gceOOP::current class'),
                                                                            name='extra',
                                                                            value='second',
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_class_variable(OPCODE='&gceOOP::on (CLASS) get class var (NAME)', name='source', class_='Tagged'),
                                                                    b='on-class',
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_class_variable(OPCODE='&gceOOP::on (CLASS) get class var (NAME)', name='extra', class_='Tagged'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='onClass: visible in propertyNamesOfClass',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Method added via onClass appears in property list',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Widget', substack=[]),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='No methods yet',
                                                            substack=[
                                                                h.gceTestRunner.assert_text_not_in_value(
                                                                    OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                                    text='render',
                                                                    value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='instance method', class_='Widget'),
                                                                ),
                                                                h.gceOOP.on_class(
                                                                    OPCODE='&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}',
                                                                    class_='Widget',
                                                                    substack=[
                                                                        h.gceOOP.define_instance_method(
                                                                            OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                                            name='render',
                                                                            substack=[
                                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='rendered'),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Method now listed after onClass',
                                                            substack=[
                                                                h.gceTestRunner.assert_text_in_value(
                                                                    OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                                    text='render',
                                                                    value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='instance method', class_='Widget'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='onClass: cleanup on error',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='class def scope cleanup runs even when body throws',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Safe', substack=[]),
                                                        h.gceTestRunner.assert_throws(
                                                            OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                            substack=[
                                                                h.gceOOP.on_class(
                                                                    OPCODE='&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}',
                                                                    class_='Safe',
                                                                    substack=[
                                                                        h.gceFuncsScopes.execute_expression(
                                                                            OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                            expr=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='__missing__'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='After the error, onClass on same class still works',
                                                            substack=[
                                                                h.gceTestRunner.assert_does_not_throw(
                                                                    OPCODE='&gceTestRunner::assert does not throw error {SUBSTACK}',
                                                                    substack=[
                                                                        h.gceOOP.on_class(
                                                                            OPCODE='&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}',
                                                                            class_='Safe',
                                                                            substack=[
                                                                                h.gceOOP.define_instance_method(
                                                                                    OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                                                    name='ok',
                                                                                    substack=[
                                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='ok'),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.call_method(
                                                                        OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                        instance=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Safe', posargs='[]'),
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
                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                            name='Instance Methods',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='basic method call',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Define class with methods, call them on an instance',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='Greeter',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["name"]', argdefaults='[]'),
                                                                h.gceOOP.define_instance_method(
                                                                    OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                                    name='greet',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.join3(
                                                                                OPCODE='&operators::join (STRING1) (STRING2) (STRING3)',
                                                                                string1='Hello, ',
                                                                                string2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='name'),
                                                                                string3='!',
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_instance_method(
                                                                    OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                                    name='getType',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.gceFuncsScopes.typeof_value(
                                                                                OPCODE='&gceFuncsScopes::typeof (VALUE)',
                                                                                value=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_instance_method(
                                                                    OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                                    name='getAttr',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.gceOOP.get_attribute(
                                                                                OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                                name='label',
                                                                                instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='g',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Greeter', posargs='[]'),
                                                        ),
                                                        h.gceOOP.set_attribute(
                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                            instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='g'),
                                                            name='label',
                                                            value='test-label',
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Method with arg',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.call_method(
                                                                        OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='g'),
                                                                        name='greet',
                                                                        posargs='["World"]',
                                                                    ),
                                                                    b='Hello, World!',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Same method with different arg',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.call_method(
                                                                        OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='g'),
                                                                        name='greet',
                                                                        posargs='["Alice"]',
                                                                    ),
                                                                    b='Hello, Alice!',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='No-arg method returns correct type string',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.call_method(
                                                                        OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='g'),
                                                                        name='getType',
                                                                        posargs='[]',
                                                                    ),
                                                                    b=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='Class Instance (GCE)'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Method reads self attribute',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.call_method(
                                                                        OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='g'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='self is the correct instance',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Two instances with different attribute values',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='Box',
                                                            substack=[
                                                                h.gceOOP.define_instance_method(
                                                                    OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                                    name='describe',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.join(
                                                                                OPCODE='&operators::join (STRING1) (STRING2)',
                                                                                string1='Box-',
                                                                                string2=h.gceOOP.get_attribute(
                                                                                    OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                                    name='id',
                                                                                    instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='b1',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Box', posargs='[]'),
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='b2',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Box', posargs='[]'),
                                                        ),
                                                        h.gceOOP.set_attribute(
                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                            instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b1'),
                                                            name='id',
                                                            value='AAA',
                                                        ),
                                                        h.gceOOP.set_attribute(
                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                            instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b2'),
                                                            name='id',
                                                            value='BBB',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_method(
                                                                OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b1'),
                                                                name='describe',
                                                                posargs='[]',
                                                            ),
                                                            b='Box-AAA',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_method(
                                                                OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b2'),
                                                                name='describe',
                                                                posargs='[]',
                                                            ),
                                                            b='Box-BBB',
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='self is distinct for each instance',
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                    condition=h.gceFuncsScopes.check_identity(
                                                                        OPCODE='&gceFuncsScopes::(VALUE1) is (VALUE2) ?',
                                                                        value1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b1'),
                                                                        value2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b2'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='error cases',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Calling an undefined method throws',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Empty', substack=[]),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='e',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Empty', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.assert_throws(
                                                            OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                    expr=h.gceOOP.call_method(
                                                                        OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='e'),
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
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Calling a method on a non-instance throws',
                                            substack=[
                                                h.gceTestRunner.assert_throws(
                                                    OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                    substack=[
                                                        h.gceFuncsScopes.execute_expression(
                                                            OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                            expr=h.gceOOP.call_method(
                                                                OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                instance='not-an-instance',
                                                                name='anyMethod',
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='method with yield point',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Method body that includes sayforsecs (yielding block) returns correctly and waits',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='Speaker',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["msg"]', argdefaults='[]'),
                                                                h.gceOOP.define_instance_method(
                                                                    OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                                    name='speak',
                                                                    substack=[
                                                                        h.looks.sayforsecs(
                                                                            OPCODE='&looks::say (MESSAGE) for (SECONDS) seconds',
                                                                            message=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='msg'),
                                                                            seconds='0.5',
                                                                        ),
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.join(
                                                                                OPCODE='&operators::join (STRING1) (STRING2)',
                                                                                string1='said: ',
                                                                                string2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='msg'),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='s',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Speaker', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Return value is correct after yield',
                                                            substack=[
                                                                h.sensing.resettimer(OPCODE='&sensing::reset timer'),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.call_method(
                                                                        OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='s'),
                                                                        name='speak',
                                                                        posargs='["hello"]',
                                                                    ),
                                                                    b='said: hello',
                                                                ),
                                                                h.gceTestRunner.test_scope(
                                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                                    name='At least 0.4s elapsed (sayforsecs 0.5s actually waited)',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_(
                                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                                            condition=h.operator.gt(
                                                                                OPCODE='&operators::(OPERAND1) > (OPERAND2)',
                                                                                operand1=h.sensing.timer(OPCODE='&sensing::timer'),
                                                                                operand2='0.4',
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Second call also returns correctly and also waits',
                                                            substack=[
                                                                h.sensing.resettimer(OPCODE='&sensing::reset timer'),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.call_method(
                                                                        OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='s'),
                                                                        name='speak',
                                                                        posargs='["world"]',
                                                                    ),
                                                                    b='said: world',
                                                                ),
                                                                h.gceTestRunner.test_scope(
                                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                                    name='At least 0.4s elapsed on second call too',
                                                                    substack=[
                                                                        h.gceTestRunner.assert_(
                                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                                            condition=h.operator.gt(
                                                                                OPCODE='&operators::(OPERAND1) > (OPERAND2)',
                                                                                operand1=h.sensing.timer(OPCODE='&sensing::timer'),
                                                                                operand2='0.4',
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
                                    ],
                                ),
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                            name='Special Method: init',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='init sets attributes from args',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Define class whose init sets x and y from positional args',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='Point',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["x","y"]', argdefaults='[]'),
                                                                h.gceOOP.define_special_method(
                                                                    OPCODE='&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}',
                                                                    special_method='init',
                                                                    substack=[
                                                                        h.gceOOP.set_attribute(
                                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                                            instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                            name='x',
                                                                            value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='x'),
                                                                        ),
                                                                        h.gceOOP.set_attribute(
                                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                                            instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                            name='y',
                                                                            value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='y'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='p',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Point', posargs='["3","4"]'),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.get_attribute(
                                                                OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                name='x',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='p'),
                                                            ),
                                                            b='3',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.get_attribute(
                                                                OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                name='y',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='p'),
                                                            ),
                                                            b='4',
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Second instance has independent values',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                                    name='q',
                                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Point', posargs='["10","20"]'),
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='x',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='q'),
                                                                    ),
                                                                    b='10',
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='y',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='q'),
                                                                    ),
                                                                    b='20',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='First instance unchanged after second is created',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='x',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='p'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='init with default args',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Defaults fill in when args omitted',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='Color',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["r","g","b"]', argdefaults='["0","0","0"]'),
                                                                h.gceOOP.define_special_method(
                                                                    OPCODE='&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}',
                                                                    special_method='init',
                                                                    substack=[
                                                                        h.gceOOP.set_attribute(
                                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                                            instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                            name='r',
                                                                            value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='r'),
                                                                        ),
                                                                        h.gceOOP.set_attribute(
                                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                                            instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                            name='g',
                                                                            value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='g'),
                                                                        ),
                                                                        h.gceOOP.set_attribute(
                                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                                            instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                            name='b',
                                                                            value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='All defaults: r=0, g=0, b=0',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                                    name='black',
                                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Color', posargs='[]'),
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='r',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='black'),
                                                                    ),
                                                                    b='0',
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='g',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='black'),
                                                                    ),
                                                                    b='0',
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='b',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='black'),
                                                                    ),
                                                                    b='0',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Partial override: r=255',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                                    name='red',
                                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Color', posargs='["255"]'),
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='r',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='red'),
                                                                    ),
                                                                    b='255',
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='g',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='red'),
                                                                    ),
                                                                    b='0',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Full args',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                                    name='custom',
                                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Color', posargs='["10","20","30"]'),
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='b',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='custom'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='subclass init calls super init',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Subclass init calls callSuperInitMethod',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='Shape',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["color"]', argdefaults='[]'),
                                                                h.gceOOP.define_special_method(
                                                                    OPCODE='&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}',
                                                                    special_method='init',
                                                                    substack=[
                                                                        h.gceOOP.set_attribute(
                                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                                            instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                            name='color',
                                                                            value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='color'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.create_subclass_at(
                                                            OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                            name='Circle',
                                                            superclass='Shape',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["radius","color"]', argdefaults='[]'),
                                                                h.gceOOP.define_special_method(
                                                                    OPCODE='&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}',
                                                                    special_method='init',
                                                                    substack=[
                                                                        h.gceFuncsScopes.execute_expression(
                                                                            OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                            expr=h.gceOOP.call_super_init_method(OPCODE='&gceOOP::call super init method with positional args (POSARGS)', posargs='["blue"]'),
                                                                        ),
                                                                        h.gceOOP.set_attribute(
                                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                                            instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                            name='radius',
                                                                            value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='radius'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='c',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Circle', posargs='["5","ignored"]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='radius set by Circle init',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='radius',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
                                                                    ),
                                                                    b='5',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='color set by super (Shape) init with hardcoded value',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='color',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
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
                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                            name='Inheritance and Super',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='isSubclass',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='A', substack=[]),
                                                h.gceOOP.create_subclass_at(
                                                    OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                    name='B',
                                                    superclass='A',
                                                    substack=[],
                                                ),
                                                h.gceOOP.create_subclass_at(
                                                    OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                    name='C',
                                                    superclass='B',
                                                    substack=[],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Direct subclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?', subclass='B', superclass='A'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Transitive subclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?', subclass='C', superclass='A'),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?', subclass='C', superclass='B'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Reverse is false',
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?', subclass='A', superclass='B'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?', subclass='A', superclass='C'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='A class is a subclass of itself',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_subclass(OPCODE='&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?', subclass='A', superclass='A'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='isInstance with inheritance',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Vehicle', substack=[]),
                                                h.gceOOP.create_subclass_at(
                                                    OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                    name='Car',
                                                    superclass='Vehicle',
                                                    substack=[],
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='v',
                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Vehicle', posargs='[]'),
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='c',
                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Car', posargs='[]'),
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Instance is instance of own class',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_instance(
                                                                OPCODE='&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?',
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='v'),
                                                                class_='Vehicle',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_instance(
                                                                OPCODE='&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?',
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
                                                                class_='Car',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Subclass instance is instance of superclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_instance(
                                                                OPCODE='&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?',
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
                                                                class_='Vehicle',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Superclass instance is NOT instance of subclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceOOP.is_instance(
                                                                OPCODE='&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?',
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='v'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='method override and super',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                    name='Animal',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='speak',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='generic sound'),
                                                            ],
                                                        ),
                                                        h.gceOOP.define_instance_method(
                                                            OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='breathe',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='breathing'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceOOP.create_subclass_at(
                                                    OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                    name='Dog',
                                                    superclass='Animal',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='speak',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                    value=h.operator.join(
                                                                        OPCODE='&operators::join (STRING1) (STRING2)',
                                                                        string1=h.gceOOP.call_super_method(OPCODE='&gceOOP::call super method (NAME) with positional args (POSARGS)', name='speak', posargs='[]'),
                                                                        string2=' (but louder)',
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='a',
                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Animal', posargs='[]'),
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='d',
                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Dog', posargs='[]'),
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Overridden method returns augmented result',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_method(
                                                                OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='d'),
                                                                name='speak',
                                                                posargs='[]',
                                                            ),
                                                            b='generic sound (but louder)',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Parent method still returns original',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_method(
                                                                OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                name='speak',
                                                                posargs='[]',
                                                            ),
                                                            b='generic sound',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Inherited (non-overridden) method works on subclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_method(
                                                                OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='d'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='getSuperclass',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Base', substack=[]),
                                                h.gceOOP.create_subclass_at(
                                                    OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                    name='Child',
                                                    superclass='Base',
                                                    substack=[],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Superclass of Child is Base',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='Base',
                                                            value=h.gceOOP.get_superclass(OPCODE='&gceOOP::get superclass of (CLASS)', class_='Child'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Superclass of Base is built-in Superclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='Superclass',
                                                            value=h.gceOOP.get_superclass(OPCODE='&gceOOP::get superclass of (CLASS)', class_='Base'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='getSuperclass on a missing class name throws',
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                    expr=h.gceOOP.get_superclass(OPCODE='&gceOOP::get superclass of (CLASS)', class_='__no_such_class__'),
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
                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                            name='Getters and Setters',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='setter transforms and stores, getter retrieves',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name="Setter prepends 'set:'; getter appends ':get'",
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='Box',
                                                            substack=[
                                                                h.gceOOP.define_setter(
                                                                    OPCODE='&gceOOP::define setter for (NAME) {:SHADOW1:} {:SHADOW2:} {SUBSTACK}',
                                                                    name='size',
                                                                    substack=[
                                                                        h.gceOOP.set_attribute(
                                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                                            instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                            name='_size',
                                                                            value=h.operator.join(
                                                                                OPCODE='&operators::join (STRING1) (STRING2)',
                                                                                string1='set:',
                                                                                string2=h.gceOOP.define_setter_value(OPCODE='&gceOOP::operator value {{id=gceOOP_defineSetterValue}}'),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_getter(
                                                                    OPCODE='&gceOOP::define getter for (NAME) {:SHADOW:} {SUBSTACK}',
                                                                    name='size',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.join(
                                                                                OPCODE='&operators::join (STRING1) (STRING2)',
                                                                                string1=h.gceOOP.get_attribute(
                                                                                    OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                                    name='_size',
                                                                                    instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                                ),
                                                                                string2=':get',
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='b',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Box', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='setAttribute goes through setter',
                                                            substack=[
                                                                h.gceOOP.set_attribute(
                                                                    OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                                    instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b'),
                                                                    name='size',
                                                                    value='42',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Raw _size attribute reflects setter transformation',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='_size',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b'),
                                                                    ),
                                                                    b='set:42',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='getAttribute goes through getter',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='size',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b'),
                                                                    ),
                                                                    b='set:42:get',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Update via setter replaces stored value',
                                                            substack=[
                                                                h.gceOOP.set_attribute(
                                                                    OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                                    instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b'),
                                                                    name='size',
                                                                    value='hello',
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='_size',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b'),
                                                                    ),
                                                                    b='set:hello',
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='size',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='getter-only attribute',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Getter for computed read-only value',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='Circle',
                                                            substack=[
                                                                h.gceOOP.define_getter(
                                                                    OPCODE='&gceOOP::define getter for (NAME) {:SHADOW:} {SUBSTACK}',
                                                                    name='doubled',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.multiply(
                                                                                OPCODE='&operators::(OPERAND1) * (OPERAND2)',
                                                                                operand1=h.gceOOP.get_attribute(
                                                                                    OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                                    name='_val',
                                                                                    instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                                ),
                                                                                operand2='2',
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='c',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Circle', posargs='[]'),
                                                        ),
                                                        h.gceOOP.set_attribute(
                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                            instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
                                                            name='_val',
                                                            value='7',
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='getter doubles _val',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='doubled',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
                                                                    ),
                                                                    b='14',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Raw _val unaffected',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='_val',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='attributes without getter/setter bypass directly',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='setAttribute and getAttribute on plain attributes',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Plain', substack=[]),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='p',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Plain', posargs='[]'),
                                                        ),
                                                        h.gceOOP.set_attribute(
                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                            instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='p'),
                                                            name='x',
                                                            value='99',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.get_attribute(
                                                                OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                name='x',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='p'),
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
                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                            name='Operator Methods',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='left add operator',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Custom class with left add: returns val + operand',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='MyNum',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["val"]', argdefaults='[]'),
                                                                h.gceOOP.define_special_method(
                                                                    OPCODE='&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}',
                                                                    special_method='init',
                                                                    substack=[
                                                                        h.gceOOP.set_attribute(
                                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                                            instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                            name='val',
                                                                            value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='val'),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='left add',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.add(
                                                                                OPCODE='&operators::(OPERAND1) + (OPERAND2)',
                                                                                operand1=h.gceOOP.get_attribute(
                                                                                    OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                                    name='val',
                                                                                    instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                                ),
                                                                                operand2=h.gceOOP.operator_operator_value(OPCODE='&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}'),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='left subtract',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.subtract(
                                                                                OPCODE='&operators::(OPERAND1) - (OPERAND2)',
                                                                                operand1=h.gceOOP.get_attribute(
                                                                                    OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                                    name='val',
                                                                                    instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                                ),
                                                                                operand2=h.gceOOP.operator_operator_value(OPCODE='&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}'),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='n',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='MyNum', posargs='["10"]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='left add: 10 + 5 = 15',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.operator.add(
                                                                        OPCODE='&operators::(OPERAND1) + (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='n'),
                                                                        operand2='5',
                                                                    ),
                                                                    b='15',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='left add: 10 + 0 = 10',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.operator.add(
                                                                        OPCODE='&operators::(OPERAND1) + (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='n'),
                                                                        operand2='0',
                                                                    ),
                                                                    b='10',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='left subtract: 10 - 3 = 7',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.operator.subtract(
                                                                        OPCODE='&operators::(OPERAND1) - (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='n'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='equals operator',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Custom equals: compares val attribute',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='Token',
                                                            substack=[
                                                                h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["id"]', argdefaults='[]'),
                                                                h.gceOOP.define_special_method(
                                                                    OPCODE='&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}',
                                                                    special_method='init',
                                                                    substack=[
                                                                        h.gceOOP.set_attribute(
                                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                                            instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                            name='id',
                                                                            value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='id'),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='equals',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.equals(
                                                                                OPCODE='&operators::(OPERAND1) = (OPERAND2)',
                                                                                operand1=h.gceOOP.get_attribute(
                                                                                    OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                                    name='id',
                                                                                    instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                                ),
                                                                                operand2=h.gceOOP.operator_operator_value(OPCODE='&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}'),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='tok',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Token', posargs='["abc"]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Equals the stored id',
                                                            substack=[
                                                                h.gceTestRunner.assert_(
                                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                                    condition=h.operator.equals(
                                                                        OPCODE='&operators::(OPERAND1) = (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='tok'),
                                                                        operand2='abc',
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Does not equal a different value',
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                    condition=h.operator.equals(
                                                                        OPCODE='&operators::(OPERAND1) = (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='tok'),
                                                                        operand2='xyz',
                                                                    ),
                                                                ),
                                                                h.gceTestRunner.assert_not(
                                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                    condition=h.operator.equals(
                                                                        OPCODE='&operators::(OPERAND1) = (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='tok'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='reverse operations',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Right-side method is used when left operand has no matching method',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='RightOnly',
                                                            substack=[
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='right add',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.join(
                                                                                OPCODE='&operators::join (STRING1) (STRING2)',
                                                                                string1='R+',
                                                                                string2=h.gceOOP.operator_operator_value(OPCODE='&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}'),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='r',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='RightOnly', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='plain_number + instance: triggers right add',
                                                            substack=[
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.operator.add(
                                                                        OPCODE='&operators::(OPERAND1) + (OPERAND2)',
                                                                        operand1='7',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='r'),
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
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Comparison reverse: op.greater triggers right-side less-than method',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='CompRight',
                                                            substack=[
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='less than',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.lt(
                                                                                OPCODE='&operators::(OPERAND1) < (OPERAND2)',
                                                                                operand1=h.gceOOP.operator_operator_value(OPCODE='&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}'),
                                                                                operand2=h.gceOOP.get_attribute(
                                                                                    OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                                    name='threshold',
                                                                                    instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='c',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='CompRight', posargs='[]'),
                                                        ),
                                                        h.gceOOP.set_attribute(
                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                            instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
                                                            name='threshold',
                                                            value='10',
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name="5 > c: triggers c's less-than with operator_value=5; 5<10 is true",
                                                            substack=[
                                                                h.gceTestRunner.assert_(
                                                                    OPCODE='&gceTestRunner::assert <CONDITION>',
                                                                    condition=h.operator.gt(
                                                                        OPCODE='&operators::(OPERAND1) > (OPERAND2)',
                                                                        operand1='5',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='15 > c: operator_value=15; 15<10 is false',
                                                            substack=[
                                                                h.gceTestRunner.assert_not(
                                                                    OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                                    condition=h.operator.gt(
                                                                        OPCODE='&operators::(OPERAND1) > (OPERAND2)',
                                                                        operand1='15',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='all operator kinds',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Arithmetic operator kinds: each left/right variant is callable',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='ArithOps',
                                                            substack=[
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='left add',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='L+'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='right add',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='R+'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='left subtract',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='L-'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='right subtract',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='R-'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='left multiply',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='L*'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='right multiply',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='R*'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='left divide',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='L/'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='right divide',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='R/'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='left power',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='L^'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='right power',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='R^'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='left mod',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='L%'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='right mod',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='R%'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='a',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='ArithOps', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Left-side arithmetic methods',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.operator.add(
                                                                        OPCODE='&operators::(OPERAND1) + (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                        operand2='0',
                                                                    ),
                                                                    b='L+',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.operator.subtract(
                                                                        OPCODE='&operators::(OPERAND1) - (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                        operand2='0',
                                                                    ),
                                                                    b='L-',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.operator.multiply(
                                                                        OPCODE='&operators::(OPERAND1) * (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                        operand2='1',
                                                                    ),
                                                                    b='L*',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.operator.divide(
                                                                        OPCODE='&operators::(OPERAND1) / (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                        operand2='1',
                                                                    ),
                                                                    b='L/',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.operator.power(
                                                                        OPCODE='&operators::(OPERAND1) ^ (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                        operand2='1',
                                                                    ),
                                                                    b='L^',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.operator.mod(
                                                                        OPCODE='&operators::(OPERAND1) mod (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                        operand2='1',
                                                                    ),
                                                                    b='L%',
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Right-side arithmetic methods (plain number on left)',
                                                            substack=[
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.operator.add(
                                                                        OPCODE='&operators::(OPERAND1) + (OPERAND2)',
                                                                        operand1='0',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                    ),
                                                                    b='R+',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.operator.subtract(
                                                                        OPCODE='&operators::(OPERAND1) - (OPERAND2)',
                                                                        operand1='0',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                    ),
                                                                    b='R-',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.operator.multiply(
                                                                        OPCODE='&operators::(OPERAND1) * (OPERAND2)',
                                                                        operand1='1',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                    ),
                                                                    b='R*',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.operator.divide(
                                                                        OPCODE='&operators::(OPERAND1) / (OPERAND2)',
                                                                        operand1='1',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                    ),
                                                                    b='R/',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.operator.power(
                                                                        OPCODE='&operators::(OPERAND1) ^ (OPERAND2)',
                                                                        operand1='1',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                    ),
                                                                    b='R^',
                                                                ),
                                                                h.gceTestRunner.assert_strict_equal(
                                                                    OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                                    a=h.operator.mod(
                                                                        OPCODE='&operators::(OPERAND1) mod (OPERAND2)',
                                                                        operand1='1',
                                                                        operand2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
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
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Comparison operator kinds: each kind is callable',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='CompOps',
                                                            substack=[
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='equals',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.true_boolean(OPCODE='&operators::true'),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='not equals',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.true_boolean(OPCODE='&operators::true'),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='greater than',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.true_boolean(OPCODE='&operators::true'),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='greater or equal',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.true_boolean(OPCODE='&operators::true'),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='less than',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.true_boolean(OPCODE='&operators::true'),
                                                                        ),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_operator_method(
                                                                    OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                                    operator_kind='less or equal',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(
                                                                            OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                            value=h.operator.true_boolean(OPCODE='&operators::true'),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='c',
                                                            value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='CompOps', posargs='[]'),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.operator.equals(
                                                                OPCODE='&operators::(OPERAND1) = (OPERAND2)',
                                                                operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
                                                                operand2='x',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.operator.notequal(
                                                                OPCODE='&operators::(OPERAND1) != (OPERAND2)',
                                                                operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
                                                                operand2='x',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.operator.gt(
                                                                OPCODE='&operators::(OPERAND1) > (OPERAND2)',
                                                                operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
                                                                operand2='x',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.operator.gtorequal(
                                                                OPCODE='&operators::(OPERAND1) >= (OPERAND2)',
                                                                operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
                                                                operand2='x',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.operator.lt(
                                                                OPCODE='&operators::(OPERAND1) < (OPERAND2)',
                                                                operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
                                                                operand2='x',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.operator.ltorequal(
                                                                OPCODE='&operators::(OPERAND1) <= (OPERAND2)',
                                                                operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
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
                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                            name='Static Methods',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='define and call a static method',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                    name='MathUtils',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["x"]', argdefaults='[]'),
                                                        h.gceOOP.define_static_method(
                                                            OPCODE='&gceOOP::define static method (NAME) {SUBSTACK}',
                                                            name='square',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                    value=h.operator.multiply(
                                                                        OPCODE='&operators::(OPERAND1) * (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='x'),
                                                                        operand2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='x'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["a","b"]', argdefaults='[]'),
                                                        h.gceOOP.define_static_method(
                                                            OPCODE='&gceOOP::define static method (NAME) {SUBSTACK}',
                                                            name='add',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                    value=h.operator.add(
                                                                        OPCODE='&operators::(OPERAND1) + (OPERAND2)',
                                                                        operand1=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                        operand2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='b'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='callStaticMethod: square(4) = 16',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceOOP.call_static_method(
                                                                OPCODE='&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)',
                                                                class_='MathUtils',
                                                                name='square',
                                                                posargs='["4"]',
                                                            ),
                                                            b='16',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='callStaticMethod: square(0) = 0',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceOOP.call_static_method(
                                                                OPCODE='&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)',
                                                                class_='MathUtils',
                                                                name='square',
                                                                posargs='["0"]',
                                                            ),
                                                            b='0',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='callStaticMethod: add(3, 7) = 10',
                                                    substack=[
                                                        h.gceTestRunner.assert_strict_equal(
                                                            OPCODE='&gceTestRunner::assert typed equality (A) = (B)',
                                                            a=h.gceOOP.call_static_method(
                                                                OPCODE='&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)',
                                                                class_='MathUtils',
                                                                name='add',
                                                                posargs='["3","7"]',
                                                            ),
                                                            b='10',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='getStaticMethodFunc + callFunction',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                    name='Fmt',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["val"]', argdefaults='[]'),
                                                        h.gceOOP.define_static_method(
                                                            OPCODE='&gceOOP::define static method (NAME) {SUBSTACK}',
                                                            name='wrap',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                    value=h.operator.join3(
                                                                        OPCODE='&operators::join (STRING1) (STRING2) (STRING3)',
                                                                        string1='[',
                                                                        string2=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='val'),
                                                                        string3=']',
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='getStaticMethodFunc returns a callable function',
                                                    substack=[
                                                        h.gceFuncsScopes.set_scope_var(
                                                            OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                            name='wrapFn',
                                                            value=h.gceOOP.get_static_method_func(OPCODE='&gceOOP::get static method (NAME) of (CLASS) as function', name='wrap', class_='Fmt'),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceFuncsScopes.typeof_value(
                                                                OPCODE='&gceFuncsScopes::typeof (VALUE)',
                                                                value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='wrapFn'),
                                                            ),
                                                            b=h.gceFuncsScopes.typeof_value_selection(OPCODE='&gceFuncsScopes::([TYPE])', type='Function (GCE)'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='callFunction on retrieved static method',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='wrapFn', posargs='["hello"]'),
                                                            b='[hello]',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Both callStaticMethod and callFunction give same result',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_static_method(
                                                                OPCODE='&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)',
                                                                class_='Fmt',
                                                                name='wrap',
                                                                posargs='["world"]',
                                                            ),
                                                            b=h.gceFuncsScopes.call_function(OPCODE='&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)', func='wrapFn', posargs='["world"]'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='error cases',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Solo', substack=[]),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Calling a non-existent static method throws',
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                    expr=h.gceOOP.call_static_method(
                                                                        OPCODE='&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)',
                                                                        class_='Solo',
                                                                        name='missing',
                                                                        posargs='[]',
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
                            ],
                        ),
                        h.gceTestRunner.test_scope(
                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                            name='Class Variables',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='set and get class variable',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Counter', substack=[]),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Set and read a class variable',
                                                    substack=[
                                                        h.gceOOP.set_class_variable(
                                                            OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                            class_='Counter',
                                                            name='count',
                                                            value='0',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.get_class_variable(OPCODE='&gceOOP::on (CLASS) get class var (NAME)', name='count', class_='Counter'),
                                                            b='0',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Update the class variable',
                                                    substack=[
                                                        h.gceOOP.set_class_variable(
                                                            OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                            class_='Counter',
                                                            name='count',
                                                            value='42',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.get_class_variable(OPCODE='&gceOOP::on (CLASS) get class var (NAME)', name='count', class_='Counter'),
                                                            b='42',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Multiple class variables coexist',
                                                    substack=[
                                                        h.gceOOP.set_class_variable(
                                                            OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                            class_='Counter',
                                                            name='name',
                                                            value='MyCounter',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.get_class_variable(OPCODE='&gceOOP::on (CLASS) get class var (NAME)', name='name', class_='Counter'),
                                                            b='MyCounter',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Reading first variable unchanged',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.get_class_variable(OPCODE='&gceOOP::on (CLASS) get class var (NAME)', name='count', class_='Counter'),
                                                            b='42',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='propertyNamesOfClass reflects class variables',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                    name='Config',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='doWork',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='done'),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceOOP.set_class_variable(
                                                    OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                    class_='Config',
                                                    name='version',
                                                    value='1',
                                                ),
                                                h.gceOOP.set_class_variable(
                                                    OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                    class_='Config',
                                                    name='author',
                                                    value='test',
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Class variable names listed',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='version',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='class variable', class_='Config'),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='author',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='class variable', class_='Config'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Method names NOT in class variable list',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                            text='doWork',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='class variable', class_='Config'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Instance method names listed correctly',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='doWork',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='instance method', class_='Config'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Class variable names NOT in instance method list',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                            text='version',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='instance method', class_='Config'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='delete class variable',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Bag', substack=[]),
                                                h.gceOOP.set_class_variable(
                                                    OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                    class_='Bag',
                                                    name='keep',
                                                    value='yes',
                                                ),
                                                h.gceOOP.set_class_variable(
                                                    OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                    class_='Bag',
                                                    name='remove',
                                                    value='no',
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Both exist before delete',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='keep',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='class variable', class_='Bag'),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='remove',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='class variable', class_='Bag'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Delete one',
                                                    substack=[
                                                        h.gceOOP.delete_class_variable(OPCODE='&gceOOP::on (CLASS) delete class var (NAME)', class_='Bag', name='remove'),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Deleted variable throws on get',
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                    expr=h.gceOOP.get_class_variable(OPCODE='&gceOOP::on (CLASS) get class var (NAME)', name='remove', class_='Bag'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Deleted variable absent from property names',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                            text='remove',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='class variable', class_='Bag'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Other variable unaffected',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='keep',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='class variable', class_='Bag'),
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.get_class_variable(OPCODE='&gceOOP::on (CLASS) get class var (NAME)', name='keep', class_='Bag'),
                                                            b='yes',
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='class variables are shared across instances',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                    name='Shared',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='getVar',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                    value=h.gceOOP.get_class_variable(OPCODE='&gceOOP::on (CLASS) get class var (NAME)', name='shared', class_='Shared'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceOOP.set_class_variable(
                                                    OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                    class_='Shared',
                                                    name='shared',
                                                    value='initial',
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='i1',
                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Shared', posargs='[]'),
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='i2',
                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Shared', posargs='[]'),
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Both instances see the same class variable',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_method(
                                                                OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='i1'),
                                                                name='getVar',
                                                                posargs='[]',
                                                            ),
                                                            b='initial',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_method(
                                                                OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='i2'),
                                                                name='getVar',
                                                                posargs='[]',
                                                            ),
                                                            b='initial',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Update class variable - both instances see new value',
                                                    substack=[
                                                        h.gceOOP.set_class_variable(
                                                            OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                            class_='Shared',
                                                            name='shared',
                                                            value='updated',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_method(
                                                                OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='i1'),
                                                                name='getVar',
                                                                posargs='[]',
                                                            ),
                                                            b='updated',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.call_method(
                                                                OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='i2'),
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
                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                            name='Introspection',
                            substack=[
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='getAttribute and setAttribute (direct)',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                    name='Person',
                                                    substack=[
                                                        h.gceFuncsScopes.configure_next_function_args(OPCODE='&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)', argnames='["name"]', argdefaults='[]'),
                                                        h.gceOOP.define_special_method(
                                                            OPCODE='&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}',
                                                            special_method='init',
                                                            substack=[
                                                                h.gceOOP.set_attribute(
                                                                    OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                                    instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                    name='name',
                                                                    value=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='name'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.define_instance_method(
                                                            OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='greet',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                    value=h.operator.join(
                                                                        OPCODE='&operators::join (STRING1) (STRING2)',
                                                                        string1='Hi, ',
                                                                        string2=h.gceOOP.get_attribute(
                                                                            OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                            name='name',
                                                                            instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceOOP.create_subclass_at(
                                                    OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                    name='Employee',
                                                    superclass='Person',
                                                    substack=[],
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='p',
                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Person', posargs='["Bob"]'),
                                                ),
                                                h.gceOOP.set_attribute(
                                                    OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                    instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='p'),
                                                    name='age',
                                                    value='30',
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Attribute set via init',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.get_attribute(
                                                                OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                name='name',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='p'),
                                                            ),
                                                            b='Bob',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Attribute set after creation',
                                                    substack=[
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.get_attribute(
                                                                OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                name='age',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='p'),
                                                            ),
                                                            b='30',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Overwrite attribute',
                                                    substack=[
                                                        h.gceOOP.set_attribute(
                                                            OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                            instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='p'),
                                                            name='name',
                                                            value='Robert',
                                                        ),
                                                        h.gceTestRunner.assert_unstrict_equal(
                                                            OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                            a=h.gceOOP.get_attribute(
                                                                OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                name='name',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='p'),
                                                            ),
                                                            b='Robert',
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Missing attribute throws',
                                                    substack=[
                                                        h.gceTestRunner.assert_throws(
                                                            OPCODE='&gceTestRunner::assert throws error {SUBSTACK}',
                                                            substack=[
                                                                h.gceFuncsScopes.execute_expression(
                                                                    OPCODE='&gceFuncsScopes::execute expression (EXPR)',
                                                                    expr=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='missing',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='p'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='getClassOfInstance',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Cat', substack=[]),
                                                h.gceOOP.create_subclass_at(
                                                    OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                    name='Kitten',
                                                    superclass='Cat',
                                                    substack=[],
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='c',
                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Cat', posargs='[]'),
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='k',
                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Kitten', posargs='[]'),
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='getClassOfInstance contains the class name',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='Cat',
                                                            value=h.gceOOP.get_class_of_instance(
                                                                OPCODE='&gceOOP::get class of (INSTANCE)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='Kitten',
                                                            value=h.gceOOP.get_class_of_instance(
                                                                OPCODE='&gceOOP::get class of (INSTANCE)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='k'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Cat instance does NOT report Kitten',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                            text='Kitten',
                                                            value=h.gceOOP.get_class_of_instance(
                                                                OPCODE='&gceOOP::get class of (INSTANCE)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='isInstance',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Fruit', substack=[]),
                                                h.gceOOP.create_subclass_at(
                                                    OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                    name='Apple',
                                                    superclass='Fruit',
                                                    substack=[],
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='f',
                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Fruit', posargs='[]'),
                                                ),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='a',
                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Apple', posargs='[]'),
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Instance of own class',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_instance(
                                                                OPCODE='&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?',
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='f'),
                                                                class_='Fruit',
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_instance(
                                                                OPCODE='&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?',
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                class_='Apple',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Subclass instance is instance of superclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_(
                                                            OPCODE='&gceTestRunner::assert <CONDITION>',
                                                            condition=h.gceOOP.is_instance(
                                                                OPCODE='&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?',
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='a'),
                                                                class_='Fruit',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Superclass instance is NOT instance of subclass',
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceOOP.is_instance(
                                                                OPCODE='&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?',
                                                                potential_instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='f'),
                                                                class_='Apple',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Non-instance values return false',
                                                    substack=[
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceOOP.is_instance(OPCODE='&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?', potential_instance='hello', class_='Fruit'),
                                                        ),
                                                        h.gceTestRunner.assert_not(
                                                            OPCODE='&gceTestRunner::assert not <CONDITION>',
                                                            condition=h.gceOOP.is_instance(
                                                                OPCODE='&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?',
                                                                potential_instance=h.gceFuncsScopes.nothing(OPCODE='&gceFuncsScopes::Nothing'),
                                                                class_='Fruit',
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='propertyNamesOfClass',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                    name='Widget',
                                                    substack=[
                                                        h.gceOOP.define_instance_method(
                                                            OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='render',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='rendered'),
                                                            ],
                                                        ),
                                                        h.gceOOP.define_static_method(
                                                            OPCODE='&gceOOP::define static method (NAME) {SUBSTACK}',
                                                            name='create',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='widget'),
                                                            ],
                                                        ),
                                                        h.gceOOP.define_getter(
                                                            OPCODE='&gceOOP::define getter for (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='width',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                    value=h.gceOOP.get_attribute(
                                                                        OPCODE='&gceOOP::on (INSTANCE) get attribute (NAME)',
                                                                        name='_w',
                                                                        instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.define_setter(
                                                            OPCODE='&gceOOP::define setter for (NAME) {:SHADOW1:} {:SHADOW2:} {SUBSTACK}',
                                                            name='height',
                                                            substack=[
                                                                h.gceOOP.set_attribute(
                                                                    OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                                    instance=h.gceOOP.self_value(OPCODE='&gceOOP::self'),
                                                                    name='_h',
                                                                    value=h.gceOOP.define_setter_value(OPCODE='&gceOOP::operator value {{id=gceOOP_defineSetterValue}}'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceOOP.set_class_variable(
                                                    OPCODE='&gceOOP::on (CLASS) set class var (NAME) to (VALUE)',
                                                    class_='Widget',
                                                    name='version',
                                                    value='2',
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Instance methods',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='render',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='instance method', class_='Widget'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                            text='create',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='instance method', class_='Widget'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Static methods',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='create',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='static method', class_='Widget'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                            text='render',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='static method', class_='Widget'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Getter methods',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='width',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='getter method', class_='Widget'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                            text='height',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='getter method', class_='Widget'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Setter methods',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='height',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='setter method', class_='Widget'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                            text='width',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='setter method', class_='Widget'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Class variables',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='version',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='class variable', class_='Widget'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='propertyNamesOfClass edge cases',
                                    substack=[
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Empty class has no own instance methods (beyond built-in)',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Empty', substack=[]),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                            text='render',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='instance method', class_='Empty'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                            text='create',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='static method', class_='Empty'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                            text='version',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='class variable', class_='Empty'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Subclass without own methods still sees inherited methods',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='Parent',
                                                            substack=[
                                                                h.gceOOP.define_instance_method(
                                                                    OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                                    name='inherited',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='from-parent'),
                                                                    ],
                                                                ),
                                                                h.gceOOP.define_static_method(
                                                                    OPCODE='&gceOOP::define static method (NAME) {SUBSTACK}',
                                                                    name='parentStatic',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='static-from-parent'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.create_subclass_at(
                                                            OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                            name='ChildNoMethods',
                                                            superclass='Parent',
                                                            substack=[],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Inherited instance method visible on child',
                                                            substack=[
                                                                h.gceTestRunner.assert_text_in_value(
                                                                    OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                                    text='inherited',
                                                                    value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='instance method', class_='ChildNoMethods'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Inherited static method visible on child',
                                                            substack=[
                                                                h.gceTestRunner.assert_text_in_value(
                                                                    OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                                    text='parentStatic',
                                                                    value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='static method', class_='ChildNoMethods'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name="Parent's own methods also still visible on parent",
                                                            substack=[
                                                                h.gceTestRunner.assert_text_in_value(
                                                                    OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                                    text='inherited',
                                                                    value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='instance method', class_='Parent'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        h.gceTestRunner.test_scope(
                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                            name='Overriding a method replaces it, not duplicates it',
                                            substack=[
                                                h.gceFuncsScopes.create_var_scope(
                                                    OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='Base2',
                                                            substack=[
                                                                h.gceOOP.define_instance_method(
                                                                    OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                                    name='greet',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='base-greet'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.create_subclass_at(
                                                            OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                            name='Child2',
                                                            superclass='Base2',
                                                            substack=[
                                                                h.gceOOP.define_instance_method(
                                                                    OPCODE='&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}',
                                                                    name='greet',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='child-greet'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name="greet appears in child's instance methods",
                                                            substack=[
                                                                h.gceTestRunner.assert_text_in_value(
                                                                    OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                                    text='greet',
                                                                    value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='instance method', class_='Child2'),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.test_scope(
                                                            OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                            name='Override is active � child instance calls child version',
                                                            substack=[
                                                                h.gceFuncsScopes.set_scope_var(
                                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                                    name='c',
                                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Child2', posargs='[]'),
                                                                ),
                                                                h.gceTestRunner.assert_unstrict_equal(
                                                                    OPCODE='&gceTestRunner::assert string equality (A) = (B)',
                                                                    a=h.gceOOP.call_method(
                                                                        OPCODE='&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)',
                                                                        instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='c'),
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
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='getAllAttributes',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='Data', substack=[]),
                                                h.gceFuncsScopes.set_scope_var(
                                                    OPCODE='&gceFuncsScopes::set var (NAME) to (VALUE) in current scope',
                                                    name='d',
                                                    value=h.gceOOP.create_instance(OPCODE='&gceOOP::create instance of class (CLASS) with positional args (POSARGS)', class_='Data', posargs='[]'),
                                                ),
                                                h.gceOOP.set_attribute(
                                                    OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                    instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='d'),
                                                    name='x',
                                                    value='1',
                                                ),
                                                h.gceOOP.set_attribute(
                                                    OPCODE='&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)',
                                                    instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='d'),
                                                    name='y',
                                                    value='2',
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='getAllAttributes includes all set attributes',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='x',
                                                            value=h.gceOOP.get_all_attributes(
                                                                OPCODE='&gceOOP::all attributes of (INSTANCE)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='d'),
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='y',
                                                            value=h.gceOOP.get_all_attributes(
                                                                OPCODE='&gceOOP::all attributes of (INSTANCE)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='d'),
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='1',
                                                            value=h.gceOOP.get_all_attributes(
                                                                OPCODE='&gceOOP::all attributes of (INSTANCE)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='d'),
                                                            ),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='2',
                                                            value=h.gceOOP.get_all_attributes(
                                                                OPCODE='&gceOOP::all attributes of (INSTANCE)',
                                                                instance=h.gceFuncsScopes.get_scope_var(OPCODE='&gceFuncsScopes::get var (NAME)', name='d'),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='propertyNamesOfClass: special method dropdown',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceOOP.create_class_at(
                                                    OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                    name='Nameable',
                                                    substack=[
                                                        h.gceOOP.define_special_method(OPCODE='&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}', special_method='init', substack=[]),
                                                        h.gceOOP.define_special_method(
                                                            OPCODE='&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}',
                                                            special_method='as string',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='nameable'),
                                                            ],
                                                        ),
                                                        h.gceOOP.define_operator_method(
                                                            OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                            operator_kind='left add',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                    value=h.operator.join(
                                                                        OPCODE='&operators::join (STRING1) (STRING2)',
                                                                        string1='L+',
                                                                        string2=h.gceOOP.operator_operator_value(OPCODE='&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}'),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.define_operator_method(
                                                            OPCODE='&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}',
                                                            operator_kind='not equals',
                                                            substack=[
                                                                h.gceFuncsScopes.return_value(
                                                                    OPCODE='&gceFuncsScopes::return (VALUE)',
                                                                    value=h.operator.true_boolean(OPCODE='&operators::true'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name="init appears as 'init' in special method list",
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='init',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='special method', class_='Nameable'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name="as string appears as 'as string' in special method list",
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='as string',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='special method', class_='Nameable'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Special methods do NOT appear in instance method list',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                            text='init',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='instance method', class_='Nameable'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                            text='as string',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='instance method', class_='Nameable'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Operator methods appear as public names in operator method list',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='left add',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='operator method', class_='Nameable'),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='not equals',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='operator method', class_='Nameable'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Operator methods do NOT appear in instance or special method list',
                                                    substack=[
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                            text='left add',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='instance method', class_='Nameable'),
                                                        ),
                                                        h.gceTestRunner.assert_text_not_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) not in value (VALUE)',
                                                            text='left add',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='special method', class_='Nameable'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                h.gceTestRunner.test_scope(
                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                    name='propertyNamesOfClass: special method inheritance',
                                    substack=[
                                        h.gceFuncsScopes.create_var_scope(
                                            OPCODE='&gceFuncsScopes::create local variable scope {SUBSTACK}',
                                            substack=[
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Empty class always has init from common superclass',
                                                    substack=[
                                                        h.gceOOP.create_class_at(OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}', name='BareClass', substack=[]),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='init',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='special method', class_='BareClass'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Class with only as string still inherits init',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='AsStringOnly',
                                                            substack=[
                                                                h.gceOOP.define_special_method(
                                                                    OPCODE='&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}',
                                                                    special_method='as string',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='str'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='init',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='special method', class_='AsStringOnly'),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='as string',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='special method', class_='AsStringOnly'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Subclass inherits special methods from parent',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='SpBase',
                                                            substack=[
                                                                h.gceOOP.define_special_method(
                                                                    OPCODE='&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}',
                                                                    special_method='as string',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='base'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.create_subclass_at(
                                                            OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                            name='SpChild',
                                                            superclass='SpBase',
                                                            substack=[],
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='as string',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='special method', class_='SpChild'),
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='init',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='special method', class_='SpChild'),
                                                        ),
                                                    ],
                                                ),
                                                h.gceTestRunner.test_scope(
                                                    OPCODE='&gceTestRunner::test scope named (NAME) {SUBSTACK}',
                                                    name='Subclass overriding as string replaces, not duplicates',
                                                    substack=[
                                                        h.gceOOP.create_class_at(
                                                            OPCODE='&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}',
                                                            name='SpBase2',
                                                            substack=[
                                                                h.gceOOP.define_special_method(
                                                                    OPCODE='&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}',
                                                                    special_method='as string',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='base2'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceOOP.create_subclass_at(
                                                            OPCODE='&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}',
                                                            name='SpChild2',
                                                            superclass='SpBase2',
                                                            substack=[
                                                                h.gceOOP.define_special_method(
                                                                    OPCODE='&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}',
                                                                    special_method='as string',
                                                                    substack=[
                                                                        h.gceFuncsScopes.return_value(OPCODE='&gceFuncsScopes::return (VALUE)', value='child2'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        h.gceTestRunner.assert_text_in_value(
                                                            OPCODE='&gceTestRunner::assert text (TEXT) in value (VALUE)',
                                                            text='as string',
                                                            value=h.gceOOP.property_names_of_class(OPCODE='&gceOOP::([PROPERTY]) names of class (CLASS)', property='special method', class_='SpChild2'),
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
            uuid=t.UUID('9b731a89-b6f8-407a-815f-b2d90a10c2b2'),
        ),
    ],
    sprite_layer_stack=[
        t.UUID('40db1669-66d0-4bbc-95b1-e8b0002b15b8'),
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