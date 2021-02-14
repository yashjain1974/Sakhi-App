helper_code = """
ScreenManager:
    id:scr_mngr
    FirstScreen:
    LoginScreen:
    MainScreen:
    Books:
    Todo:
    Meditation:
    WomenSafety:
    NearbyHospitals:
    NearbyPolicestation:
    HelpLineNumbers:

<FirstScreen>
    name:"First"
    Image:
        source:"logo_size.jpg"
        size: self.texture_size
        size_hint:(None,None)
        size:(200,200)
        pos_hint:{"center_x":0.5,"center_y":0.5}
    MDFloatingActionButton:
        icon:"arrow-right"
        pos_hint:{"center_x":0.5,"center_y":0.1}
        md_bg_color: app.theme_cls.primary_color
        on_press:root.manager.current="Login"
<LoginScreen>
    name:"Login"
    
    MDTextField:
        
        hint_text:"Enter username"
        helper_text:"or forgot username"
        helper_text_mode:"on_focus"
        icon_right:"login"
        icon_right_color:app.theme_cls.primary_color
        pos_hint:{"center_x":0.5,"center_y":0.5}

        size_hint_x:None
        width:200
        

    MDFloatingActionButton:
        icon:"arrow-right"
        pos_hint:{"center_x":0.5,"center_y":0.3}
        on_press:root.manager.current="Main"
        md_bg_color: app.theme_cls.primary_color
        
        



<MainScreen>
    name:"Main"
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    size:root.width,root.height
                    orientation:"vertical"
                    
                    MDToolbar:
                        title:"Sakhi"
                        left_action_items:[["menu",lambda x:nav_drawer.set_state()]]
                        right_action_items:[["clock",lambda x:app.clock_bar()]]
                        elevation:8
                        GridLayout:
                            cols: 3
                            cols_minimum: {0: 100, 1: 800, 0:100}
        
                            Image:
                                source:"logo_size.jpg"
                                
                        
                        
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text:"To-do"
                                on_press:
                                    root.manager.current="todo"
                                IconLeftWidget:
                                    icon:"alarm"
                            OneLineIconListItem:
                                text:"Meditation"
                                on_press:root.manager.current="meditation"
                                IconLeftWidget:
                                    icon:"meditation"
                            OneLineIconListItem:
                                text:"Women_Safety-Measures"
                                on_press:root.manager.current="womensafety"
                                IconLeftWidget:
                                    icon:"hospital-box"
                            OneLineIconListItem:
                                text:"Books"
                                on_press:root.manager.current="books"
                                IconLeftWidget:
                                    icon:"book"

                            OneLineIconListItem:
                                text:"Nearby Hospitals"
                                on_press:root.manager.current="hospital"
                                IconLeftWidget:
                                    icon:"hospital-building"
                            OneLineIconListItem:
                                text:"Nearby Policestation"
                                on_press:root.manager.current="policestation"
                                IconLeftWidget:
                                    icon:"police-badge"
                            OneLineIconListItem:
                                text:"Help-line Numbers"
                                on_press:root.manager.current="helpline"
                                IconLeftWidget:
                                    icon:"contacts"
                            
                    

                    MDBottomAppBar:
                        MDToolbar:
                            mode:"center"
                            type:"bottom"
                            icon:"face-woman-outline"
                            left_action_items:[["coffee",lambda x:app.navigation_draw()]] 
                MDFloatingActionButtonSpeedDial:
                    hint_animation:True
                    rotation_root_button:True
                    

                    
                                
                                        
                    data:
                        {'account-question': 'Question',
                        'cart': 'Cart',
                        'calendar': 'Calendar'}           
                            
                        
        MDNavigationDrawer:
            id:nav_drawer

            BoxLayout:
                size:root.width,root.height
                orientation:"vertical"
                padding:"5dp"
                MDToolbar:
                    left_action_items:[["menu-left",lambda x:nav_drawer.set_state()]]
                    elevation:8


                Image:
                    source:"logo_size.jpg"
                    size: self.texture_size
                    size_hint:(None,None)
                    size:(100,100)
                    pos_hint:{"center_x":0.5,"center_y":0.5}

                BoxLayout:
                    orientation:"vertical"

                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text:"Profile"
                                IconLeftWidget:
                                    icon:"account"
                            OneLineIconListItem:
                                text:"Upload"
                                IconLeftWidget:
                                    icon:"upload"
                            OneLineIconListItem:
                                text:"Login"
                                IconLeftWidget:
                                    icon:"login"
                    MDLabel:
                        text:"Creator:-Yash Jain"
                        size_hint_y:None
                        height:self.texture_size[1]
                        theme_text_color:"Custom"
                        text_color:(0.2,0.7,0.7,1)
<Books>
    name:"books"
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:

                    orientation:"vertical"

                    MDToolbar:
                        title:"Books:-"
                        left_action_items:[["menu-right",lambda x:nav_drawer.set_state()]]
                        right_action_items:[["clock",lambda x:app.clock_bar()]]
                        elevation:8
                    BoxLayout:
                        orientation:"vertical"
                        padding:2
                        spacing:5
                        Image:
                            source:"books/img0.jpeg"
                            size: self.texture_size
                            size_hint:(None,None)
                            size:(500,150)
                            pos_hint:{"center_x":0.5,"center_y":0}
                        ScrollView:
                            size:self.size
                            MDList:
                                ThreeLineAvatarListItem:
                                    text:"Becoming"
                                    secondary_text:"Author:-Michelle Obama"
                                    tertiary_text:"Theme:-Chronicle,women_rights"
                                    ImageLeftWidget:
                                        source:"books/img1.jpg"
                                ThreeLineAvatarListItem:
                                    text:"Wild: From Lost to Found on the Pacific Crest Trail"
                                    secondary_text:"Author:-Cheryl Strayed"
                                    tertiary_text:"Theme:-epic,survival"
                                    ImageLeftWidget:
                                        source:"books/img2.jpg"
                                ThreeLineAvatarListItem:
                                    text:"Ruth Bader Ginsburg: A Life"
                                    secondary_text:"Author:-Jane Sherron de Hart"
                                    tertiary_text:"Theme:-Biography"
                                    ImageLeftWidget:
                                        source:"books/img.jpg"
                                ThreeLineAvatarListItem:
                                    text:"The Inheritance of Loss"
                                    secondary_text:"Author:-Kiran Desai"
                                    tertiary_text:"Theme:-Psychological-Fiction"
                                    ImageLeftWidget:
                                        source:"books/img4.jpeg"
                                ThreeLineAvatarListItem:
                                    text:"The Ministry of Utmost Happiness"
                                    secondary_text:"Author:-Arundhati Roy"
                                    tertiary_text:"Theme:-Literary Fiction"
                                    ImageLeftWidget:
                                        source:"books/img5.jpeg"
                                ThreeLineAvatarListItem:
                                    text:"The Twientith Wife"
                                    secondary_text:"Indu Sundersan"
                                    tertiary_text:"Theme:-Period Drama/Biography fiction"
                                    ImageLeftWidget:
                                        source:"books/img6.jpeg"
                                ThreeLineAvatarListItem:
                                    text:"The God Of Small Things"
                                    secondary_text:"Author:-Arundhati Roy"
                                    tertiary_text:"Genre:-Domestic-Fiction"
                                    ImageLeftWidget:
                                        source:"books/img3.jpeg"
                    MDBottomAppBar:
                        MDToolbar:
                            elevation:10
                            mode:"end"
                            type:"bottom"
                            icon:"face-woman-outline"
                            MDFlatButton:
                                text:"Back"
                                pos_hint:{"center_x":0.2,"center_y":0.3}
                                on_press:
                                    root.manager.current="Main"
                                    

    MDNavigationDrawer:
        id:nav_drawer

        BoxLayout:
            size:root.width,root.height
            orientation:"vertical"
            padding:"5dp"
            MDToolbar:
                left_action_items:[["menu-left",lambda x:nav_drawer.set_state()]]
                elevation:8


            Image:
                source:"logo_size.jpg"
                size: self.texture_size
                size_hint:(None,None)
                size:(100,100)
                pos_hint:{"center_x":0.5,"center_y":0.5}

            BoxLayout:
                orientation:"vertical"

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"Profile"
                            IconLeftWidget:
                                icon:"account"
                        OneLineIconListItem:
                            text:"Upload"
                            IconLeftWidget:
                                icon:"upload"
                        OneLineIconListItem:
                            text:"Login"
                            IconLeftWidget:
                                icon:"login"
                MDLabel:
                    text:"Creator:-Yash Jain"
                    size_hint_y:None
                    height:self.texture_size[1]
                    theme_text_color:"Custom"
                    text_color:(0.2,0.7,0.7,1)   

<Todo>
    name:"todo"
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:

                    orientation:"vertical"

                    MDToolbar:
                        title:"Todo:-"
                        left_action_items:[["menu-right",lambda x:nav_drawer.set_state()]]
                        right_action_items:[["clock",lambda x:app.clock_bar()]]
                        elevation:8
                    ScrollView:
                        BoxLayout:
                            size:root.width,root.height
                            orientation:"vertical"
                            padding:"5dp"
                            MDTextField:
                                hint_text:"Enter To_do "
                                pos_hint:{"center_x":0.5,"center_y":0.5}
                                icon_right:"pencil"
                                icon_right_color:app.theme_cls.primary_color
                                size_hint_x:None
                                width:200
                            MDFloatingActionButton:
                                icon:"arrow-down"
                                pos_hint:{"center_x":0.2,"center_y":0.3}
                                on_press:root.manager.current="Main"
                                md_bg_color: app.theme_cls.primary_color
                    MDBottomAppBar:
                        MDToolbar:
                            elevation:10
                            mode:"end"
                            type:"bottom"
                            icon:"face-woman-outline"
                            MDFlatButton:
                                text:"Back"
                                pos_hint:{"center_x":0.2,"center_y":0.3}
                                on_press:root.manager.current="Main"
    
                
    

    MDNavigationDrawer:
        id:nav_drawer

        BoxLayout:
            size:root.width,root.height
            orientation:"vertical"
            padding:"5dp"
            MDToolbar:
                left_action_items:[["menu-left",lambda x:nav_drawer.set_state()]]
                elevation:8


            Image:
                source:"logo_size.jpg"
                size: self.texture_size
                size_hint:(None,None)
                size:(100,100)
                pos_hint:{"center_x":0.5,"center_y":0.5}

            BoxLayout:
                orientation:"vertical"

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"Profile"
                            IconLeftWidget:
                                icon:"account"
                        OneLineIconListItem:
                            text:"Upload"
                            IconLeftWidget:
                                icon:"upload"
                        OneLineIconListItem:
                            text:"Login"
                            IconLeftWidget:
                                icon:"login"
                MDLabel:
                    text:"Creator:-Yash Jain"
                    size_hint_y:None
                    height:self.texture_size[1]
                    theme_text_color:"Custom"
                    text_color:(0.2,0.7,0.7,1)  
<Meditation>
    name:"meditation"
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:

                    orientation:"vertical"

                    MDToolbar:
                        title:"Meditation:-"
                        left_action_items:[["menu-right",lambda x:nav_drawer.set_state()]]
                        right_action_items:[["clock",lambda x:app.clock_bar()]]
                        elevation:8
                    BoxLayout:
                        orientation:"vertical"
                        padding:2
                        spacing:3
                        Image:
                            source:"Meditation/img6.jpg"
                            size: self.texture_size
                            size_hint:(None,None)
                            size:(500,150)
                            pos_hint:{"center_x":0.5,"center_y":0}
                        ScrollView:
                            MDList:
                                TwoLineAvatarListItem:
                                    text:"1.The Raisin Exercise"
                                    secondary_text:"Exercise for beginners"
                                    ImageLeftWidget:
                                        source:"Meditation/img1.jpg"
                                TwoLineAvatarListItem:
                                    text:"2. The Body Scan"
                                    secondary_text:"Exercise for practitioners"
                                    ImageLeftWidget:
                                        source:"Meditation/img2.jpg"
                                TwoLineAvatarListItem:
                                    text:"3. Mindful Seeing"
                                    secondary_text:"A healthy imagination"
                                    ImageLeftWidget:
                                        source:"Meditation/img3.jpg"
                                TwoLineAvatarListItem:
                                    text:"4. Mindful Listening"
                                    secondary_text:"Valuable positive Communication"
                                    ImageLeftWidget:
                                        source:"Meditation/img4.png"
                                TwoLineAvatarListItem:
                                    text:"5.Five Senses Exercise"
                                    secondary_text:"Understand Our Body"
                                    ImageLeftWidget:
                                        source:"Meditation/img5.jpg"
                    MDBottomAppBar:
                        MDToolbar:
                            elevation:10
                            mode:"end"
                            type:"bottom"
                            icon:"face-woman-outline"
                            MDFlatButton:
                                text:"Back"
                                pos_hint:{"center_x":0.2,"center_y":0.3}
                                on_press:root.manager.current="Main"
    MDNavigationDrawer:
        id:nav_drawer

        BoxLayout:
            size:root.width,root.height
            orientation:"vertical"
            padding:"5dp"
            MDToolbar:
                left_action_items:[["menu-left",lambda x:nav_drawer.set_state()]]
                elevation:8


            Image:
                source:"logo_size.jpg"
                size: self.texture_size
                size_hint:(None,None)
                size:(100,100)
                pos_hint:{"center_x":0.5,"center_y":0.5}

            BoxLayout:
                orientation:"vertical"

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"Profile"
                            IconLeftWidget:
                                icon:"account"
                        OneLineIconListItem:
                            text:"Upload"
                            IconLeftWidget:
                                icon:"upload"
                        OneLineIconListItem:
                            text:"Login"
                            IconLeftWidget:
                                icon:"login"
                MDLabel:
                    text:"Creator:-Yash Jain"
                    size_hint_y:None
                    height:self.texture_size[1]
                    theme_text_color:"Custom"
                    text_color:(0.2,0.7,0.7,1)   

                    
                    
    

<WomenSafety>
    name:"womensafety"
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:

                    orientation:"vertical"
                    padding:0
                    spacing:0

                    MDToolbar:
                        title:"Safety-Measures"
                        left_action_items:[["menu-right",lambda x:nav_drawer.set_state()]]
                        right_action_items:[["clock",lambda x:app.clock_bar()]]
                        elevation:8
                    BoxLayout:
                        orientation:"vertical"
                        padding:2
                        spacing:5
                        Image:
                            source:"Womensafety/img1.jpg"
                            size: self.texture_size
                            size_hint:(None,None)
                            size:(500,150)
                            pos_hint:{"center_x":0.5,"center_y":0}
                        ScrollView:
                            MDList:
                                TwoLineAvatarListItem:
                                    text:"1. PRACTICE AWARENESS"
                                    secondary_text:"Self-defense is awareness"
                                    ImageLeftWidget:
                                        source:"Womensafety/img2.jpg"
                                TwoLineAvatarListItem:
                                    text:"2. USE YOUR SIXTH SENSE."
                                    secondary_text:"Sixth sense."
                                    ImageLeftWidget:
                                        source:"Womensafety/img3.png"
                                TwoLineAvatarListItem:
                                    text:"3. TAKE SELF-DEFENSE TRAINING."
                                    secondary_text:"Arts techniques"
                                    ImageLeftWidget:
                                        source:"Womensafety/img4.jpeg"
                                TwoLineAvatarListItem:
                                    text:"4. ESCAPE IS ALWAYS YOUR BEST OPTION."
                                    secondary_text:"Unthinkable happens?"
                                    ImageLeftWidget:
                                        source:"Womensafety/img5.jpg"
                                TwoLineAvatarListItem:
                                    text:"5. YOU HAVE A RIGHT TO FIGHT."
                                    secondary_text:"Defend yourself physically"
                                    ImageLeftWidget:
                                        source:"Womensafety/img6.jpg"
                                TwoLineAvatarListItem:
                                    text:"6. SAFEGUARD AGAINST HOME INVASIONS."
                                    secondary_text:"prevent a home invasion "
                                    ImageLeftWidget:
                                        source:"Womensafety/img7.jpg"
                                TwoLineAvatarListItem:
                                    text:"7. BE PREPARED WHEN YOU TRAVEL."
                                    secondary_text:"Violent crimes against women"
                                    ImageLeftWidget:
                                        source:"Womensafety/img8.png"
                                        
                        
                    MDBottomAppBar:
                        MDToolbar:
                            elevation:10
                            mode:"end"
                            type:"bottom"
                            icon:"face-woman-outline"
                            MDFlatButton:
                                text:"Back"
                                pos_hint:{"center_x":0.2,"center_y":0.3}
                                on_press:root.manager.current="Main"
    MDNavigationDrawer:
        id:nav_drawer

        BoxLayout:
            size:root.width,root.height
            orientation:"vertical"
            padding:"5dp"
            MDToolbar:
                left_action_items:[["menu-left",lambda x:nav_drawer.set_state()]]
                elevation:8


            Image:
                source:"logo_size.jpg"
                size: self.texture_size
                size_hint:(None,None)
                size:(100,100)
                pos_hint:{"center_x":0.5,"center_y":0.5}

            BoxLayout:
                orientation:"vertical"

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"Profile"
                            IconLeftWidget:
                                icon:"account"
                        OneLineIconListItem:
                            text:"Upload"
                            IconLeftWidget:
                                icon:"upload"
                        OneLineIconListItem:
                            text:"Login"
                            IconLeftWidget:
                                icon:"login"
                MDLabel:
                    text:"Creator:-Yash Jain"
                    size_hint_y:None
                    height:self.texture_size[1]
                    theme_text_color:"Custom"
                    text_color:(0.2,0.7,0.7,1)   

<NearbyHospitals>
    name:"hospital"
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:

                    orientation:"vertical"

                    MDToolbar:
                        title:"Hospitals:-"
                        left_action_items:[["menu-right",lambda x:nav_drawer.set_state()]]
                        right_action_items:[["clock",lambda x:app.clock_bar()]]
                        elevation:8
                    BoxLayout:
                        orientation:"vertical"
                        padding:20
                        spacing:50
                        ScrollView:
                    MDBottomAppBar:
                        MDToolbar:
                            elevation:10
                            mode:"free-end"
                            type:"bottom"
                            icon:"face-woman-outline"
                            MDFlatButton:
                                text:"Back"
                                pos_hint:{"center_x":0.2,"center_y":0.3}
                                on_press:root.manager.current="Main"
    MDNavigationDrawer:
        id:nav_drawer

        BoxLayout:
            size:root.width,root.height
            orientation:"vertical"
            padding:"5dp"
            MDToolbar:
                left_action_items:[["menu-left",lambda x:nav_drawer.set_state()]]
                elevation:8


            Image:
                source:"logo_size.jpg"
                size: self.texture_size
                size_hint:(None,None)
                size:(100,100)
                pos_hint:{"center_x":0.5,"center_y":0.5}

            BoxLayout:
                orientation:"vertical"

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"Profile"
                            IconLeftWidget:
                                icon:"account"
                        OneLineIconListItem:
                            text:"Upload"
                            IconLeftWidget:
                                icon:"upload"
                        OneLineIconListItem:
                            text:"Login"
                            IconLeftWidget:
                                icon:"login"
                MDLabel:
                    text:"Creator:-Yash Jain"
                    size_hint_y:None
                    height:self.texture_size[1]
                    theme_text_color:"Custom"
                    text_color:(0.2,0.7,0.7,1)   
           
<NearbyPolicestation>
    name:"policestation"
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:

                    orientation:"vertical"

                    MDToolbar:
                        title:"PoliceStations:-"
                        left_action_items:[["menu-right",lambda x:nav_drawer.set_state()]]
                        right_action_items:[["clock",lambda x:app.clock_bar()]]
                        elevation:8
                    BoxLayout:
                        orientation:"vertical"
                        padding:20
                        spacing:50
                        ScrollView:
                    MDBottomAppBar:
                        MDToolbar:
                            elevation:10
                            mode:"free-end"
                            type:"bottom"
                            icon:"face-woman-outline"
                            MDFlatButton:
                                text:"Back"
                                pos_hint:{"center_x":0.2,"center_y":0.3}
                                on_press:root.manager.current="Main"
    MDNavigationDrawer:
        id:nav_drawer

        BoxLayout:
            size:root.width,root.height
            orientation:"vertical"
            padding:"5dp"
            MDToolbar:
                left_action_items:[["menu-left",lambda x:nav_drawer.set_state()]]
                elevation:8


            Image:
                source:"logo_size.jpg"
                size: self.texture_size
                size_hint:(None,None)
                size:(100,100)
                pos_hint:{"center_x":0.5,"center_y":0.5}

            BoxLayout:
                orientation:"vertical"

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"Profile"
                            IconLeftWidget:
                                icon:"account"
                        OneLineIconListItem:
                            text:"Upload"
                            IconLeftWidget:
                                icon:"upload"
                        OneLineIconListItem:
                            text:"Login"
                            IconLeftWidget:
                                icon:"login"
                MDLabel:
                    text:"Creator:-Yash Jain"
                    size_hint_y:None
                    height:self.texture_size[1]
                    theme_text_color:"Custom"
                    text_color:(0.2,0.7,0.7,1)   
            
<HelpLineNumbers>
    name:"helpline"
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:

                    orientation:"vertical"

                    MDToolbar:
                        title:"HelplineNumbers:-"
                        left_action_items:[["menu-right",lambda x:nav_drawer.set_state()]]
                        right_action_items:[["clock",lambda x:app.clock_bar()]]
                        elevation:8
                    BoxLayout:
                        orientation:"vertical"
                        padding:20
                        spacing:50
                        ScrollView:
                        MDList:
                            TwoLineAvatarListItem:
                                text:"1. PRACTICE AWARENESS"
                                secondary_text:"Self-defense is awareness"
                                ImageLeftWidget:
                                    source:"Womensafety/img2.jpg"
                            TwoLineAvatarListItem:
                                text:"1. PRACTICE AWARENESS"
                                secondary_text:"Self-defense is awareness"
                                ImageLeftWidget:
                                    source:"Womensafety/img2.jpg"
                            TwoLineAvatarListItem:
                                text:"1. PRACTICE AWARENESS"
                                secondary_text:"Self-defense is awareness"
                                ImageLeftWidget:
                                    source:"Womensafety/img2.jpg"
                    MDBottomAppBar:
                        MDToolbar:
                            elevation:10
                            mode:"end"
                            type:"bottom"
                            icon:"face-woman-outline"
                            on_action_button:app.botton_icon()
                            MDFlatButton:
                                text:"Back"
                                pos_hint:{"center_x":0.2,"center_y":0.3}
                                on_press:root.manager.current="Main"
    MDNavigationDrawer:
        id:nav_drawer

        BoxLayout:
            size:root.width,root.height
            orientation:"vertical"
            padding:"5dp"
            MDToolbar:
                left_action_items:[["menu-left",lambda x:nav_drawer.set_state()]]
                elevation:8


            Image:
                source:"logo_size.jpg"
                size: self.texture_size
                size_hint:(None,None)
                size:(100,100)
                pos_hint:{"center_x":0.5,"center_y":0.5}

            BoxLayout:
                orientation:"vertical"

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"Profile"
                            IconLeftWidget:
                                icon:"account"
                        OneLineIconListItem:
                            text:"Upload"
                            IconLeftWidget:
                                icon:"upload"
                        OneLineIconListItem:
                            text:"Login"
                            IconLeftWidget:
                                icon:"login"
                MDLabel:
                    text:"Creator:-Yash Jain"
                    size_hint_y:None
                    height:self.texture_size[1]
                    theme_text_color:"Custom"
                    text_color:(1,0,0)

"""
