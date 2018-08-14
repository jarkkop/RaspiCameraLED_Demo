*** Settings ***
Library    bluetoothscreencontroller.py
Library    snapandanalyse.py
Suite Setup       Connect To Unit Via Bluetooth
Suite Teardown    Unit Screen Clear And Disconnect

*** Variables ***
${TARGET_BLUETOOTH_ADDRESS}    B8:27:EB:92:F8:D2

${PATTERN_ONE}    10000001\01000010\00100100\00011000\00011000\00100100\01000010\10000001
${PATTERN_TWO}    00000000\00100100\00100100\00000000\01000010\00111100
${PATTERN_HEART}  00000000\01100110\11111111\11111111\11111111\01111110\00111100\00011000
${PATTERN_A}      00000000\00011000\00100100\00100100\00111100\00100100\00100100\00000000
${PATTERN_B}      01111000\01001000\01001000\01110000\01001000\01000100\01000100\01111100
${PATTERN_C}      00000000\00011110\00100000\01000000\01000000\01000000\00100000\00011110
${PATTERN_D}      00000000\00111000\00100100\00100010\00100010\00100100\00111000\00000000
${PATTERN_E}      00000000\00111100\00100000\00111000\00100000\00100000\00111100\00000000
${PATTERN_F}      00000000\00111100\00100000\00111000\00100000\00100000\00100000\00000000
${PATTERN_G}      00000000\00111110\00100000\00100000\00101110\00100010\00111110\00000000
${PATTERN_H}      00000000\00100100\00100100\00111100\00100100\00100100\00100100\00000000
${PATTERN_I}      00000000\00111000\00010000\00010000\00010000\00010000\00111000\00000000
#byte J[] = {B00000000,B00011100,B00001000,B00001000,B00001000,B00101000,B00111000,B00000000};
#byte K[] = {B00000000,B00100100,B00101000,B00110000,B00101000,B00100100,B00100100,B00000000};
#byte L[] = {B00000000,B00100000,B00100000,B00100000,B00100000,B00100000,B00111100,B00000000};
#byte M[] = {B00000000,B00000000,B01000100,B10101010,B10010010,B10000010,B10000010,B00000000};
#byte N[] = {B00000000,B00100010,B00110010,B00101010,B00100110,B00100010,B00000000,B00000000};
#byte O[] = {B00000000,B00111100,B01000010,B01000010,B01000010,B01000010,B00111100,B00000000};
#byte P[] = {B00000000,B00111000,B00100100,B00100100,B00111000,B00100000,B00100000,B00000000};
#byte Q[] = {B00000000,B00111100,B01000010,B01000010,B01000010,B01000110,B00111110,B00000001};
#byte R[] = {B00000000,B00111000,B00100100,B00100100,B00111000,B00100100,B00100100,B00000000};
#byte S[] = {B00000000,B00111100,B00100000,B00111100,B00000100,B00000100,B00111100,B00000000};
#byte T[] = {B00000000,B01111100,B00010000,B00010000,B00010000,B00010000,B00010000,B00000000};
#byte U[] = {B00000000,B01000010,B01000010,B01000010,B01000010,B00100100,B00011000,B00000000};
#byte V[] = {B00000000,B00100010,B00100010,B00100010,B00010100,B00010100,B00001000,B00000000};
#byte W[] = {B00000000,B10000010,B10010010,B01010100,B01010100,B00101000,B00000000,B00000000};
#byte X[] = {B00000000,B01000010,B00100100,B00011000,B00011000,B00100100,B01000010,B00000000};
#byte Y[] = {B00000000,B01000100,B00101000,B00010000,B00010000,B00010000,B00010000,B00000000};
#byte Z[] = {B00000000,B00111100,B00000100,B00001000,B00010000,B00100000,B00111100,B00000000};


*** Test Cases ***
Connect And LightUp Navy Heart
    [Tags]    pattern    navy    test2
    Send Command    pattern navy heart
    Take Picture    navy.png
    Mask From Color Image    navy.png    navy  
    Analyse Color Mask    mask_navy.png       17

