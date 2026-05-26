ThirdProject(
    stage=ThirdStage(
        scripts=[],
        comments=[],
        costumes=[
            ThirdVectorCostume(
                name="empty",
                file_extension="svg",
                rotation_center=(240, 180),
                content='<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" height="2" version="1.1" viewBox="-1 -1 2 2" width="2">
  <!-- Exported by Scratch - http://scratch.mit.edu/ -->
</svg>',
            ),
        ],
        sounds=[],
        costume_index=0,
        volume=100,
    ),
    sprites=[
        ThirdSprite(
            scripts=[
                ThirdScript(
                    blocks=[
                        whenflagclicked(OPCODE="&events::when green flag clicked"),
                        test_scope(
                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                            name="TypeChecker",
                            substack=[
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="My Types",
                                    substack=[
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=create_function_named(OPCODE="&gceFuncsScopes::create function named (NAME) {SUBSTACK}", name="myFn", substack=[]),
                                                type="Function (GCE)",
                                            ),
                                        ),
                                        label_command(OPCODE="&jwProto::// (LABEL) {{id=jwProto_labelCommand}}", label="Methods can not be accessed from a reporter"),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=create_class_named(OPCODE="&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}", name="MyClass", substack=[]),
                                                type="Class (GCE)",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=create_instance(
                                                    OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)",
                                                    class_=create_class_named(OPCODE="&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}", name="MyClass", substack=[]),
                                                    posargs="[]",
                                                ),
                                                type="Class Instance (GCE)",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                type="Nothing (GCE)",
                                            ),
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="Common/Safe JS data types",
                                    substack=[
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=js_reporter(OPCODE="&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsReporter}}", code="return undefined"),
                                                type="JavaScript Undefined",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=js_reporter(OPCODE="&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsReporter}}", code="return null"),
                                                type="JavaScript Null",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=true_boolean(OPCODE="&operators::true"),
                                                type="Boolean",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?", value="777", type="Number"),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?", value="hello", type="String"),
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="Custom Extension Types",
                                    substack=[
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=new_buffer(OPCODE="&agBuffer::create new array buffer of size (LENGTH)", length="1"),
                                                type="Buffer (AndrewGaming587)",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=create_pointer(
                                                    OPCODE="&agBuffer::create ([TYPE]) pointer for (BUFFER) at (INDEX) <ENDIAN>",
                                                    index="0",
                                                    endian=False,
                                                    buffer=new_buffer(OPCODE="&agBuffer::create new array buffer of size (LENGTH)", length="1"),
                                                    type="Uint8",
                                                ),
                                                type="Buffer Pointer (AndrewGaming587)",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=current_date(OPCODE="&ddeDateFormat::current date"),
                                                type="Date (Old Version) (ddededodediamante)",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=current_date(OPCODE="&ddeDateFormatV2::current date"),
                                                type="Date (ddededodediamante)",
                                            ),
                                        ),
                                        label_command(OPCODE="&jwProto::// (LABEL) {{id=jwProto_labelCommand}}", label="You can't access a div effect type from any reporter"),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=iter_builder(OPCODE="&divIterator::iterator builder with {:S:} = (STATE) {SUBSTACK}", state="", substack=[]),
                                                type="Iterator (Div)",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=blank(OPCODE="&dogeiscutObject::blank object"),
                                                type="Object (DogeisCut)",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=regex(OPCODE="&dogeiscutRegularExpressions::regular expression (PATTERN) (FLAGS)", pattern="(.*)", flags="gm"),
                                                type="Regular Expression (DogeisCut)",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=blank(OPCODE="&dogeiscutSet::blank set"),
                                                type="Set (DogeisCut)",
                                            ),
                                        ),
                                        label_command(OPCODE="&jwProto::// (LABEL) {{id=jwProto_labelCommand}}", label="You can't access a timer type from any reporter"),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=blank(OPCODE="&jwArray::blank array"),
                                                type="Array (jwklong)",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=new_color(OPCODE="&jwColor::new color (COLOR)", color="#ff0000"),
                                                type="Color (jwklong)",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=now(OPCODE="&jwDate::now"),
                                                type="Date (jwklong)",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=new_lambda(OPCODE="&jwLambda::new lambda {:ARG:} {SUBSTACK}", substack=[]),
                                                type="Lambda (jwklong)",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=add(OPCODE="&jwNum::(A) + (B)", a="1", b="2"),
                                                type="Number (jwklong)",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=this(OPCODE="&jwTargets::this target"),
                                                type="Target (jwklong)",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=new_vector(OPCODE="&jwVector::new vector x: (X) y: (Y)", x="1", y="2"),
                                                type="Vector (jwklong)",
                                            ),
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=new_node(OPCODE="&jwXML::new node (NAME)", name="test"),
                                                type="XML (jwklong)",
                                            ),
                                        ),
                                        label_function(
                                            OPCODE="&jwProto::// (LABEL) {SUBSTACK}",
                                            label="For this to work please create a canvas variable e.g. 'myCanvasVar', then enable the condition",
                                            substack=[
                                                if_(
                                                    OPCODE="&control::if <CONDITION> then {THEN}",
                                                    condition=False,
                                                    then=[
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=typeof_value_is_menu(OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?", value="<put the canvas variable block here>", type="Canvas (RedMan13)"),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        assert_(
                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                            condition=typeof_value_is_menu(
                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                value=get_colour(OPCODE="&fruitsPaintUtils::get colour from colour name (COLOUR_NAME)", colour_name="orange"),
                                                type="Paint Utils Colour (Fruits555000)",
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        test_scope(
                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                            name="Cast",
                            substack=[
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="toArray",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="my var", value="hello"),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="var list",
                                                    value=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="all scopes"),
                                                ),
                                                assert_type(
                                                    OPCODE="&gceTestRunner::assert type of (VALUE) is ([EXPECTED])",
                                                    value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="var list"),
                                                    expected="Array (jwklong)",
                                                ),
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="var list"),
                                                    b='["my var"]',
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="toObject",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="MyClass", substack=[]),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="instance var",
                                                    value=create_instance(
                                                        OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)",
                                                        class_=create_class_named(OPCODE="&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}", name="MyClass", substack=[]),
                                                        posargs="[]",
                                                    ),
                                                ),
                                                set_attribute(
                                                    OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                    instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="instance var"),
                                                    name="my attribute",
                                                    value="hello",
                                                ),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="attributes",
                                                    value=get_all_attributes(
                                                        OPCODE="&gceOOP::all attributes of (INSTANCE)",
                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="instance var"),
                                                    ),
                                                ),
                                                assert_type(
                                                    OPCODE="&gceTestRunner::assert type of (VALUE) is ([EXPECTED])",
                                                    value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="attributes"),
                                                    expected="Object (DogeisCut)",
                                                ),
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="attributes"),
                                                    b='{"my attribute":"hello"}',
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="toClass && toClassInstance && toFunction",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="MyClass", substack=[]),
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=get_superclass(
                                                        OPCODE="&gceOOP::get superclass of (CLASS)",
                                                        class_=create_subclass_named(
                                                            OPCODE="&gceOOP::create subclass named (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                            name="Sub",
                                                            superclass="MyClass",
                                                            substack=[],
                                                        ),
                                                    ),
                                                    b="<Class 'MyClass'>",
                                                ),
                                                assert_throws_contains(
                                                    OPCODE="&gceTestRunner::assert throws error containing (MSG) {SUBSTACK}",
                                                    msg="but got no input value",
                                                    substack=[
                                                        execute_expression(
                                                            OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                            expr=get_superclass(
                                                                OPCODE="&gceOOP::get superclass of (CLASS)",
                                                                class_=js_reporter(OPCODE="&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsReporter}}", code="return undefined"),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                assert_throws_contains(
                                                    OPCODE="&gceTestRunner::assert throws error containing (MSG) {SUBSTACK}",
                                                    msg="but got no input value",
                                                    substack=[
                                                        execute_expression(
                                                            OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                            expr=get_superclass(
                                                                OPCODE="&gceOOP::get superclass of (CLASS)",
                                                                class_=js_reporter(OPCODE="&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsReporter}}", code="return null"),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=get_superclass(OPCODE="&gceOOP::get superclass of (CLASS)", class_="MyClass"),
                                                    b="<Class 'Superclass'>",
                                                ),
                                                create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="513", substack=[]),
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=get_superclass(OPCODE="&gceOOP::get superclass of (CLASS)", class_="513"),
                                                    b="<Class 'Superclass'>",
                                                ),
                                                assert_throws_contains(
                                                    OPCODE="&gceTestRunner::assert throws error containing (MSG) {SUBSTACK}",
                                                    msg="but got no input value",
                                                    substack=[
                                                        execute_expression(
                                                            OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                            expr=get_superclass(
                                                                OPCODE="&gceOOP::get superclass of (CLASS)",
                                                                class_=js_reporter(OPCODE="&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsReporter}}", code="return null"),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                assert_throws(
                                                    OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                    substack=[
                                                        create_subclass_at(
                                                            OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                            name="Sub2",
                                                            superclass=create_function_named(OPCODE="&gceFuncsScopes::create function named (NAME) {SUBSTACK}", name="myFunction", substack=[]),
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
                        test_scope(
                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                            name="Scoped Variables Blocks",
                            substack=[
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="set/get/exists",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Set and read a local variable",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="myVar", kind="all scopes"),
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="myVar", kind="local scope"),
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="myVar", kind="global scope"),
                                                        ),
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="myVar", value="hello"),
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="myVar"),
                                                            b="hello",
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="myVar", kind="all scopes"),
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="myVar", kind="local scope"),
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="myVar", kind="global scope"),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="delete var",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Delete removes the variable from the current scope",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="tmp", value="to-delete"),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="tmp", kind="all scopes"),
                                                        ),
                                                        delete_scope_var(OPCODE="&gceFuncsScopes::delete var (NAME) in current scope", name="tmp"),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="tmp", kind="all scopes"),
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="tmp", kind="local scope"),
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="tmp", kind="global scope"),
                                                        ),
                                                        assert_throws(
                                                            OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                            substack=[
                                                                execute_expression(
                                                                    OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                    expr=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="tmp"),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="all variables + local scope",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="List variables by kind and verify nested local scope behavior",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="a", value="1"),
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="b", value="2"),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="all scopes"),
                                                            b='["a","b"]',
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="local scope"),
                                                            b='["a","b"]',
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="global scope"),
                                                            b="[]",
                                                        ),
                                                        create_var_scope(
                                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                            substack=[
                                                                test_scope(
                                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                                    name="In a fresh local scope, inherited names are visible in all scopes",
                                                                    substack=[
                                                                        assert_unstrict_equal(
                                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                            a=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="all scopes"),
                                                                            b='["a","b"]',
                                                                        ),
                                                                        assert_unstrict_equal(
                                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                            a=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="local scope"),
                                                                            b="[]",
                                                                        ),
                                                                        assert_unstrict_equal(
                                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                            a=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="global scope"),
                                                                            b="[]",
                                                                        ),
                                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="c", value="3"),
                                                                        assert_unstrict_equal(
                                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                            a=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="all scopes"),
                                                                            b='["a","b","c"]',
                                                                        ),
                                                                        assert_unstrict_equal(
                                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                            a=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="local scope"),
                                                                            b='["c"]',
                                                                        ),
                                                                        assert_unstrict_equal(
                                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                            a=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="global scope"),
                                                                            b="[]",
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="c", kind="local scope"),
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="c", kind="all scopes"),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="allVariables with globals and locals simultaneously",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="kind_global and kind_local see only their own tier; kind_all sees both",
                                            substack=[
                                                run_with_separate_globals(
                                                    OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="globalX", value="gx"),
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="globalY", value="gy"),
                                                        create_var_scope(
                                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                            substack=[
                                                                set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="localZ", value="lz"),
                                                                test_scope(
                                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                                    name="kind_global sees globals only",
                                                                    substack=[
                                                                        assert_text_in_value(
                                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                                            text="globalX",
                                                                            value=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="global scope"),
                                                                        ),
                                                                        assert_text_in_value(
                                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                                            text="globalY",
                                                                            value=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="global scope"),
                                                                        ),
                                                                        assert_text_not_in_value(
                                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                                            text="localZ",
                                                                            value=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="global scope"),
                                                                        ),
                                                                    ],
                                                                ),
                                                                test_scope(
                                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                                    name="kind_local sees locals only",
                                                                    substack=[
                                                                        assert_text_in_value(
                                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                                            text="localZ",
                                                                            value=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="local scope"),
                                                                        ),
                                                                        assert_text_not_in_value(
                                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                                            text="globalX",
                                                                            value=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="local scope"),
                                                                        ),
                                                                        assert_text_not_in_value(
                                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                                            text="globalY",
                                                                            value=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="local scope"),
                                                                        ),
                                                                    ],
                                                                ),
                                                                test_scope(
                                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                                    name="kind_all sees both globals and locals",
                                                                    substack=[
                                                                        assert_text_in_value(
                                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                                            text="globalX",
                                                                            value=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="all scopes"),
                                                                        ),
                                                                        assert_text_in_value(
                                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                                            text="globalY",
                                                                            value=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="all scopes"),
                                                                        ),
                                                                        assert_text_in_value(
                                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                                            text="localZ",
                                                                            value=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="all scopes"),
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
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="bind global + non-local",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Bind global in an inner scope and mutate it",
                                            substack=[
                                                run_with_separate_globals(
                                                    OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="globalCounter", value="0"),
                                                        create_var_scope(
                                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                            substack=[
                                                                bind_var_to_scope(OPCODE="&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope", kind="global", name="globalCounter"),
                                                                set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="globalCounter", value="1"),
                                                            ],
                                                        ),
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="globalCounter"),
                                                            b="1",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Bind non-local variable in nested local scopes and mutate it",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="outerLocal", value="A"),
                                                        create_var_scope(
                                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                            substack=[
                                                                bind_var_to_scope(OPCODE="&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope", kind="non-local", name="outerLocal"),
                                                                set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="outerLocal", value="B"),
                                                            ],
                                                        ),
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="outerLocal"),
                                                            b="B",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="shadowing: inner scope shadows outer name",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="get_scope_var resolves to innermost definition",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="x", value="outer"),
                                                        create_var_scope(
                                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                            substack=[
                                                                set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="x", value="inner"),
                                                                test_scope(
                                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                                    name="Inner scope sees the inner value",
                                                                    substack=[
                                                                        assert_strict_equal(
                                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                            a=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="x"),
                                                                            b="inner",
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="After inner scope exits, outer value is restored",
                                                            substack=[
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="x"),
                                                                    b="outer",
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="bind then delete",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Delete a bound global variable from an inner scope",
                                            substack=[
                                                run_with_separate_globals(
                                                    OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="toDelete", value="exists"),
                                                        create_var_scope(
                                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                            substack=[
                                                                bind_var_to_scope(OPCODE="&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope", kind="global", name="toDelete"),
                                                                delete_scope_var(OPCODE="&gceFuncsScopes::delete var (NAME) in current scope", name="toDelete"),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Variable is gone from globals after delete",
                                                            substack=[
                                                                assert_not(
                                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                    condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="toDelete", kind="global scope"),
                                                                ),
                                                                assert_not(
                                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                    condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="toDelete", kind="all scopes"),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Delete a bound non-local variable from an inner scope",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="outerVar", value="exists"),
                                                        create_var_scope(
                                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                            substack=[
                                                                bind_var_to_scope(OPCODE="&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope", kind="non-local", name="outerVar"),
                                                                delete_scope_var(OPCODE="&gceFuncsScopes::delete var (NAME) in current scope", name="outerVar"),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Variable is gone from outer scope after delete",
                                                            substack=[
                                                                assert_not(
                                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                    condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="outerVar", kind="all scopes"),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="bind error paths",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Binding a missing global/non-local variable should throw",
                                            substack=[
                                                assert_throws(
                                                    OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                    substack=[
                                                        bind_var_to_scope(OPCODE="&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope", kind="global", name="missingGlobal"),
                                                    ],
                                                ),
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        assert_throws(
                                                            OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                            substack=[
                                                                bind_var_to_scope(OPCODE="&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope", kind="non-local", name="missingNonLocal"),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="createVarScope cleanup on error",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="exitUserScope must run even if an error is thrown inside the scope",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="outerVar", value="present"),
                                                        create_var_scope(
                                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                            substack=[
                                                                set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="innerVar", value="value"),
                                                                assert_throws(
                                                                    OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                                    substack=[
                                                                        execute_expression(
                                                                            OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                            expr=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="__missing_var__"),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Inner variable should be gone after error",
                                                            substack=[
                                                                assert_not(
                                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                    condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="innerVar", kind="all scopes"),
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Outer variable should still exist",
                                                            substack=[
                                                                assert_(
                                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                                    condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="outerVar", kind="all scopes"),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="scopeVarExists with 3-level nesting",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Verify kindLocal, kindAll, kindGlobal across 3 scopes",
                                            substack=[
                                                run_with_separate_globals(
                                                    OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="globalVar", value="g"),
                                                        create_var_scope(
                                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                            substack=[
                                                                set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="level1", value="L1"),
                                                                create_var_scope(
                                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                                    substack=[
                                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="level2", value="L2"),
                                                                        create_var_scope(
                                                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                                            substack=[
                                                                                set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="level3", value="L3"),
                                                                                test_scope(
                                                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                                                    name="Innermost: level3 is local, others are not",
                                                                                    substack=[
                                                                                        assert_(
                                                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="level3", kind="local scope"),
                                                                                        ),
                                                                                        assert_not(
                                                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="level1", kind="local scope"),
                                                                                        ),
                                                                                        assert_not(
                                                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="level2", kind="local scope"),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                test_scope(
                                                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                                                    name="All three are visible via kindAll",
                                                                                    substack=[
                                                                                        assert_(
                                                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="level1", kind="all scopes"),
                                                                                        ),
                                                                                        assert_(
                                                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="level2", kind="all scopes"),
                                                                                        ),
                                                                                        assert_(
                                                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="level3", kind="all scopes"),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                test_scope(
                                                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                                                    name="Global is visible via kindGlobal and kindAll",
                                                                                    substack=[
                                                                                        assert_(
                                                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="globalVar", kind="global scope"),
                                                                                        ),
                                                                                        assert_(
                                                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="globalVar", kind="all scopes"),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                test_scope(
                                                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                                                    name="Local vars are NOT global",
                                                                                    substack=[
                                                                                        assert_not(
                                                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="level3", kind="global scope"),
                                                                                        ),
                                                                                        assert_not(
                                                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="level2", kind="global scope"),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                                test_scope(
                                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                                    name="level2 and level3 gone after exiting their scopes",
                                                                    substack=[
                                                                        assert_not(
                                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="level2", kind="all scopes"),
                                                                        ),
                                                                        assert_not(
                                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="level3", kind="all scopes"),
                                                                        ),
                                                                        assert_(
                                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="level1", kind="local scope"),
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
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="runWithSeparateGlobals",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Outer locals are not visible inside",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="outerLocal", value="outer"),
                                                        run_with_separate_globals(
                                                            OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                                            substack=[
                                                                assert_not(
                                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                    condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="outerLocal", kind="all scopes"),
                                                                ),
                                                                assert_not(
                                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                    condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="outerLocal", kind="local scope"),
                                                                ),
                                                                assert_not(
                                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                    condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="outerLocal", kind="global scope"),
                                                                ),
                                                                assert_throws(
                                                                    OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                                    substack=[
                                                                        execute_expression(
                                                                            OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                            expr=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="outerLocal"),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Outer globals are not visible inside",
                                            substack=[
                                                set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="outerGlobal", value="outerGlobalValue"),
                                                run_with_separate_globals(
                                                    OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                                    substack=[
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="outerGlobal", kind="all scopes"),
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="outerGlobal", kind="global scope"),
                                                        ),
                                                        assert_throws(
                                                            OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                            substack=[
                                                                execute_expression(
                                                                    OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                    expr=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="outerGlobal"),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                delete_scope_var(OPCODE="&gceFuncsScopes::delete var (NAME) in current scope", name="outerGlobal"),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Writes inside do not affect outer locals",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="sharedName", value="before"),
                                                        run_with_separate_globals(
                                                            OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                                            substack=[
                                                                set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="sharedName", value="inside"),
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="sharedName"),
                                                                    b="inside",
                                                                ),
                                                            ],
                                                        ),
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="sharedName"),
                                                            b="before",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Writes inside do not affect outer globals",
                                            substack=[
                                                set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="sharedGlobal", value="globalBefore"),
                                                run_with_separate_globals(
                                                    OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="sharedGlobal", value="globalInside"),
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="sharedGlobal"),
                                                            b="globalInside",
                                                        ),
                                                    ],
                                                ),
                                                assert_strict_equal(
                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                    a=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="sharedGlobal"),
                                                    b="globalBefore",
                                                ),
                                                delete_scope_var(OPCODE="&gceFuncsScopes::delete var (NAME) in current scope", name="sharedGlobal"),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Inner globals and locals start empty",
                                            substack=[
                                                run_with_separate_globals(
                                                    OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                                    substack=[
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="all scopes"),
                                                            b="[]",
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="global scope"),
                                                            b="[]",
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=all_variables(OPCODE="&gceFuncsScopes::all variables in ([KIND])", kind="local scope"),
                                                            b="[]",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Variables created inside are gone after block exits",
                                            substack=[
                                                run_with_separate_globals(
                                                    OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="innerOnly", value="value"),
                                                    ],
                                                ),
                                                assert_not(
                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                    condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="innerOnly", kind="all scopes"),
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Cleanup happens even if an error is thrown inside",
                                            substack=[
                                                assert_throws(
                                                    OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                    substack=[
                                                        run_with_separate_globals(
                                                            OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                                            substack=[
                                                                set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="innerError", value="value"),
                                                                execute_expression(
                                                                    OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                    expr=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="__missing__"),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                assert_not(
                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                    condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="innerError", kind="all scopes"),
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Nested runWithSeparateGlobals are fully independent",
                                            substack=[
                                                set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="outerG", value="OG"),
                                                run_with_separate_globals(
                                                    OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope", name="middleG", value="MG"),
                                                        run_with_separate_globals(
                                                            OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                                            substack=[
                                                                assert_not(
                                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                    condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="outerG", kind="all scopes"),
                                                                ),
                                                                assert_not(
                                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                    condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="middleG", kind="all scopes"),
                                                                ),
                                                            ],
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="middleG", kind="global scope"),
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="outerG", kind="all scopes"),
                                                        ),
                                                    ],
                                                ),
                                                assert_(
                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                    condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="outerG", kind="global scope"),
                                                ),
                                                assert_not(
                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                    condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="middleG", kind="all scopes"),
                                                ),
                                                delete_scope_var(OPCODE="&gceFuncsScopes::delete var (NAME) in current scope", name="outerG"),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        test_scope(
                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                            name="Function Blocks",
                            substack=[
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="basic function",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Define a simple function that returns a constant",
                                                    substack=[
                                                        create_function_at(
                                                            OPCODE="&gceFuncsScopes::create function at var (NAME) {SUBSTACK}",
                                                            name="myFunc",
                                                            substack=[
                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="hello"),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Call the function with no arguments",
                                                    substack=[
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="myFunc", posargs="[]"),
                                                            b="hello",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="function with args",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Configure and define function with two arguments",
                                                    substack=[
                                                        configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["greeting", "name"]', argdefaults="[]"),
                                                        create_function_at(
                                                            OPCODE="&gceFuncsScopes::create function at var (NAME) {SUBSTACK}",
                                                            name="greet",
                                                            substack=[
                                                                return_value(
                                                                    OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                    value=join3(
                                                                        OPCODE="&operators::join (STRING1) (STRING2) (STRING3)",
                                                                        string1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="greeting"),
                                                                        string2=" ",
                                                                        string3=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="name"),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Call with two arguments passed as array",
                                                    substack=[
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="greet", posargs='["Hello", "Ada"]'),
                                                            b="Hello Ada",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="default arguments",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Configure function with required arg and default trailing arg",
                                                    substack=[
                                                        configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["person", "greeting"]', argdefaults='["Hi"]'),
                                                        create_function_at(
                                                            OPCODE="&gceFuncsScopes::create function at var (NAME) {SUBSTACK}",
                                                            name="sayHi",
                                                            substack=[
                                                                return_value(
                                                                    OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                    value=join3(
                                                                        OPCODE="&operators::join (STRING1) (STRING2) (STRING3)",
                                                                        string1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="greeting"),
                                                                        string2=" ",
                                                                        string3=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="person"),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Call with only first arg (second uses default Hi)",
                                                    substack=[
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="sayHi", posargs='["Bob"]'),
                                                            b="Hi Bob",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Call with both args (overrides default)",
                                                    substack=[
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="sayHi", posargs='["Bob", "Hey"]'),
                                                            b="Hey Bob",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="return behavior",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Function returns early inside an if-block; later return must not run",
                                                    substack=[
                                                        configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["flag"]', argdefaults="[]"),
                                                        create_function_at(
                                                            OPCODE="&gceFuncsScopes::create function at var (NAME) {SUBSTACK}",
                                                            name="conditional",
                                                            substack=[
                                                                if_(
                                                                    OPCODE="&control::if <CONDITION> then {THEN}",
                                                                    condition=equals(
                                                                        OPCODE="&operators::(OPERAND1) = (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="flag"),
                                                                        operand2="yes",
                                                                    ),
                                                                    then=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="early"),
                                                                    ],
                                                                ),
                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="late"),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="When condition is true, early return fires",
                                                    substack=[
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="conditional", posargs='["yes"]'),
                                                            b="early",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="When condition is false, falls through to second return",
                                                    substack=[
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="conditional", posargs='["no"]'),
                                                            b="late",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="closures",
                                    substack=[
                                        run_with_separate_globals(
                                            OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                            substack=[
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Outer function accepts prefix, returns inner function that closes over it",
                                                    substack=[
                                                        configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["prefix"]', argdefaults="[]"),
                                                        create_function_at(
                                                            OPCODE="&gceFuncsScopes::create function at var (NAME) {SUBSTACK}",
                                                            name="makeGreeter",
                                                            substack=[
                                                                test_scope(
                                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                                    name="Configure inner function arg before defining it",
                                                                    substack=[
                                                                        configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["name"]', argdefaults="[]"),
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=create_function_named(
                                                                                OPCODE="&gceFuncsScopes::create function named (NAME) {SUBSTACK}",
                                                                                name="greeter",
                                                                                substack=[
                                                                                    return_value(
                                                                                        OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                                        value=join3(
                                                                                            OPCODE="&operators::join (STRING1) (STRING2) (STRING3)",
                                                                                            string1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="prefix"),
                                                                                            string2=", ",
                                                                                            string3=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="name"),
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
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Each call to makeGreeter produces an independent greeter",
                                                    substack=[
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="hiGreeter",
                                                            value=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="makeGreeter", posargs='["Hi"]'),
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="heyGreeter",
                                                            value=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="makeGreeter", posargs='["Hey"]'),
                                                        ),
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="hiGreeter", posargs='["Ada"]'),
                                                            b="Hi, Ada",
                                                        ),
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="heyGreeter", posargs='["Ada"]'),
                                                            b="Hey, Ada",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Captured prefix is independent per closure instance",
                                                    substack=[
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="hiGreeter", posargs='["Bob"]'),
                                                            b="Hi, Bob",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="create function named",
                                    substack=[
                                        run_with_separate_globals(
                                            OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                            substack=[
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Create a function as a reporter block (returns the function)",
                                                    substack=[
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="myFunc",
                                                            value=create_function_named(
                                                                OPCODE="&gceFuncsScopes::create function named (NAME) {SUBSTACK}",
                                                                name="anonFunc",
                                                                substack=[
                                                                    return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="from-anon"),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Call the stored function",
                                                    substack=[
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="myFunc", posargs="[]"),
                                                            b="from-anon",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="error: wrong arg count",
                                    substack=[
                                        run_with_separate_globals(
                                            OPCODE="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                                            substack=[
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Function that accepts no arguments",
                                                    substack=[
                                                        create_function_at(
                                                            OPCODE="&gceFuncsScopes::create function at var (NAME) {SUBSTACK}",
                                                            name="noArgs",
                                                            substack=[
                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="done"),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Calling with extra arguments should throw",
                                                    substack=[
                                                        assert_throws(
                                                            OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                            substack=[
                                                                execute_expression(
                                                                    OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                    expr=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="noArgs", posargs='["extra"]'),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Function that requires one argument",
                                                    substack=[
                                                        configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["required"]', argdefaults="[]"),
                                                        create_function_at(
                                                            OPCODE="&gceFuncsScopes::create function at var (NAME) {SUBSTACK}",
                                                            name="oneArg",
                                                            substack=[
                                                                return_value(
                                                                    OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                    value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="required"),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Calling with no arguments should throw",
                                                    substack=[
                                                        assert_throws(
                                                            OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                            substack=[
                                                                execute_expression(
                                                                    OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                    expr=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="oneArg", posargs="[]"),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="var scope inside function body",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="createVarScope inside a function is isolated per call",
                                                    substack=[
                                                        configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["val"]', argdefaults="[]"),
                                                        create_function_at(
                                                            OPCODE="&gceFuncsScopes::create function at var (NAME) {SUBSTACK}",
                                                            name="withScope",
                                                            substack=[
                                                                create_var_scope(
                                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                                    substack=[
                                                                        set_scope_var(
                                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                                            name="inner",
                                                                            value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="val"),
                                                                        ),
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="inner"),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="First call",
                                                    substack=[
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="withScope", posargs='["first"]'),
                                                            b="first",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Second call: inner var is fresh each call",
                                                    substack=[
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="withScope", posargs='["second"]'),
                                                            b="second",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Inner scope var is not visible outside the function",
                                                    substack=[
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=scope_var_exists(OPCODE="&gceFuncsScopes::var (NAME) exists in [KIND]?", name="inner", kind="all scopes"),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        test_scope(
                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                            name="Utilities Blocks",
                            substack=[
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="nothing",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Nothing is its own type",
                                            substack=[
                                                assert_(
                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                    condition=typeof_value_is_menu(
                                                        OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                        value=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                        type="Nothing (GCE)",
                                                    ),
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Nothing equals itself via string comparison",
                                            substack=[
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                    b=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Nothing is identical to itself (same singleton)",
                                            substack=[
                                                assert_(
                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                    condition=check_identity(
                                                        OPCODE="&gceFuncsScopes::(VALUE1) is (VALUE2) ?",
                                                        value1=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                        value2=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Nothing is not identical to any other value",
                                            substack=[
                                                assert_not(
                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                    condition=check_identity(
                                                        OPCODE="&gceFuncsScopes::(VALUE1) is (VALUE2) ?",
                                                        value1=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                        value2="0",
                                                    ),
                                                ),
                                                assert_not(
                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                    condition=check_identity(
                                                        OPCODE="&gceFuncsScopes::(VALUE1) is (VALUE2) ?",
                                                        value1=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                        value2="",
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="typeofValue",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Primitive types",
                                            substack=[
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=typeof_value(OPCODE="&gceFuncsScopes::typeof (VALUE)", value="hello"),
                                                    b=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="String"),
                                                ),
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=typeof_value(OPCODE="&gceFuncsScopes::typeof (VALUE)", value="42"),
                                                    b=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="Number"),
                                                ),
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=typeof_value(
                                                        OPCODE="&gceFuncsScopes::typeof (VALUE)",
                                                        value=true_boolean(OPCODE="&operators::true"),
                                                    ),
                                                    b=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="Boolean"),
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="GCE types",
                                            substack=[
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=typeof_value(
                                                        OPCODE="&gceFuncsScopes::typeof (VALUE)",
                                                        value=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                    ),
                                                    b=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="Nothing (GCE)"),
                                                ),
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=typeof_value(
                                                        OPCODE="&gceFuncsScopes::typeof (VALUE)",
                                                        value=create_function_named(
                                                            OPCODE="&gceFuncsScopes::create function named (NAME) {SUBSTACK}",
                                                            name="f",
                                                            substack=[
                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="x"),
                                                            ],
                                                        ),
                                                    ),
                                                    b=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="Function (GCE)"),
                                                ),
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=typeof_value(
                                                        OPCODE="&gceFuncsScopes::typeof (VALUE)",
                                                        value=create_class_named(OPCODE="&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}", name="MyClass", substack=[]),
                                                    ),
                                                    b=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="Class (GCE)"),
                                                ),
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=typeof_value(
                                                        OPCODE="&gceFuncsScopes::typeof (VALUE)",
                                                        value=create_instance(
                                                            OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)",
                                                            class_=create_class_named(OPCODE="&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}", name="MyClass", substack=[]),
                                                            posargs="[]",
                                                        ),
                                                    ),
                                                    b=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="Class Instance (GCE)"),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="typeofValueIsMenu",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Correct type returns true",
                                            substack=[
                                                assert_(
                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                    condition=typeof_value_is_menu(OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?", value="hello", type="String"),
                                                ),
                                                assert_(
                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                    condition=typeof_value_is_menu(OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?", value="42", type="Number"),
                                                ),
                                                assert_(
                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                    condition=typeof_value_is_menu(
                                                        OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                        value=true_boolean(OPCODE="&operators::true"),
                                                        type="Boolean",
                                                    ),
                                                ),
                                                assert_(
                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                    condition=typeof_value_is_menu(
                                                        OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                        value=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                        type="Nothing (GCE)",
                                                    ),
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Wrong type returns false",
                                            substack=[
                                                assert_not(
                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                    condition=typeof_value_is_menu(OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?", value="hello", type="Number"),
                                                ),
                                                assert_not(
                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                    condition=typeof_value_is_menu(OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?", value="42", type="String"),
                                                ),
                                                assert_not(
                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                    condition=typeof_value_is_menu(
                                                        OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                        value=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                        type="String",
                                                    ),
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="typeofValueIsMenu is consistent with typeofValue",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="fn",
                                                            value=create_function_named(
                                                                OPCODE="&gceFuncsScopes::create function named (NAME) {SUBSTACK}",
                                                                name="g",
                                                                substack=[
                                                                    return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="y"),
                                                                ],
                                                            ),
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=typeof_value_is_menu(
                                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                                value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="fn"),
                                                                type="Function (GCE)",
                                                            ),
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=typeof_value_is_menu(
                                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                                value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="fn"),
                                                                type="Class (GCE)",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="typeofValueSelection",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="The reporter returns the menu value as a string",
                                            substack=[
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="String"),
                                                    b="String",
                                                ),
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="Nothing (GCE)"),
                                                    b="Nothing (GCE)",
                                                ),
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="Function (GCE)"),
                                                    b="Function (GCE)",
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Result matches typeofValue output",
                                            substack=[
                                                assert_(
                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                    condition=equals(
                                                        OPCODE="&operators::(OPERAND1) = (OPERAND2)",
                                                        operand1=typeof_value(
                                                            OPCODE="&gceFuncsScopes::typeof (VALUE)",
                                                            value=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                        ),
                                                        operand2=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="Nothing (GCE)"),
                                                    ),
                                                ),
                                                assert_(
                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                    condition=equals(
                                                        OPCODE="&operators::(OPERAND1) = (OPERAND2)",
                                                        operand1=typeof_value(OPCODE="&gceFuncsScopes::typeof (VALUE)", value="test"),
                                                        operand2=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="String"),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="objectAsString",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Primitive values stringify as-is",
                                            substack=[
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=object_as_string(OPCODE="&gceFuncsScopes::(VALUE) as string", value="hello"),
                                                    b="hello",
                                                ),
                                                assert_unstrict_equal(
                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                    a=object_as_string(OPCODE="&gceFuncsScopes::(VALUE) as string", value="42"),
                                                    b="42",
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Nothing stringifies to its representation",
                                            substack=[
                                                assert_does_not_throw(
                                                    OPCODE="&gceTestRunner::assert does not throw error {SUBSTACK}",
                                                    substack=[
                                                        execute_expression(
                                                            OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                            expr=object_as_string(
                                                                OPCODE="&gceFuncsScopes::(VALUE) as string",
                                                                value=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Instance without as-string method: no error, returns some string",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Plain", substack=[]),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="inst",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Plain", posargs="[]"),
                                                        ),
                                                        assert_does_not_throw(
                                                            OPCODE="&gceTestRunner::assert does not throw error {SUBSTACK}",
                                                            substack=[
                                                                execute_expression(
                                                                    OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                    expr=object_as_string(
                                                                        OPCODE="&gceFuncsScopes::(VALUE) as string",
                                                                        value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="inst"),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=typeof_value_is_menu(
                                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                                value=object_as_string(
                                                                    OPCODE="&gceFuncsScopes::(VALUE) as string",
                                                                    value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="inst"),
                                                                ),
                                                                type="String",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Instance WITH as-string method: calls the method",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="Stringable",
                                                            substack=[
                                                                define_special_method(
                                                                    OPCODE="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
                                                                    special_method="as string",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="custom-string"),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="inst",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Stringable", posargs="[]"),
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=object_as_string(
                                                                OPCODE="&gceFuncsScopes::(VALUE) as string",
                                                                value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="inst"),
                                                            ),
                                                            b="custom-string",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="checkIdentity",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Two separate instances of the same class are NOT identical",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="MyClass", substack=[]),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="a",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="MyClass", posargs="[]"),
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="b",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="MyClass", posargs="[]"),
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=check_identity(
                                                                OPCODE="&gceFuncsScopes::(VALUE1) is (VALUE2) ?",
                                                                value1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                value2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b"),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="The same instance stored in two variables IS identical",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="MyClass", substack=[]),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="a",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="MyClass", posargs="[]"),
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="b",
                                                            value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=check_identity(
                                                                OPCODE="&gceFuncsScopes::(VALUE1) is (VALUE2) ?",
                                                                value1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                value2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b"),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Nothing is identical to itself",
                                            substack=[
                                                assert_(
                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                    condition=check_identity(
                                                        OPCODE="&gceFuncsScopes::(VALUE1) is (VALUE2) ?",
                                                        value1=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                        value2=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Nothing is not identical to a function",
                                            substack=[
                                                assert_not(
                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                    condition=check_identity(
                                                        OPCODE="&gceFuncsScopes::(VALUE1) is (VALUE2) ?",
                                                        value1=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                        value2=create_function_named(
                                                            OPCODE="&gceFuncsScopes::create function named (NAME) {SUBSTACK}",
                                                            name="h",
                                                            substack=[
                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="z"),
                                                            ],
                                                        ),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Two separately created functions are NOT identical",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="f1",
                                                            value=create_function_named(
                                                                OPCODE="&gceFuncsScopes::create function named (NAME) {SUBSTACK}",
                                                                name="fn1",
                                                                substack=[
                                                                    return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="r"),
                                                                ],
                                                            ),
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="f2",
                                                            value=create_function_named(
                                                                OPCODE="&gceFuncsScopes::create function named (NAME) {SUBSTACK}",
                                                                name="fn2",
                                                                substack=[
                                                                    return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="r"),
                                                                ],
                                                            ),
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=check_identity(
                                                                OPCODE="&gceFuncsScopes::(VALUE1) is (VALUE2) ?",
                                                                value1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="f1"),
                                                                value2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="f2"),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Primitive strings identical",
                                            substack=[
                                                assert_(
                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                    condition=check_identity(OPCODE="&gceFuncsScopes::(VALUE1) is (VALUE2) ?", value1="hello", value2="hello"),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="executeExpression",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Evaluate a reporter block as a command (no error)",
                                            substack=[
                                                assert_does_not_throw(
                                                    OPCODE="&gceTestRunner::assert does not throw error {SUBSTACK}",
                                                    substack=[
                                                        execute_expression(
                                                            OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                            expr=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="executeExpression propagates errors from its subexpression",
                                            substack=[
                                                assert_throws(
                                                    OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                    substack=[
                                                        execute_expression(
                                                            OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                            expr=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="__missing__"),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="executeExpression can evaluate any reporter",
                                            substack=[
                                                assert_does_not_throw(
                                                    OPCODE="&gceTestRunner::assert does not throw error {SUBSTACK}",
                                                    substack=[
                                                        execute_expression(
                                                            OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                            expr=typeof_value(OPCODE="&gceFuncsScopes::typeof (VALUE)", value="test"),
                                                        ),
                                                    ],
                                                ),
                                                assert_does_not_throw(
                                                    OPCODE="&gceTestRunner::assert does not throw error {SUBSTACK}",
                                                    substack=[
                                                        execute_expression(
                                                            OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                            expr=object_as_string(OPCODE="&gceFuncsScopes::(VALUE) as string", value="hello"),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="executeExpression can call a function and discard the return value",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_function_at(
                                                            OPCODE="&gceFuncsScopes::create function at var (NAME) {SUBSTACK}",
                                                            name="noopFn",
                                                            substack=[
                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="done"),
                                                            ],
                                                        ),
                                                        assert_does_not_throw(
                                                            OPCODE="&gceTestRunner::assert does not throw error {SUBSTACK}",
                                                            substack=[
                                                                execute_expression(
                                                                    OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                    expr=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="noopFn", posargs="[]"),
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
                        test_scope(
                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                            name="Class Definition and Inheritance Blocks",
                            substack=[
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="createClassAt",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Class is accessible by name and typeof is Class (GCE)",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="MyClass", substack=[]),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=typeof_value(
                                                                OPCODE="&gceFuncsScopes::typeof (VALUE)",
                                                                value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="MyClass"),
                                                            ),
                                                            b=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="Class (GCE)"),
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Can create an instance immediately",
                                                            substack=[
                                                                set_scope_var(
                                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                                    name="inst",
                                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="MyClass", posargs="[]"),
                                                                ),
                                                                assert_(
                                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                                    condition=typeof_value_is_menu(
                                                                        OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                                        value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="inst"),
                                                                        type="Class Instance (GCE)",
                                                                    ),
                                                                ),
                                                                assert_(
                                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                                    condition=is_instance(
                                                                        OPCODE="&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?",
                                                                        potential_instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="inst"),
                                                                        class_="MyClass",
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Class with methods and init defined inline",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="Counter",
                                                            substack=[
                                                                configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["start"]', argdefaults='["0"]'),
                                                                define_special_method(
                                                                    OPCODE="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
                                                                    special_method="init",
                                                                    substack=[
                                                                        set_attribute(
                                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                                            instance=self_value(OPCODE="&gceOOP::self"),
                                                                            name="count",
                                                                            value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="start"),
                                                                        ),
                                                                    ],
                                                                ),
                                                                define_instance_method(
                                                                    OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                                    name="value",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=get_attribute(
                                                                                OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                                name="count",
                                                                                instance=self_value(OPCODE="&gceOOP::self"),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="c",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Counter", posargs='["5"]'),
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_method(
                                                                OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                                name="value",
                                                                posargs="[]",
                                                            ),
                                                            b="5",
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Default arg: no args uses default 0",
                                                            substack=[
                                                                set_scope_var(
                                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                                    name="d",
                                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Counter", posargs="[]"),
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=call_method(
                                                                        OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="d"),
                                                                        name="value",
                                                                        posargs="[]",
                                                                    ),
                                                                    b="0",
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="createClassNamed (reporter)",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Create class inline as a reporter value, store and use it",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="Dyn",
                                                            value=create_class_named(
                                                                OPCODE="&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}",
                                                                name="DynClass",
                                                                substack=[
                                                                    define_instance_method(
                                                                        OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                                        name="ping",
                                                                        substack=[
                                                                            return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="pong"),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Stored value is a Class (GCE)",
                                                            substack=[
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=typeof_value(
                                                                        OPCODE="&gceFuncsScopes::typeof (VALUE)",
                                                                        value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="Dyn"),
                                                                    ),
                                                                    b=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="Class (GCE)"),
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Class can be instantiated",
                                                            substack=[
                                                                set_scope_var(
                                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                                    name="inst",
                                                                    value=create_instance(
                                                                        OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)",
                                                                        class_=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="Dyn"),
                                                                        posargs="[]",
                                                                    ),
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=call_method(
                                                                        OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="inst"),
                                                                        name="ping",
                                                                        posargs="[]",
                                                                    ),
                                                                    b="pong",
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="currentClass",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="currentClass inside createClassAt returns the class being defined",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="Stamped",
                                                            substack=[
                                                                set_class_variable(
                                                                    OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                                    class_=current_class(OPCODE="&gceOOP::current class"),
                                                                    name="tag",
                                                                    value="stamped-value",
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Class variable set via currentClass is accessible by name",
                                                            substack=[
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_class_variable(OPCODE="&gceOOP::on (CLASS) get class var (NAME)", name="tag", class_="Stamped"),
                                                                    b="stamped-value",
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="currentClass inside createClassNamed also works",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="NC",
                                                            value=create_class_named(
                                                                OPCODE="&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}",
                                                                name="NamedCls",
                                                                substack=[
                                                                    set_class_variable(
                                                                        OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                                        class_=current_class(OPCODE="&gceOOP::current class"),
                                                                        name="info",
                                                                        value="from-named",
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=get_class_variable(
                                                                OPCODE="&gceOOP::on (CLASS) get class var (NAME)",
                                                                name="info",
                                                                class_=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="NC"),
                                                            ),
                                                            b="from-named",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="currentClass inside onClass returns the correct class",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Extendable", substack=[]),
                                                        on_class(
                                                            OPCODE="&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}",
                                                            class_="Extendable",
                                                            substack=[
                                                                set_class_variable(
                                                                    OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                                    class_=current_class(OPCODE="&gceOOP::current class"),
                                                                    name="addedTag",
                                                                    value="via-on-class",
                                                                ),
                                                            ],
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=get_class_variable(OPCODE="&gceOOP::on (CLASS) get class var (NAME)", name="addedTag", class_="Extendable"),
                                                            b="via-on-class",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="createSubclassAt",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(
                                                    OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                    name="Animal",
                                                    substack=[
                                                        define_instance_method(
                                                            OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="breathe",
                                                            substack=[
                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="breathing"),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                create_subclass_at(
                                                    OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                    name="Dog",
                                                    superclass="Animal",
                                                    substack=[
                                                        define_instance_method(
                                                            OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="bark",
                                                            substack=[
                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="woof"),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="isSubclass reflects the relationship",
                                                    substack=[
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_subclass(OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?", subclass="Dog", superclass="Animal"),
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=is_subclass(OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?", subclass="Animal", superclass="Dog"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="getSuperclass of Dog is Animal",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="Animal",
                                                            value=get_superclass(OPCODE="&gceOOP::get superclass of (CLASS)", class_="Dog"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Dog instance can call both inherited and own methods",
                                                    substack=[
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="d",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Dog", posargs="[]"),
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_method(
                                                                OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="d"),
                                                                name="breathe",
                                                                posargs="[]",
                                                            ),
                                                            b="breathing",
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_method(
                                                                OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="d"),
                                                                name="bark",
                                                                posargs="[]",
                                                            ),
                                                            b="woof",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="currentClass inside subclass body returns the subclass",
                                                    substack=[
                                                        create_subclass_at(
                                                            OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                            name="Puppy",
                                                            superclass="Dog",
                                                            substack=[
                                                                set_class_variable(
                                                                    OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                                    class_=current_class(OPCODE="&gceOOP::current class"),
                                                                    name="size",
                                                                    value="small",
                                                                ),
                                                            ],
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=get_class_variable(OPCODE="&gceOOP::on (CLASS) get class var (NAME)", name="size", class_="Puppy"),
                                                            b="small",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="isSubclass is transitive",
                                                    substack=[
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_subclass(OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?", subclass="Puppy", superclass="Animal"),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="createSubclassNamed (reporter)",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(
                                                    OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                    name="BaseR",
                                                    substack=[
                                                        define_instance_method(
                                                            OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="base",
                                                            substack=[
                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="from-base"),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="Sub",
                                                    value=create_subclass_named(
                                                        OPCODE="&gceOOP::create subclass named (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                        name="SubNamed",
                                                        superclass="BaseR",
                                                        substack=[
                                                            define_instance_method(
                                                                OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                                name="child",
                                                                substack=[
                                                                    return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="from-child"),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Stored value is a Class (GCE)",
                                                    substack=[
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=typeof_value(
                                                                OPCODE="&gceFuncsScopes::typeof (VALUE)",
                                                                value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="Sub"),
                                                            ),
                                                            b=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="Class (GCE)"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="isSubclass works for reporter-created subclass",
                                                    substack=[
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_subclass(
                                                                OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?",
                                                                subclass=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="Sub"),
                                                                superclass="BaseR",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Instance inherits from base and has own method",
                                                    substack=[
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="inst",
                                                            value=create_instance(
                                                                OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)",
                                                                class_=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="Sub"),
                                                                posargs="[]",
                                                            ),
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_method(
                                                                OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="inst"),
                                                                name="base",
                                                                posargs="[]",
                                                            ),
                                                            b="from-base",
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_method(
                                                                OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="inst"),
                                                                name="child",
                                                                posargs="[]",
                                                            ),
                                                            b="from-child",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="isSubclass",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="A", substack=[]),
                                                create_subclass_at(
                                                    OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                    name="B",
                                                    superclass="A",
                                                    substack=[],
                                                ),
                                                create_subclass_at(
                                                    OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                    name="C",
                                                    superclass="B",
                                                    substack=[],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Direct and transitive subclass",
                                                    substack=[
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_subclass(OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?", subclass="B", superclass="A"),
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_subclass(OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?", subclass="C", superclass="A"),
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_subclass(OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?", subclass="C", superclass="B"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Reverse is false",
                                                    substack=[
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=is_subclass(OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?", subclass="A", superclass="B"),
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=is_subclass(OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?", subclass="A", superclass="C"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="A class is kinda a subclass of itself",
                                                    substack=[
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_subclass(OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?", subclass="A", superclass="A"),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="getSuperclass",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Root", substack=[]),
                                                create_subclass_at(
                                                    OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                    name="Branch",
                                                    superclass="Root",
                                                    substack=[],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Superclass of Branch is Root",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="Root",
                                                            value=get_superclass(OPCODE="&gceOOP::get superclass of (CLASS)", class_="Branch"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Root's superclass is the built-in Superclass",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="Superclass",
                                                            value=get_superclass(OPCODE="&gceOOP::get superclass of (CLASS)", class_="Root"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Superclass of the built-in Superclass is Nothing",
                                                    substack=[
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=typeof_value_is_menu(
                                                                OPCODE="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                                                                value=get_superclass(
                                                                    OPCODE="&gceOOP::get superclass of (CLASS)",
                                                                    class_=get_superclass(OPCODE="&gceOOP::get superclass of (CLASS)", class_="Root"),
                                                                ),
                                                                type="Nothing (GCE)",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Missing class throws",
                                                    substack=[
                                                        assert_throws(
                                                            OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                            substack=[
                                                                execute_expression(
                                                                    OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                    expr=get_superclass(OPCODE="&gceOOP::get superclass of (CLASS)", class_="__no_such_class__"),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="onClass: add instance method",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Define class with no methods, then add one via onClass",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Greeter", substack=[]),
                                                        on_class(
                                                            OPCODE="&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}",
                                                            class_="Greeter",
                                                            substack=[
                                                                configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["name"]', argdefaults="[]"),
                                                                define_instance_method(
                                                                    OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                                    name="hello",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=join(
                                                                                OPCODE="&operators::join (STRING1) (STRING2)",
                                                                                string1="Hello, ",
                                                                                string2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="name"),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="g",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Greeter", posargs="[]"),
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Method added via onClass is callable",
                                                            substack=[
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=call_method(
                                                                        OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="g"),
                                                                        name="hello",
                                                                        posargs='["World"]',
                                                                    ),
                                                                    b="Hello, World",
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="onClass: add static method",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Util", substack=[]),
                                                on_class(
                                                    OPCODE="&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}",
                                                    class_="Util",
                                                    substack=[
                                                        configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["x"]', argdefaults="[]"),
                                                        define_static_method(
                                                            OPCODE="&gceOOP::define static method (NAME) {SUBSTACK}",
                                                            name="double",
                                                            substack=[
                                                                return_value(
                                                                    OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                    value=multiply(
                                                                        OPCODE="&operators::(OPERAND1) * (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="x"),
                                                                        operand2="2",
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Static method added via onClass is callable",
                                                    substack=[
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_static_method(
                                                                OPCODE="&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)",
                                                                class_="Util",
                                                                name="double",
                                                                posargs='["7"]',
                                                            ),
                                                            b="14",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="onClass: currentClass inside body",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="currentClass used inside onClass body sets a class variable",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Tagged", substack=[]),
                                                        on_class(
                                                            OPCODE="&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}",
                                                            class_="Tagged",
                                                            substack=[
                                                                set_class_variable(
                                                                    OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                                    class_=current_class(OPCODE="&gceOOP::current class"),
                                                                    name="source",
                                                                    value="on-class",
                                                                ),
                                                            ],
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=get_class_variable(OPCODE="&gceOOP::on (CLASS) get class var (NAME)", name="source", class_="Tagged"),
                                                            b="on-class",
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Multiple onClass calls accumulate class variables",
                                                            substack=[
                                                                on_class(
                                                                    OPCODE="&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}",
                                                                    class_="Tagged",
                                                                    substack=[
                                                                        set_class_variable(
                                                                            OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                                            class_=current_class(OPCODE="&gceOOP::current class"),
                                                                            name="extra",
                                                                            value="second",
                                                                        ),
                                                                    ],
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_class_variable(OPCODE="&gceOOP::on (CLASS) get class var (NAME)", name="source", class_="Tagged"),
                                                                    b="on-class",
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_class_variable(OPCODE="&gceOOP::on (CLASS) get class var (NAME)", name="extra", class_="Tagged"),
                                                                    b="second",
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="onClass: visible in propertyNamesOfClass",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Method added via onClass appears in property list",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Widget", substack=[]),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="No methods yet",
                                                            substack=[
                                                                assert_text_not_in_value(
                                                                    OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                                    text="render",
                                                                    value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="instance method", class_="Widget"),
                                                                ),
                                                                on_class(
                                                                    OPCODE="&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}",
                                                                    class_="Widget",
                                                                    substack=[
                                                                        define_instance_method(
                                                                            OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                                            name="render",
                                                                            substack=[
                                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="rendered"),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Method now listed after onClass",
                                                            substack=[
                                                                assert_text_in_value(
                                                                    OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                                    text="render",
                                                                    value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="instance method", class_="Widget"),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="onClass: cleanup on error",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="class def scope cleanup runs even when body throws",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Safe", substack=[]),
                                                        assert_throws(
                                                            OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                            substack=[
                                                                on_class(
                                                                    OPCODE="&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}",
                                                                    class_="Safe",
                                                                    substack=[
                                                                        execute_expression(
                                                                            OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                            expr=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="__missing__"),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="After the error, onClass on same class still works",
                                                            substack=[
                                                                assert_does_not_throw(
                                                                    OPCODE="&gceTestRunner::assert does not throw error {SUBSTACK}",
                                                                    substack=[
                                                                        on_class(
                                                                            OPCODE="&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}",
                                                                            class_="Safe",
                                                                            substack=[
                                                                                define_instance_method(
                                                                                    OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                                                    name="ok",
                                                                                    substack=[
                                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="ok"),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=call_method(
                                                                        OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                        instance=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Safe", posargs="[]"),
                                                                        name="ok",
                                                                        posargs="[]",
                                                                    ),
                                                                    b="ok",
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
                        test_scope(
                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                            name="Instance Methods",
                            substack=[
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="basic method call",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Define class with methods, call them on an instance",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="Greeter",
                                                            substack=[
                                                                configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["name"]', argdefaults="[]"),
                                                                define_instance_method(
                                                                    OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                                    name="greet",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=join3(
                                                                                OPCODE="&operators::join (STRING1) (STRING2) (STRING3)",
                                                                                string1="Hello, ",
                                                                                string2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="name"),
                                                                                string3="!",
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                define_instance_method(
                                                                    OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                                    name="getType",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=typeof_value(
                                                                                OPCODE="&gceFuncsScopes::typeof (VALUE)",
                                                                                value=self_value(OPCODE="&gceOOP::self"),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                define_instance_method(
                                                                    OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                                    name="getAttr",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=get_attribute(
                                                                                OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                                name="label",
                                                                                instance=self_value(OPCODE="&gceOOP::self"),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="g",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Greeter", posargs="[]"),
                                                        ),
                                                        set_attribute(
                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                            instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="g"),
                                                            name="label",
                                                            value="test-label",
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Method with arg",
                                                            substack=[
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=call_method(
                                                                        OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="g"),
                                                                        name="greet",
                                                                        posargs='["World"]',
                                                                    ),
                                                                    b="Hello, World!",
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Same method with different arg",
                                                            substack=[
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=call_method(
                                                                        OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="g"),
                                                                        name="greet",
                                                                        posargs='["Alice"]',
                                                                    ),
                                                                    b="Hello, Alice!",
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="No-arg method returns correct type string",
                                                            substack=[
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=call_method(
                                                                        OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="g"),
                                                                        name="getType",
                                                                        posargs="[]",
                                                                    ),
                                                                    b=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="Class Instance (GCE)"),
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Method reads self attribute",
                                                            substack=[
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=call_method(
                                                                        OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="g"),
                                                                        name="getAttr",
                                                                        posargs="[]",
                                                                    ),
                                                                    b="test-label",
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="self is the correct instance",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Two instances with different attribute values",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="Box",
                                                            substack=[
                                                                define_instance_method(
                                                                    OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                                    name="describe",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=join(
                                                                                OPCODE="&operators::join (STRING1) (STRING2)",
                                                                                string1="Box-",
                                                                                string2=get_attribute(
                                                                                    OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                                    name="id",
                                                                                    instance=self_value(OPCODE="&gceOOP::self"),
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="b1",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Box", posargs="[]"),
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="b2",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Box", posargs="[]"),
                                                        ),
                                                        set_attribute(
                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                            instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b1"),
                                                            name="id",
                                                            value="AAA",
                                                        ),
                                                        set_attribute(
                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                            instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b2"),
                                                            name="id",
                                                            value="BBB",
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_method(
                                                                OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b1"),
                                                                name="describe",
                                                                posargs="[]",
                                                            ),
                                                            b="Box-AAA",
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_method(
                                                                OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b2"),
                                                                name="describe",
                                                                posargs="[]",
                                                            ),
                                                            b="Box-BBB",
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="self is distinct for each instance",
                                                            substack=[
                                                                assert_not(
                                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                    condition=check_identity(
                                                                        OPCODE="&gceFuncsScopes::(VALUE1) is (VALUE2) ?",
                                                                        value1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b1"),
                                                                        value2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b2"),
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
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="error cases",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Calling an undefined method throws",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Empty", substack=[]),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="e",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Empty", posargs="[]"),
                                                        ),
                                                        assert_throws(
                                                            OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                            substack=[
                                                                execute_expression(
                                                                    OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                    expr=call_method(
                                                                        OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="e"),
                                                                        name="nonExistent",
                                                                        posargs="[]",
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Calling a method on a non-instance throws",
                                            substack=[
                                                assert_throws(
                                                    OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                    substack=[
                                                        execute_expression(
                                                            OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                            expr=call_method(
                                                                OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                instance="not-an-instance",
                                                                name="anyMethod",
                                                                posargs="[]",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="method with yield point",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Method body that includes sayforsecs (yielding block) returns correctly and waits",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="Speaker",
                                                            substack=[
                                                                configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["msg"]', argdefaults="[]"),
                                                                define_instance_method(
                                                                    OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                                    name="speak",
                                                                    substack=[
                                                                        sayforsecs(
                                                                            OPCODE="&looks::say (MESSAGE) for (SECONDS) seconds",
                                                                            message=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="msg"),
                                                                            seconds="0.5",
                                                                        ),
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=join(
                                                                                OPCODE="&operators::join (STRING1) (STRING2)",
                                                                                string1="said: ",
                                                                                string2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="msg"),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="s",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Speaker", posargs="[]"),
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Return value is correct after yield",
                                                            substack=[
                                                                resettimer(OPCODE="&sensing::reset timer"),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=call_method(
                                                                        OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="s"),
                                                                        name="speak",
                                                                        posargs='["hello"]',
                                                                    ),
                                                                    b="said: hello",
                                                                ),
                                                                test_scope(
                                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                                    name="At least 0.4s elapsed (sayforsecs 0.5s actually waited)",
                                                                    substack=[
                                                                        assert_(
                                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                                            condition=gt(
                                                                                OPCODE="&operators::(OPERAND1) > (OPERAND2)",
                                                                                operand1=timer(OPCODE="&sensing::timer"),
                                                                                operand2="0.4",
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Second call also returns correctly and also waits",
                                                            substack=[
                                                                resettimer(OPCODE="&sensing::reset timer"),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=call_method(
                                                                        OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="s"),
                                                                        name="speak",
                                                                        posargs='["world"]',
                                                                    ),
                                                                    b="said: world",
                                                                ),
                                                                test_scope(
                                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                                    name="At least 0.4s elapsed on second call too",
                                                                    substack=[
                                                                        assert_(
                                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                                            condition=gt(
                                                                                OPCODE="&operators::(OPERAND1) > (OPERAND2)",
                                                                                operand1=timer(OPCODE="&sensing::timer"),
                                                                                operand2="0.4",
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
                        test_scope(
                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                            name="Special Method: init",
                            substack=[
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="init sets attributes from args",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Define class whose init sets x and y from positional args",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="Point",
                                                            substack=[
                                                                configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["x","y"]', argdefaults="[]"),
                                                                define_special_method(
                                                                    OPCODE="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
                                                                    special_method="init",
                                                                    substack=[
                                                                        set_attribute(
                                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                                            instance=self_value(OPCODE="&gceOOP::self"),
                                                                            name="x",
                                                                            value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="x"),
                                                                        ),
                                                                        set_attribute(
                                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                                            instance=self_value(OPCODE="&gceOOP::self"),
                                                                            name="y",
                                                                            value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="y"),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="p",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Point", posargs='["3","4"]'),
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=get_attribute(
                                                                OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                name="x",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="p"),
                                                            ),
                                                            b="3",
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=get_attribute(
                                                                OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                name="y",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="p"),
                                                            ),
                                                            b="4",
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Second instance has independent values",
                                                            substack=[
                                                                set_scope_var(
                                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                                    name="q",
                                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Point", posargs='["10","20"]'),
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="x",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="q"),
                                                                    ),
                                                                    b="10",
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="y",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="q"),
                                                                    ),
                                                                    b="20",
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="First instance unchanged after second is created",
                                                            substack=[
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="x",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="p"),
                                                                    ),
                                                                    b="3",
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="init with default args",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Defaults fill in when args omitted",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="Color",
                                                            substack=[
                                                                configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["r","g","b"]', argdefaults='["0","0","0"]'),
                                                                define_special_method(
                                                                    OPCODE="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
                                                                    special_method="init",
                                                                    substack=[
                                                                        set_attribute(
                                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                                            instance=self_value(OPCODE="&gceOOP::self"),
                                                                            name="r",
                                                                            value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="r"),
                                                                        ),
                                                                        set_attribute(
                                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                                            instance=self_value(OPCODE="&gceOOP::self"),
                                                                            name="g",
                                                                            value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="g"),
                                                                        ),
                                                                        set_attribute(
                                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                                            instance=self_value(OPCODE="&gceOOP::self"),
                                                                            name="b",
                                                                            value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b"),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="All defaults: r=0, g=0, b=0",
                                                            substack=[
                                                                set_scope_var(
                                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                                    name="black",
                                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Color", posargs="[]"),
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="r",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="black"),
                                                                    ),
                                                                    b="0",
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="g",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="black"),
                                                                    ),
                                                                    b="0",
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="b",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="black"),
                                                                    ),
                                                                    b="0",
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Partial override: r=255",
                                                            substack=[
                                                                set_scope_var(
                                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                                    name="red",
                                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Color", posargs='["255"]'),
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="r",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="red"),
                                                                    ),
                                                                    b="255",
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="g",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="red"),
                                                                    ),
                                                                    b="0",
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Full args",
                                                            substack=[
                                                                set_scope_var(
                                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                                    name="custom",
                                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Color", posargs='["10","20","30"]'),
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="b",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="custom"),
                                                                    ),
                                                                    b="30",
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="subclass init calls super init",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Subclass init calls callSuperInitMethod",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="Shape",
                                                            substack=[
                                                                configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["color"]', argdefaults="[]"),
                                                                define_special_method(
                                                                    OPCODE="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
                                                                    special_method="init",
                                                                    substack=[
                                                                        set_attribute(
                                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                                            instance=self_value(OPCODE="&gceOOP::self"),
                                                                            name="color",
                                                                            value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="color"),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        create_subclass_at(
                                                            OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                            name="Circle",
                                                            superclass="Shape",
                                                            substack=[
                                                                configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["radius","color"]', argdefaults="[]"),
                                                                define_special_method(
                                                                    OPCODE="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
                                                                    special_method="init",
                                                                    substack=[
                                                                        execute_expression(
                                                                            OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                            expr=call_super_init_method(OPCODE="&gceOOP::call super init method with positional args (POSARGS)", posargs='["blue"]'),
                                                                        ),
                                                                        set_attribute(
                                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                                            instance=self_value(OPCODE="&gceOOP::self"),
                                                                            name="radius",
                                                                            value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="radius"),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="c",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Circle", posargs='["5","ignored"]'),
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="radius set by Circle init",
                                                            substack=[
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="radius",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                                    ),
                                                                    b="5",
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="color set by super (Shape) init with hardcoded value",
                                                            substack=[
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="color",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                                    ),
                                                                    b="blue",
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
                        test_scope(
                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                            name="Inheritance and Super",
                            substack=[
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="isSubclass",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="A", substack=[]),
                                                create_subclass_at(
                                                    OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                    name="B",
                                                    superclass="A",
                                                    substack=[],
                                                ),
                                                create_subclass_at(
                                                    OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                    name="C",
                                                    superclass="B",
                                                    substack=[],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Direct subclass",
                                                    substack=[
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_subclass(OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?", subclass="B", superclass="A"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Transitive subclass",
                                                    substack=[
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_subclass(OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?", subclass="C", superclass="A"),
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_subclass(OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?", subclass="C", superclass="B"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Reverse is false",
                                                    substack=[
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=is_subclass(OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?", subclass="A", superclass="B"),
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=is_subclass(OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?", subclass="A", superclass="C"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="A class is a subclass of itself",
                                                    substack=[
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_subclass(OPCODE="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?", subclass="A", superclass="A"),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="isInstance with inheritance",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Vehicle", substack=[]),
                                                create_subclass_at(
                                                    OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                    name="Car",
                                                    superclass="Vehicle",
                                                    substack=[],
                                                ),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="v",
                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Vehicle", posargs="[]"),
                                                ),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="c",
                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Car", posargs="[]"),
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Instance is instance of own class",
                                                    substack=[
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_instance(
                                                                OPCODE="&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?",
                                                                potential_instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="v"),
                                                                class_="Vehicle",
                                                            ),
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_instance(
                                                                OPCODE="&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?",
                                                                potential_instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                                class_="Car",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Subclass instance is instance of superclass",
                                                    substack=[
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_instance(
                                                                OPCODE="&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?",
                                                                potential_instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                                class_="Vehicle",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Superclass instance is NOT instance of subclass",
                                                    substack=[
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=is_instance(
                                                                OPCODE="&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?",
                                                                potential_instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="v"),
                                                                class_="Car",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="method override and super",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(
                                                    OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                    name="Animal",
                                                    substack=[
                                                        define_instance_method(
                                                            OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="speak",
                                                            substack=[
                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="generic sound"),
                                                            ],
                                                        ),
                                                        define_instance_method(
                                                            OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="breathe",
                                                            substack=[
                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="breathing"),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                create_subclass_at(
                                                    OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                    name="Dog",
                                                    superclass="Animal",
                                                    substack=[
                                                        define_instance_method(
                                                            OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="speak",
                                                            substack=[
                                                                return_value(
                                                                    OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                    value=join(
                                                                        OPCODE="&operators::join (STRING1) (STRING2)",
                                                                        string1=call_super_method(OPCODE="&gceOOP::call super method (NAME) with positional args (POSARGS)", name="speak", posargs="[]"),
                                                                        string2=" (but louder)",
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="a",
                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Animal", posargs="[]"),
                                                ),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="d",
                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Dog", posargs="[]"),
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Overridden method returns augmented result",
                                                    substack=[
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_method(
                                                                OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="d"),
                                                                name="speak",
                                                                posargs="[]",
                                                            ),
                                                            b="generic sound (but louder)",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Parent method still returns original",
                                                    substack=[
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_method(
                                                                OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                name="speak",
                                                                posargs="[]",
                                                            ),
                                                            b="generic sound",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Inherited (non-overridden) method works on subclass",
                                                    substack=[
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_method(
                                                                OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="d"),
                                                                name="breathe",
                                                                posargs="[]",
                                                            ),
                                                            b="breathing",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="getSuperclass",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Base", substack=[]),
                                                create_subclass_at(
                                                    OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                    name="Child",
                                                    superclass="Base",
                                                    substack=[],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Superclass of Child is Base",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="Base",
                                                            value=get_superclass(OPCODE="&gceOOP::get superclass of (CLASS)", class_="Child"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Superclass of Base is built-in Superclass",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="Superclass",
                                                            value=get_superclass(OPCODE="&gceOOP::get superclass of (CLASS)", class_="Base"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="getSuperclass on a missing class name throws",
                                                    substack=[
                                                        assert_throws(
                                                            OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                            substack=[
                                                                execute_expression(
                                                                    OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                    expr=get_superclass(OPCODE="&gceOOP::get superclass of (CLASS)", class_="__no_such_class__"),
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
                        test_scope(
                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                            name="Getters and Setters",
                            substack=[
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="setter transforms and stores, getter retrieves",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Setter prepends 'set:'; getter appends ':get'",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="Box",
                                                            substack=[
                                                                define_setter(
                                                                    OPCODE="&gceOOP::define setter for (NAME) {:SHADOW1:} {:SHADOW2:} {SUBSTACK}",
                                                                    name="size",
                                                                    substack=[
                                                                        set_attribute(
                                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                                            instance=self_value(OPCODE="&gceOOP::self"),
                                                                            name="_size",
                                                                            value=join(
                                                                                OPCODE="&operators::join (STRING1) (STRING2)",
                                                                                string1="set:",
                                                                                string2=define_setter_value(OPCODE="&gceOOP::operator value {{id=gceOOP_defineSetterValue}}"),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                define_getter(
                                                                    OPCODE="&gceOOP::define getter for (NAME) {:SHADOW:} {SUBSTACK}",
                                                                    name="size",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=join(
                                                                                OPCODE="&operators::join (STRING1) (STRING2)",
                                                                                string1=get_attribute(
                                                                                    OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                                    name="_size",
                                                                                    instance=self_value(OPCODE="&gceOOP::self"),
                                                                                ),
                                                                                string2=":get",
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="b",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Box", posargs="[]"),
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="setAttribute goes through setter",
                                                            substack=[
                                                                set_attribute(
                                                                    OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                                    instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b"),
                                                                    name="size",
                                                                    value="42",
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Raw _size attribute reflects setter transformation",
                                                            substack=[
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="_size",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b"),
                                                                    ),
                                                                    b="set:42",
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="getAttribute goes through getter",
                                                            substack=[
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="size",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b"),
                                                                    ),
                                                                    b="set:42:get",
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Update via setter replaces stored value",
                                                            substack=[
                                                                set_attribute(
                                                                    OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                                    instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b"),
                                                                    name="size",
                                                                    value="hello",
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="_size",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b"),
                                                                    ),
                                                                    b="set:hello",
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="size",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b"),
                                                                    ),
                                                                    b="set:hello:get",
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="getter-only attribute",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Getter for computed read-only value",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="Circle",
                                                            substack=[
                                                                define_getter(
                                                                    OPCODE="&gceOOP::define getter for (NAME) {:SHADOW:} {SUBSTACK}",
                                                                    name="doubled",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=multiply(
                                                                                OPCODE="&operators::(OPERAND1) * (OPERAND2)",
                                                                                operand1=get_attribute(
                                                                                    OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                                    name="_val",
                                                                                    instance=self_value(OPCODE="&gceOOP::self"),
                                                                                ),
                                                                                operand2="2",
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="c",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Circle", posargs="[]"),
                                                        ),
                                                        set_attribute(
                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                            instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                            name="_val",
                                                            value="7",
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="getter doubles _val",
                                                            substack=[
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="doubled",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                                    ),
                                                                    b="14",
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Raw _val unaffected",
                                                            substack=[
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="_val",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                                    ),
                                                                    b="7",
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="attributes without getter/setter bypass directly",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="setAttribute and getAttribute on plain attributes",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Plain", substack=[]),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="p",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Plain", posargs="[]"),
                                                        ),
                                                        set_attribute(
                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                            instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="p"),
                                                            name="x",
                                                            value="99",
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=get_attribute(
                                                                OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                name="x",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="p"),
                                                            ),
                                                            b="99",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        test_scope(
                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                            name="Operator Methods",
                            substack=[
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="left add operator",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Custom class with left add: returns val + operand",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="MyNum",
                                                            substack=[
                                                                configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["val"]', argdefaults="[]"),
                                                                define_special_method(
                                                                    OPCODE="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
                                                                    special_method="init",
                                                                    substack=[
                                                                        set_attribute(
                                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                                            instance=self_value(OPCODE="&gceOOP::self"),
                                                                            name="val",
                                                                            value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="val"),
                                                                        ),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="left add",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=add(
                                                                                OPCODE="&operators::(OPERAND1) + (OPERAND2)",
                                                                                operand1=get_attribute(
                                                                                    OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                                    name="val",
                                                                                    instance=self_value(OPCODE="&gceOOP::self"),
                                                                                ),
                                                                                operand2=operator_operator_value(OPCODE="&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}"),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="left subtract",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=subtract(
                                                                                OPCODE="&operators::(OPERAND1) - (OPERAND2)",
                                                                                operand1=get_attribute(
                                                                                    OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                                    name="val",
                                                                                    instance=self_value(OPCODE="&gceOOP::self"),
                                                                                ),
                                                                                operand2=operator_operator_value(OPCODE="&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}"),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="n",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="MyNum", posargs='["10"]'),
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="left add: 10 + 5 = 15",
                                                            substack=[
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=add(
                                                                        OPCODE="&operators::(OPERAND1) + (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="n"),
                                                                        operand2="5",
                                                                    ),
                                                                    b="15",
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="left add: 10 + 0 = 10",
                                                            substack=[
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=add(
                                                                        OPCODE="&operators::(OPERAND1) + (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="n"),
                                                                        operand2="0",
                                                                    ),
                                                                    b="10",
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="left subtract: 10 - 3 = 7",
                                                            substack=[
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=subtract(
                                                                        OPCODE="&operators::(OPERAND1) - (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="n"),
                                                                        operand2="3",
                                                                    ),
                                                                    b="7",
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="equals operator",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Custom equals: compares val attribute",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="Token",
                                                            substack=[
                                                                configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["id"]', argdefaults="[]"),
                                                                define_special_method(
                                                                    OPCODE="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
                                                                    special_method="init",
                                                                    substack=[
                                                                        set_attribute(
                                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                                            instance=self_value(OPCODE="&gceOOP::self"),
                                                                            name="id",
                                                                            value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="id"),
                                                                        ),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="equals",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=equals(
                                                                                OPCODE="&operators::(OPERAND1) = (OPERAND2)",
                                                                                operand1=get_attribute(
                                                                                    OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                                    name="id",
                                                                                    instance=self_value(OPCODE="&gceOOP::self"),
                                                                                ),
                                                                                operand2=operator_operator_value(OPCODE="&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}"),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="tok",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Token", posargs='["abc"]'),
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Equals the stored id",
                                                            substack=[
                                                                assert_(
                                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                                    condition=equals(
                                                                        OPCODE="&operators::(OPERAND1) = (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="tok"),
                                                                        operand2="abc",
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Does not equal a different value",
                                                            substack=[
                                                                assert_not(
                                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                    condition=equals(
                                                                        OPCODE="&operators::(OPERAND1) = (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="tok"),
                                                                        operand2="xyz",
                                                                    ),
                                                                ),
                                                                assert_not(
                                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                    condition=equals(
                                                                        OPCODE="&operators::(OPERAND1) = (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="tok"),
                                                                        operand2="",
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
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="reverse operations",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Right-side method is used when left operand has no matching method",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="RightOnly",
                                                            substack=[
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="right add",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=join(
                                                                                OPCODE="&operators::join (STRING1) (STRING2)",
                                                                                string1="R+",
                                                                                string2=operator_operator_value(OPCODE="&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}"),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="r",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="RightOnly", posargs="[]"),
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="plain_number + instance: triggers right add",
                                                            substack=[
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=add(
                                                                        OPCODE="&operators::(OPERAND1) + (OPERAND2)",
                                                                        operand1="7",
                                                                        operand2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="r"),
                                                                    ),
                                                                    b="R+7",
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Comparison reverse: op.greater triggers right-side less-than method",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="CompRight",
                                                            substack=[
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="less than",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=lt(
                                                                                OPCODE="&operators::(OPERAND1) < (OPERAND2)",
                                                                                operand1=operator_operator_value(OPCODE="&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}"),
                                                                                operand2=get_attribute(
                                                                                    OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                                    name="threshold",
                                                                                    instance=self_value(OPCODE="&gceOOP::self"),
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="c",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="CompRight", posargs="[]"),
                                                        ),
                                                        set_attribute(
                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                            instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                            name="threshold",
                                                            value="10",
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="5 > c: triggers c's less-than with operator_value=5; 5<10 is true",
                                                            substack=[
                                                                assert_(
                                                                    OPCODE="&gceTestRunner::assert <CONDITION>",
                                                                    condition=gt(
                                                                        OPCODE="&operators::(OPERAND1) > (OPERAND2)",
                                                                        operand1="5",
                                                                        operand2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="15 > c: operator_value=15; 15<10 is false",
                                                            substack=[
                                                                assert_not(
                                                                    OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                                    condition=gt(
                                                                        OPCODE="&operators::(OPERAND1) > (OPERAND2)",
                                                                        operand1="15",
                                                                        operand2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
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
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="all operator kinds",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Arithmetic operator kinds: each left/right variant is callable",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="ArithOps",
                                                            substack=[
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="left add",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="L+"),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="right add",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="R+"),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="left subtract",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="L-"),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="right subtract",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="R-"),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="left multiply",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="L*"),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="right multiply",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="R*"),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="left divide",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="L/"),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="right divide",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="R/"),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="left power",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="L^"),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="right power",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="R^"),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="left mod",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="L%"),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="right mod",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="R%"),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="a",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="ArithOps", posargs="[]"),
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Left-side arithmetic methods",
                                                            substack=[
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=add(
                                                                        OPCODE="&operators::(OPERAND1) + (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                        operand2="0",
                                                                    ),
                                                                    b="L+",
                                                                ),
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=subtract(
                                                                        OPCODE="&operators::(OPERAND1) - (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                        operand2="0",
                                                                    ),
                                                                    b="L-",
                                                                ),
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=multiply(
                                                                        OPCODE="&operators::(OPERAND1) * (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                        operand2="1",
                                                                    ),
                                                                    b="L*",
                                                                ),
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=divide(
                                                                        OPCODE="&operators::(OPERAND1) / (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                        operand2="1",
                                                                    ),
                                                                    b="L/",
                                                                ),
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=power(
                                                                        OPCODE="&operators::(OPERAND1) ^ (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                        operand2="1",
                                                                    ),
                                                                    b="L^",
                                                                ),
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=mod(
                                                                        OPCODE="&operators::(OPERAND1) mod (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                        operand2="1",
                                                                    ),
                                                                    b="L%",
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Right-side arithmetic methods (plain number on left)",
                                                            substack=[
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=add(
                                                                        OPCODE="&operators::(OPERAND1) + (OPERAND2)",
                                                                        operand1="0",
                                                                        operand2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                    ),
                                                                    b="R+",
                                                                ),
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=subtract(
                                                                        OPCODE="&operators::(OPERAND1) - (OPERAND2)",
                                                                        operand1="0",
                                                                        operand2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                    ),
                                                                    b="R-",
                                                                ),
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=multiply(
                                                                        OPCODE="&operators::(OPERAND1) * (OPERAND2)",
                                                                        operand1="1",
                                                                        operand2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                    ),
                                                                    b="R*",
                                                                ),
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=divide(
                                                                        OPCODE="&operators::(OPERAND1) / (OPERAND2)",
                                                                        operand1="1",
                                                                        operand2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                    ),
                                                                    b="R/",
                                                                ),
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=power(
                                                                        OPCODE="&operators::(OPERAND1) ^ (OPERAND2)",
                                                                        operand1="1",
                                                                        operand2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                    ),
                                                                    b="R^",
                                                                ),
                                                                assert_strict_equal(
                                                                    OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                                    a=mod(
                                                                        OPCODE="&operators::(OPERAND1) mod (OPERAND2)",
                                                                        operand1="1",
                                                                        operand2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                    ),
                                                                    b="R%",
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Comparison operator kinds: each kind is callable",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="CompOps",
                                                            substack=[
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="equals",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=true_boolean(OPCODE="&operators::true"),
                                                                        ),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="not equals",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=true_boolean(OPCODE="&operators::true"),
                                                                        ),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="greater than",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=true_boolean(OPCODE="&operators::true"),
                                                                        ),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="greater or equal",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=true_boolean(OPCODE="&operators::true"),
                                                                        ),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="less than",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=true_boolean(OPCODE="&operators::true"),
                                                                        ),
                                                                    ],
                                                                ),
                                                                define_operator_method(
                                                                    OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                                    operator_kind="less or equal",
                                                                    substack=[
                                                                        return_value(
                                                                            OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                            value=true_boolean(OPCODE="&operators::true"),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="c",
                                                            value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="CompOps", posargs="[]"),
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=equals(
                                                                OPCODE="&operators::(OPERAND1) = (OPERAND2)",
                                                                operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                                operand2="x",
                                                            ),
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=notequal(
                                                                OPCODE="&operators::(OPERAND1) != (OPERAND2)",
                                                                operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                                operand2="x",
                                                            ),
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=gt(
                                                                OPCODE="&operators::(OPERAND1) > (OPERAND2)",
                                                                operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                                operand2="x",
                                                            ),
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=gtorequal(
                                                                OPCODE="&operators::(OPERAND1) >= (OPERAND2)",
                                                                operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                                operand2="x",
                                                            ),
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=lt(
                                                                OPCODE="&operators::(OPERAND1) < (OPERAND2)",
                                                                operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                                operand2="x",
                                                            ),
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=ltorequal(
                                                                OPCODE="&operators::(OPERAND1) <= (OPERAND2)",
                                                                operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                                operand2="x",
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
                        test_scope(
                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                            name="Static Methods",
                            substack=[
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="define and call a static method",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(
                                                    OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                    name="MathUtils",
                                                    substack=[
                                                        configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["x"]', argdefaults="[]"),
                                                        define_static_method(
                                                            OPCODE="&gceOOP::define static method (NAME) {SUBSTACK}",
                                                            name="square",
                                                            substack=[
                                                                return_value(
                                                                    OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                    value=multiply(
                                                                        OPCODE="&operators::(OPERAND1) * (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="x"),
                                                                        operand2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="x"),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["a","b"]', argdefaults="[]"),
                                                        define_static_method(
                                                            OPCODE="&gceOOP::define static method (NAME) {SUBSTACK}",
                                                            name="add",
                                                            substack=[
                                                                return_value(
                                                                    OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                    value=add(
                                                                        OPCODE="&operators::(OPERAND1) + (OPERAND2)",
                                                                        operand1=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                        operand2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="b"),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="callStaticMethod: square(4) = 16",
                                                    substack=[
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=call_static_method(
                                                                OPCODE="&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)",
                                                                class_="MathUtils",
                                                                name="square",
                                                                posargs='["4"]',
                                                            ),
                                                            b="16",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="callStaticMethod: square(0) = 0",
                                                    substack=[
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=call_static_method(
                                                                OPCODE="&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)",
                                                                class_="MathUtils",
                                                                name="square",
                                                                posargs='["0"]',
                                                            ),
                                                            b="0",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="callStaticMethod: add(3, 7) = 10",
                                                    substack=[
                                                        assert_strict_equal(
                                                            OPCODE="&gceTestRunner::assert typed equality (A) = (B)",
                                                            a=call_static_method(
                                                                OPCODE="&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)",
                                                                class_="MathUtils",
                                                                name="add",
                                                                posargs='["3","7"]',
                                                            ),
                                                            b="10",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="getStaticMethodFunc + callFunction",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(
                                                    OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                    name="Fmt",
                                                    substack=[
                                                        configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["val"]', argdefaults="[]"),
                                                        define_static_method(
                                                            OPCODE="&gceOOP::define static method (NAME) {SUBSTACK}",
                                                            name="wrap",
                                                            substack=[
                                                                return_value(
                                                                    OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                    value=join3(
                                                                        OPCODE="&operators::join (STRING1) (STRING2) (STRING3)",
                                                                        string1="[",
                                                                        string2=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="val"),
                                                                        string3="]",
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="getStaticMethodFunc returns a callable function",
                                                    substack=[
                                                        set_scope_var(
                                                            OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                            name="wrapFn",
                                                            value=get_static_method_func(OPCODE="&gceOOP::get static method (NAME) of (CLASS) as function", name="wrap", class_="Fmt"),
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=typeof_value(
                                                                OPCODE="&gceFuncsScopes::typeof (VALUE)",
                                                                value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="wrapFn"),
                                                            ),
                                                            b=typeof_value_selection(OPCODE="&gceFuncsScopes::([TYPE])", type="Function (GCE)"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="callFunction on retrieved static method",
                                                    substack=[
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="wrapFn", posargs='["hello"]'),
                                                            b="[hello]",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Both callStaticMethod and callFunction give same result",
                                                    substack=[
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_static_method(
                                                                OPCODE="&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)",
                                                                class_="Fmt",
                                                                name="wrap",
                                                                posargs='["world"]',
                                                            ),
                                                            b=call_function(OPCODE="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)", func="wrapFn", posargs='["world"]'),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="error cases",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Solo", substack=[]),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Calling a non-existent static method throws",
                                                    substack=[
                                                        assert_throws(
                                                            OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                            substack=[
                                                                execute_expression(
                                                                    OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                    expr=call_static_method(
                                                                        OPCODE="&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)",
                                                                        class_="Solo",
                                                                        name="missing",
                                                                        posargs="[]",
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
                        test_scope(
                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                            name="Class Variables",
                            substack=[
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="set and get class variable",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Counter", substack=[]),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Set and read a class variable",
                                                    substack=[
                                                        set_class_variable(
                                                            OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                            class_="Counter",
                                                            name="count",
                                                            value="0",
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=get_class_variable(OPCODE="&gceOOP::on (CLASS) get class var (NAME)", name="count", class_="Counter"),
                                                            b="0",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Update the class variable",
                                                    substack=[
                                                        set_class_variable(
                                                            OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                            class_="Counter",
                                                            name="count",
                                                            value="42",
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=get_class_variable(OPCODE="&gceOOP::on (CLASS) get class var (NAME)", name="count", class_="Counter"),
                                                            b="42",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Multiple class variables coexist",
                                                    substack=[
                                                        set_class_variable(
                                                            OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                            class_="Counter",
                                                            name="name",
                                                            value="MyCounter",
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=get_class_variable(OPCODE="&gceOOP::on (CLASS) get class var (NAME)", name="name", class_="Counter"),
                                                            b="MyCounter",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Reading first variable unchanged",
                                                    substack=[
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=get_class_variable(OPCODE="&gceOOP::on (CLASS) get class var (NAME)", name="count", class_="Counter"),
                                                            b="42",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="propertyNamesOfClass reflects class variables",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(
                                                    OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                    name="Config",
                                                    substack=[
                                                        define_instance_method(
                                                            OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="doWork",
                                                            substack=[
                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="done"),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                set_class_variable(
                                                    OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                    class_="Config",
                                                    name="version",
                                                    value="1",
                                                ),
                                                set_class_variable(
                                                    OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                    class_="Config",
                                                    name="author",
                                                    value="test",
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Class variable names listed",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="version",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="class variable", class_="Config"),
                                                        ),
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="author",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="class variable", class_="Config"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Method names NOT in class variable list",
                                                    substack=[
                                                        assert_text_not_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                            text="doWork",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="class variable", class_="Config"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Instance method names listed correctly",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="doWork",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="instance method", class_="Config"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Class variable names NOT in instance method list",
                                                    substack=[
                                                        assert_text_not_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                            text="version",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="instance method", class_="Config"),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="delete class variable",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Bag", substack=[]),
                                                set_class_variable(
                                                    OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                    class_="Bag",
                                                    name="keep",
                                                    value="yes",
                                                ),
                                                set_class_variable(
                                                    OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                    class_="Bag",
                                                    name="remove",
                                                    value="no",
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Both exist before delete",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="keep",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="class variable", class_="Bag"),
                                                        ),
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="remove",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="class variable", class_="Bag"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Delete one",
                                                    substack=[
                                                        delete_class_variable(OPCODE="&gceOOP::on (CLASS) delete class var (NAME)", class_="Bag", name="remove"),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Deleted variable throws on get",
                                                    substack=[
                                                        assert_throws(
                                                            OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                            substack=[
                                                                execute_expression(
                                                                    OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                    expr=get_class_variable(OPCODE="&gceOOP::on (CLASS) get class var (NAME)", name="remove", class_="Bag"),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Deleted variable absent from property names",
                                                    substack=[
                                                        assert_text_not_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                            text="remove",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="class variable", class_="Bag"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Other variable unaffected",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="keep",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="class variable", class_="Bag"),
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=get_class_variable(OPCODE="&gceOOP::on (CLASS) get class var (NAME)", name="keep", class_="Bag"),
                                                            b="yes",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="class variables are shared across instances",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(
                                                    OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                    name="Shared",
                                                    substack=[
                                                        define_instance_method(
                                                            OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="getVar",
                                                            substack=[
                                                                return_value(
                                                                    OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                    value=get_class_variable(OPCODE="&gceOOP::on (CLASS) get class var (NAME)", name="shared", class_="Shared"),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                set_class_variable(
                                                    OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                    class_="Shared",
                                                    name="shared",
                                                    value="initial",
                                                ),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="i1",
                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Shared", posargs="[]"),
                                                ),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="i2",
                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Shared", posargs="[]"),
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Both instances see the same class variable",
                                                    substack=[
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_method(
                                                                OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="i1"),
                                                                name="getVar",
                                                                posargs="[]",
                                                            ),
                                                            b="initial",
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_method(
                                                                OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="i2"),
                                                                name="getVar",
                                                                posargs="[]",
                                                            ),
                                                            b="initial",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Update class variable - both instances see new value",
                                                    substack=[
                                                        set_class_variable(
                                                            OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                            class_="Shared",
                                                            name="shared",
                                                            value="updated",
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_method(
                                                                OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="i1"),
                                                                name="getVar",
                                                                posargs="[]",
                                                            ),
                                                            b="updated",
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=call_method(
                                                                OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="i2"),
                                                                name="getVar",
                                                                posargs="[]",
                                                            ),
                                                            b="updated",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        test_scope(
                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                            name="Introspection",
                            substack=[
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="getAttribute and setAttribute (direct)",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(
                                                    OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                    name="Person",
                                                    substack=[
                                                        configure_next_function_args(OPCODE="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)", argnames='["name"]', argdefaults="[]"),
                                                        define_special_method(
                                                            OPCODE="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
                                                            special_method="init",
                                                            substack=[
                                                                set_attribute(
                                                                    OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                                    instance=self_value(OPCODE="&gceOOP::self"),
                                                                    name="name",
                                                                    value=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="name"),
                                                                ),
                                                            ],
                                                        ),
                                                        define_instance_method(
                                                            OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="greet",
                                                            substack=[
                                                                return_value(
                                                                    OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                    value=join(
                                                                        OPCODE="&operators::join (STRING1) (STRING2)",
                                                                        string1="Hi, ",
                                                                        string2=get_attribute(
                                                                            OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                            name="name",
                                                                            instance=self_value(OPCODE="&gceOOP::self"),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                create_subclass_at(
                                                    OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                    name="Employee",
                                                    superclass="Person",
                                                    substack=[],
                                                ),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="p",
                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Person", posargs='["Bob"]'),
                                                ),
                                                set_attribute(
                                                    OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                    instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="p"),
                                                    name="age",
                                                    value="30",
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Attribute set via init",
                                                    substack=[
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=get_attribute(
                                                                OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                name="name",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="p"),
                                                            ),
                                                            b="Bob",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Attribute set after creation",
                                                    substack=[
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=get_attribute(
                                                                OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                name="age",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="p"),
                                                            ),
                                                            b="30",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Overwrite attribute",
                                                    substack=[
                                                        set_attribute(
                                                            OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                            instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="p"),
                                                            name="name",
                                                            value="Robert",
                                                        ),
                                                        assert_unstrict_equal(
                                                            OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                            a=get_attribute(
                                                                OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                name="name",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="p"),
                                                            ),
                                                            b="Robert",
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Missing attribute throws",
                                                    substack=[
                                                        assert_throws(
                                                            OPCODE="&gceTestRunner::assert throws error {SUBSTACK}",
                                                            substack=[
                                                                execute_expression(
                                                                    OPCODE="&gceFuncsScopes::execute expression (EXPR)",
                                                                    expr=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="missing",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="p"),
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
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="getClassOfInstance",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Cat", substack=[]),
                                                create_subclass_at(
                                                    OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                    name="Kitten",
                                                    superclass="Cat",
                                                    substack=[],
                                                ),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="c",
                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Cat", posargs="[]"),
                                                ),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="k",
                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Kitten", posargs="[]"),
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="getClassOfInstance contains the class name",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="Cat",
                                                            value=get_class_of_instance(
                                                                OPCODE="&gceOOP::get class of (INSTANCE)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                            ),
                                                        ),
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="Kitten",
                                                            value=get_class_of_instance(
                                                                OPCODE="&gceOOP::get class of (INSTANCE)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="k"),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Cat instance does NOT report Kitten",
                                                    substack=[
                                                        assert_text_not_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                            text="Kitten",
                                                            value=get_class_of_instance(
                                                                OPCODE="&gceOOP::get class of (INSTANCE)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="isInstance",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Fruit", substack=[]),
                                                create_subclass_at(
                                                    OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                    name="Apple",
                                                    superclass="Fruit",
                                                    substack=[],
                                                ),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="f",
                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Fruit", posargs="[]"),
                                                ),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="a",
                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Apple", posargs="[]"),
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Instance of own class",
                                                    substack=[
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_instance(
                                                                OPCODE="&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?",
                                                                potential_instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="f"),
                                                                class_="Fruit",
                                                            ),
                                                        ),
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_instance(
                                                                OPCODE="&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?",
                                                                potential_instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                class_="Apple",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Subclass instance is instance of superclass",
                                                    substack=[
                                                        assert_(
                                                            OPCODE="&gceTestRunner::assert <CONDITION>",
                                                            condition=is_instance(
                                                                OPCODE="&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?",
                                                                potential_instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="a"),
                                                                class_="Fruit",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Superclass instance is NOT instance of subclass",
                                                    substack=[
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=is_instance(
                                                                OPCODE="&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?",
                                                                potential_instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="f"),
                                                                class_="Apple",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Non-instance values return false",
                                                    substack=[
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=is_instance(OPCODE="&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?", potential_instance="hello", class_="Fruit"),
                                                        ),
                                                        assert_not(
                                                            OPCODE="&gceTestRunner::assert not <CONDITION>",
                                                            condition=is_instance(
                                                                OPCODE="&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?",
                                                                potential_instance=nothing(OPCODE="&gceFuncsScopes::Nothing"),
                                                                class_="Fruit",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="propertyNamesOfClass",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(
                                                    OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                    name="Widget",
                                                    substack=[
                                                        define_instance_method(
                                                            OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="render",
                                                            substack=[
                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="rendered"),
                                                            ],
                                                        ),
                                                        define_static_method(
                                                            OPCODE="&gceOOP::define static method (NAME) {SUBSTACK}",
                                                            name="create",
                                                            substack=[
                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="widget"),
                                                            ],
                                                        ),
                                                        define_getter(
                                                            OPCODE="&gceOOP::define getter for (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="width",
                                                            substack=[
                                                                return_value(
                                                                    OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                    value=get_attribute(
                                                                        OPCODE="&gceOOP::on (INSTANCE) get attribute (NAME)",
                                                                        name="_w",
                                                                        instance=self_value(OPCODE="&gceOOP::self"),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        define_setter(
                                                            OPCODE="&gceOOP::define setter for (NAME) {:SHADOW1:} {:SHADOW2:} {SUBSTACK}",
                                                            name="height",
                                                            substack=[
                                                                set_attribute(
                                                                    OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                                    instance=self_value(OPCODE="&gceOOP::self"),
                                                                    name="_h",
                                                                    value=define_setter_value(OPCODE="&gceOOP::operator value {{id=gceOOP_defineSetterValue}}"),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                set_class_variable(
                                                    OPCODE="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                                                    class_="Widget",
                                                    name="version",
                                                    value="2",
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Instance methods",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="render",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="instance method", class_="Widget"),
                                                        ),
                                                        assert_text_not_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                            text="create",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="instance method", class_="Widget"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Static methods",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="create",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="static method", class_="Widget"),
                                                        ),
                                                        assert_text_not_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                            text="render",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="static method", class_="Widget"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Getter methods",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="width",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="getter method", class_="Widget"),
                                                        ),
                                                        assert_text_not_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                            text="height",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="getter method", class_="Widget"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Setter methods",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="height",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="setter method", class_="Widget"),
                                                        ),
                                                        assert_text_not_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                            text="width",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="setter method", class_="Widget"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Class variables",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="version",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="class variable", class_="Widget"),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="propertyNamesOfClass edge cases",
                                    substack=[
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Empty class has no own instance methods (beyond built-in)",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Empty", substack=[]),
                                                        assert_text_not_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                            text="render",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="instance method", class_="Empty"),
                                                        ),
                                                        assert_text_not_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                            text="create",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="static method", class_="Empty"),
                                                        ),
                                                        assert_text_not_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                            text="version",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="class variable", class_="Empty"),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Subclass without own methods still sees inherited methods",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="Parent",
                                                            substack=[
                                                                define_instance_method(
                                                                    OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                                    name="inherited",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="from-parent"),
                                                                    ],
                                                                ),
                                                                define_static_method(
                                                                    OPCODE="&gceOOP::define static method (NAME) {SUBSTACK}",
                                                                    name="parentStatic",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="static-from-parent"),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        create_subclass_at(
                                                            OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                            name="ChildNoMethods",
                                                            superclass="Parent",
                                                            substack=[],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Inherited instance method visible on child",
                                                            substack=[
                                                                assert_text_in_value(
                                                                    OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                                    text="inherited",
                                                                    value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="instance method", class_="ChildNoMethods"),
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Inherited static method visible on child",
                                                            substack=[
                                                                assert_text_in_value(
                                                                    OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                                    text="parentStatic",
                                                                    value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="static method", class_="ChildNoMethods"),
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Parent's own methods also still visible on parent",
                                                            substack=[
                                                                assert_text_in_value(
                                                                    OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                                    text="inherited",
                                                                    value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="instance method", class_="Parent"),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        test_scope(
                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                            name="Overriding a method replaces it, not duplicates it",
                                            substack=[
                                                create_var_scope(
                                                    OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="Base2",
                                                            substack=[
                                                                define_instance_method(
                                                                    OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                                    name="greet",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="base-greet"),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        create_subclass_at(
                                                            OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                            name="Child2",
                                                            superclass="Base2",
                                                            substack=[
                                                                define_instance_method(
                                                                    OPCODE="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                                                                    name="greet",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="child-greet"),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="greet appears in child's instance methods",
                                                            substack=[
                                                                assert_text_in_value(
                                                                    OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                                    text="greet",
                                                                    value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="instance method", class_="Child2"),
                                                                ),
                                                            ],
                                                        ),
                                                        test_scope(
                                                            OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                            name="Override is active — child instance calls child version",
                                                            substack=[
                                                                set_scope_var(
                                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                                    name="c",
                                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Child2", posargs="[]"),
                                                                ),
                                                                assert_unstrict_equal(
                                                                    OPCODE="&gceTestRunner::assert string equality (A) = (B)",
                                                                    a=call_method(
                                                                        OPCODE="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                                                                        instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="c"),
                                                                        name="greet",
                                                                        posargs="[]",
                                                                    ),
                                                                    b="child-greet",
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="getAllAttributes",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="Data", substack=[]),
                                                set_scope_var(
                                                    OPCODE="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                                                    name="d",
                                                    value=create_instance(OPCODE="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)", class_="Data", posargs="[]"),
                                                ),
                                                set_attribute(
                                                    OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                    instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="d"),
                                                    name="x",
                                                    value="1",
                                                ),
                                                set_attribute(
                                                    OPCODE="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                                                    instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="d"),
                                                    name="y",
                                                    value="2",
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="getAllAttributes includes all set attributes",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="x",
                                                            value=get_all_attributes(
                                                                OPCODE="&gceOOP::all attributes of (INSTANCE)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="d"),
                                                            ),
                                                        ),
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="y",
                                                            value=get_all_attributes(
                                                                OPCODE="&gceOOP::all attributes of (INSTANCE)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="d"),
                                                            ),
                                                        ),
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="1",
                                                            value=get_all_attributes(
                                                                OPCODE="&gceOOP::all attributes of (INSTANCE)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="d"),
                                                            ),
                                                        ),
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="2",
                                                            value=get_all_attributes(
                                                                OPCODE="&gceOOP::all attributes of (INSTANCE)",
                                                                instance=get_scope_var(OPCODE="&gceFuncsScopes::get var (NAME)", name="d"),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="propertyNamesOfClass: special method dropdown",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                create_class_at(
                                                    OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                    name="Nameable",
                                                    substack=[
                                                        define_special_method(OPCODE="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}", special_method="init", substack=[]),
                                                        define_special_method(
                                                            OPCODE="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
                                                            special_method="as string",
                                                            substack=[
                                                                return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="nameable"),
                                                            ],
                                                        ),
                                                        define_operator_method(
                                                            OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                            operator_kind="left add",
                                                            substack=[
                                                                return_value(
                                                                    OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                    value=join(
                                                                        OPCODE="&operators::join (STRING1) (STRING2)",
                                                                        string1="L+",
                                                                        string2=operator_operator_value(OPCODE="&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}"),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        define_operator_method(
                                                            OPCODE="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                                                            operator_kind="not equals",
                                                            substack=[
                                                                return_value(
                                                                    OPCODE="&gceFuncsScopes::return (VALUE)",
                                                                    value=true_boolean(OPCODE="&operators::true"),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="init appears as 'init' in special method list",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="init",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="special method", class_="Nameable"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="as string appears as 'as string' in special method list",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="as string",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="special method", class_="Nameable"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Special methods do NOT appear in instance method list",
                                                    substack=[
                                                        assert_text_not_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                            text="init",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="instance method", class_="Nameable"),
                                                        ),
                                                        assert_text_not_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                            text="as string",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="instance method", class_="Nameable"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Operator methods appear as public names in operator method list",
                                                    substack=[
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="left add",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="operator method", class_="Nameable"),
                                                        ),
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="not equals",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="operator method", class_="Nameable"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Operator methods do NOT appear in instance or special method list",
                                                    substack=[
                                                        assert_text_not_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                            text="left add",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="instance method", class_="Nameable"),
                                                        ),
                                                        assert_text_not_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                                                            text="left add",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="special method", class_="Nameable"),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                test_scope(
                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                    name="propertyNamesOfClass: special method inheritance",
                                    substack=[
                                        create_var_scope(
                                            OPCODE="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                                            substack=[
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Empty class always has init from common superclass",
                                                    substack=[
                                                        create_class_at(OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}", name="BareClass", substack=[]),
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="init",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="special method", class_="BareClass"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Class with only as string still inherits init",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="AsStringOnly",
                                                            substack=[
                                                                define_special_method(
                                                                    OPCODE="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
                                                                    special_method="as string",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="str"),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="init",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="special method", class_="AsStringOnly"),
                                                        ),
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="as string",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="special method", class_="AsStringOnly"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Subclass inherits special methods from parent",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="SpBase",
                                                            substack=[
                                                                define_special_method(
                                                                    OPCODE="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
                                                                    special_method="as string",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="base"),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        create_subclass_at(
                                                            OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                            name="SpChild",
                                                            superclass="SpBase",
                                                            substack=[],
                                                        ),
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="as string",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="special method", class_="SpChild"),
                                                        ),
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="init",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="special method", class_="SpChild"),
                                                        ),
                                                    ],
                                                ),
                                                test_scope(
                                                    OPCODE="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                                                    name="Subclass overriding as string replaces, not duplicates",
                                                    substack=[
                                                        create_class_at(
                                                            OPCODE="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                                                            name="SpBase2",
                                                            substack=[
                                                                define_special_method(
                                                                    OPCODE="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
                                                                    special_method="as string",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="base2"),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        create_subclass_at(
                                                            OPCODE="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                                                            name="SpChild2",
                                                            superclass="SpBase2",
                                                            substack=[
                                                                define_special_method(
                                                                    OPCODE="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
                                                                    special_method="as string",
                                                                    substack=[
                                                                        return_value(OPCODE="&gceFuncsScopes::return (VALUE)", value="child2"),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        assert_text_in_value(
                                                            OPCODE="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                                                            text="as string",
                                                            value=property_names_of_class(OPCODE="&gceOOP::([PROPERTY]) names of class (CLASS)", property="special method", class_="SpChild2"),
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
                ThirdVectorCostume(
                    name="empty",
                    file_extension="svg",
                    rotation_center=(240, 180),
                    content='<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" height="2" version="1.1" viewBox="-1 -1 2 2" width="2">
  <!-- Exported by Scratch - http://scratch.mit.edu/ -->
</svg>',
                ),
            ],
            sounds=[],
            costume_index=0,
            volume=100,
            name="Test",
            local_variables=[],
            local_lists=[],
            local_monitors=[],
            is_visible=True,
            position=(0, 0),
            size=100,
            direction=90,
            is_draggable=False,
            rotation_style=SRSpriteRotationStyle.ALL_AROUND,
            uuid=UUID('c65ed9a3-1461-432b-9aa9-ab997c4c6ccd'),
        ),
    ],
    sprite_layer_stack=[
        UUID('285ec256-0a06-4a64-b9ca-b6b4b0d963ab'),
    ],
    global_variables=[],
    global_lists=[],
    global_monitors=[],
    extensions=[
        SRBuiltinExtension(id="jwProto"),
        SRCustomExtension(id="dogeiscutSet", url="https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutSet.js"),
        SRBuiltinExtension(id="jwLambda"),
        SRCustomExtension(id="gceOOP", url="http://localhost:5173/extensions/gceOOP.js"),
        SRCustomExtension(id="agBuffer", url="https://extensions.penguinmod.com/extensions/AndrewGaming587/agBuffer.js"),
        SRBuiltinExtension(id="jwVector"),
        SRBuiltinExtension(id="jwDate"),
        SRCustomExtension(id="divIterator", url="https://extensions.penguinmod.com/extensions/Div/divIterators.js"),
        SRCustomExtension(id="ddeDateFormatV2", url="https://extensions.penguinmod.com/extensions/ddededodediamante/dateFormatV2.js"),
        SRCustomExtension(id="fruitsPaintUtils", url="https://extensions.penguinmod.com/extensions/Fruits555000/PaintUtils.js"),
        SRBuiltinExtension(id="jwTargets"),
        SRBuiltinExtension(id="jwColor"),
        SRCustomExtension(id="gceTestRunner", url="http://localhost:5173/extensions/gceTestRunner.js"),
        SRBuiltinExtension(id="jwXML"),
        SRCustomExtension(id="dogeiscutObject", url="https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutObject.js"),
        SRBuiltinExtension(id="SPjavascriptV2"),
        SRBuiltinExtension(id="jwNum"),
        SRBuiltinExtension(id="newCanvas"),
        SRCustomExtension(id="divAlgEffects", url="https://extensions.penguinmod.com/extensions/Div/divAlgEffects.js"),
        SRCustomExtension(id="dogeiscutRegularExpressions", url="https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutRegularExpressions.js"),
        SRBuiltinExtension(id="jwArray"),
        SRCustomExtension(id="steve0greatnesstimers", url="https://extensions.penguinmod.com/extensions/steve0greatness/timers.js"),
        SRCustomExtension(id="gceFuncsScopes", url="http://localhost:5173/extensions/gceFuncsScopes.js"),
        SRCustomExtension(id="ddeDateFormat", url="https://extensions.penguinmod.com/extensions/ddededodediamante/dateFormat.js"),
    ],
)