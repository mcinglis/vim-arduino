

runtime! syntax/cpp.vim


syntax keyword arduinoConstant
            \ BIN CHANGE DEC DEFAULT EXTERNAL FALLING HALF_PI HEX HIGH INPUT
            \ INPUT_PULLUP INTERNAL INTERNAL1V1 INTERNAL2V56 LED_BUILTIN
            \ LOW LSBFIRST MSBFIRST OCT OUTPUT PI RISING TWO_PI

syntax keyword arduinoType
            \ EthernetClient EthernetUDP IPAddress EthernetServer String
            \ SoftwareSerial boolean byte word

syntax keyword arduinoModule
            \ Ethernet Keyboard Mouse Serial Serial1 Serial2 Serial3

syntax keyword arduinoFunc
            \ abs accept acos analogRead analogReference analogWrite asin atan
            \ atan2 attachInterrupt available begin bit bitClear bitRead bitSet
            \ bitWrite ceil click constrain cos degrees delay
            \ delayMicroseconds detachInterrupt digitalRead digitalWrite end
            \ exp find findUntil floor flush highByte interrupts isPressed
            \ log loop lowByte map max micros millis min move noInterrupts
            \ noTone parseFloat parseInt peek pinMode press print println
            \ pulseIn radians random randomSeed read readBytes readBytesUntil
            \ readString readStringUntil release releaseAll round setup
            \ setTimeout shiftIn shiftOut sin sq sqrt tan tone


highlight default link arduinoType      Type
highlight default link arduinoConstant  Constant
highlight default link arduinoFunc      Function
highlight default link arduinoModule    Identifier