Connect And LightUp Gray Heart
    [Tags]    pattern    gray   
    Send Command    pattern gray heart
    Take Picture    gray.png
    Mask From Color Image    gray.png    gray 
    Analyse Color Mask    mask_gray.png       16

Connect And LightUp Orange Heart Pattern
    [Tags]    pattern    orange      test
    Send Command    pattern orange ${PATTERN_HEART}
    Take Picture    orange_heart.png
    Mask From Color Image    orange_heart.png    orange
    Analyse Color Mask    mask_orange_heart.png    40
 
Connect And LightUp cyan A letter Pattern
    [Tags]    pattern    cyan      test
    Send Command    pattern cyan ${PATTERN_A}
    Take Picture    cyan_A.png
    Mask From Color Image    cyan_A.png    cyan
    Analyse Color Mask    mask_cyan_A.png    14
 
Connect And LightUp navy G letter Pattern
    [Tags]    pattern    navy      test
    Send Command    pattern navy ${PATTERN_G}
    Take Picture    navy_G.png
    Mask From Color Image    navy_G.png    navy
    Analyse Color Mask    mask_navy_G.png    18
 
Connect And LightUp Yellow Heart
     [Tags]    pattern    yellow    test
     Send Command    pattern yellow heart
     Take Picture    yellow.png
     Mask From Color Image    yellow.png    yellow
     Analyse Color Mask    mask_yellow.png       16


Connect And LightUp Red Heart
    [Tags]    pattern    red    test
    Send Command    pattern red heart
    Take Picture    red.png
    Mask From Color Image    red.png    red
    Analyse Color Mask    mask_red.png       16

Connect And LightUp Green Heart
    [Tags]    pattern    green    test
    Send Command    pattern green heart
    Take Picture    green.png
    Mask From Color Image    green.png    green
    Analyse Color Mask    mask_green.png     16

Connect And LightUp Blue Heart
    [Tags]    pattern    blue    test
    Send Command    pattern blue heart
    Take Picture    blue.png
    Mask From Color Image    blue.png    blue
    Analyse Color Mask    mask_blue.png      16

Connect And LightUp Blue Cross Pattern2
    [Tags]    pattern    blue    smile    test
    Send Command    pattern blue ${PATTERN_TWO}
    Take Picture    blue_smile.png
    Mask From Color Image    blue_smile.png    blue
    Analyse Color Mask    mask_blue_smile.png    10

Connect And LightUp Blue Cross Pattern1
    [Tags]    pattern    blue    cross    test
    Send Command    pattern blue ${PATTERN_ONE}
    Take Picture    blue_x.png
    Mask From Color Image    blue_x.png    blue
    Analyse Color Mask    mask_blue_x.png    16

Connect And Fill Screen in Red
    [Tags]    pattern    red     solid    test
    Send Command    line red 64
    Take Picture    s_red.png
    Mask From Color Image    s_red.png    red
    Analyse Color Mask    mask_s_red.png     64

Connect And Fill Screen in Green
    [Tags]    pattern    green    solid   test
    Send Command    line green 64
    Take Picture    s_green.png
    Mask From Color Image    s_green.png    green
    Analyse Color Mask    mask_s_green.png   64

Connect And Fill Screen in All Blue
    [Tags]    pattern    blue    solid    test
    Send Command    line blue 64
    Take Picture    s_blue.png
    Mask From Color Image    s_blue.png   blue     
    Analyse Color Mask    mask_s_blue.png    64

Connect And Fill Screen in Many Colors
    [Tags]    pattern    all    solid    test  
    Send Command    line green 16
    Send Command    line red 16
    Send Command    line blue 16
    Send Command    line green 16
    Take Picture    all.png
    Mask From Color Image    all.png     green
    Analyse Color Mask    mask_all.png       32

*** Keywords ***
Connect To Unit Via Bluetooth
    Connect To Screen    ${TARGET_BLUETOOTH_ADDRESS}

Unit Screen Clear And Disconnect
    Clear Screen
    Disconnect From Screen
