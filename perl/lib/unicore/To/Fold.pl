# !!!!!!!   DO NOT EDIT THIS FILE   !!!!!!!
# This file is machine-generated by mktables from the Unicode
# database, Version 7.0.0.  Any changes made here will be lost!

# !!!!!!!   IT IS DEPRECATED TO USE THIS FILE   !!!!!!!

# This file is for internal use by core Perl only.  It is retained for
# backwards compatibility with applications that may have come to rely on it,
# but its format and even its name or existence are subject to change without
# notice in a future Perl version.  Don't use it directly.  Instead, its
# contents are now retrievable through a stable API in the Unicode::UCD
# module: Unicode::UCD::prop_invmap('Case_Folding') (Values for individual
# code points can be retrieved via Unicode::UCD::charprop());



# The name this swash is to be known by, with the format of the mappings in
# the main body of the table, and what all code points missing from this file
# map to.
$utf8::SwashInfo{'ToFold'}{'format'} = 'x'; # non-negative hex whole number; a code point
$utf8::SwashInfo{'ToFold'}{'specials_name'} = 'utf8::ToSpecFold'; # Name of hash of special mappings
$utf8::SwashInfo{'ToFold'}{'missing'} = '<code point>'; # code point maps to itself

# Some code points require special handling because their mappings are each to
# multiple code points.  These do not appear in the main body, but are defined
# in the hash below.

# Each key is the string of N bytes that together make up the UTF-8 encoding
# for the code point.  (i.e. the same as looking at the code point's UTF-8
# under "use bytes").  Each value is the UTF-8 of the translation, for speed.
%utf8::ToSpecFold = (
"\xC3\x9F" => "\x{0073}\x{0073}",             # U+00DF => 0073 0073
"\xC4\xB0" => "\x{0069}\x{0307}",             # U+0130 => 0069 0307
"\xC5\x89" => "\x{02BC}\x{006E}",             # U+0149 => 02BC 006E
"\xC7\xB0" => "\x{006A}\x{030C}",             # U+01F0 => 006A 030C
"\xCE\x90" => "\x{03B9}\x{0308}\x{0301}",     # U+0390 => 03B9 0308 0301
"\xCE\xB0" => "\x{03C5}\x{0308}\x{0301}",     # U+03B0 => 03C5 0308 0301
"\xD6\x87" => "\x{0565}\x{0582}",             # U+0587 => 0565 0582
"\xE1\xBA\x96" => "\x{0068}\x{0331}",         # U+1E96 => 0068 0331
"\xE1\xBA\x97" => "\x{0074}\x{0308}",         # U+1E97 => 0074 0308
"\xE1\xBA\x98" => "\x{0077}\x{030A}",         # U+1E98 => 0077 030A
"\xE1\xBA\x99" => "\x{0079}\x{030A}",         # U+1E99 => 0079 030A
"\xE1\xBA\x9A" => "\x{0061}\x{02BE}",         # U+1E9A => 0061 02BE
"\xE1\xBA\x9E" => "\x{0073}\x{0073}",         # U+1E9E => 0073 0073
"\xE1\xBD\x90" => "\x{03C5}\x{0313}",         # U+1F50 => 03C5 0313
"\xE1\xBD\x92" => "\x{03C5}\x{0313}\x{0300}", # U+1F52 => 03C5 0313 0300
"\xE1\xBD\x94" => "\x{03C5}\x{0313}\x{0301}", # U+1F54 => 03C5 0313 0301
"\xE1\xBD\x96" => "\x{03C5}\x{0313}\x{0342}", # U+1F56 => 03C5 0313 0342
"\xE1\xBE\x80" => "\x{1F00}\x{03B9}",         # U+1F80 => 1F00 03B9
"\xE1\xBE\x81" => "\x{1F01}\x{03B9}",         # U+1F81 => 1F01 03B9
"\xE1\xBE\x82" => "\x{1F02}\x{03B9}",         # U+1F82 => 1F02 03B9
"\xE1\xBE\x83" => "\x{1F03}\x{03B9}",         # U+1F83 => 1F03 03B9
"\xE1\xBE\x84" => "\x{1F04}\x{03B9}",         # U+1F84 => 1F04 03B9
"\xE1\xBE\x85" => "\x{1F05}\x{03B9}",         # U+1F85 => 1F05 03B9
"\xE1\xBE\x86" => "\x{1F06}\x{03B9}",         # U+1F86 => 1F06 03B9
"\xE1\xBE\x87" => "\x{1F07}\x{03B9}",         # U+1F87 => 1F07 03B9
"\xE1\xBE\x88" => "\x{1F00}\x{03B9}",         # U+1F88 => 1F00 03B9
"\xE1\xBE\x89" => "\x{1F01}\x{03B9}",         # U+1F89 => 1F01 03B9
"\xE1\xBE\x8A" => "\x{1F02}\x{03B9}",         # U+1F8A => 1F02 03B9
"\xE1\xBE\x8B" => "\x{1F03}\x{03B9}",         # U+1F8B => 1F03 03B9
"\xE1\xBE\x8C" => "\x{1F04}\x{03B9}",         # U+1F8C => 1F04 03B9
"\xE1\xBE\x8D" => "\x{1F05}\x{03B9}",         # U+1F8D => 1F05 03B9
"\xE1\xBE\x8E" => "\x{1F06}\x{03B9}",         # U+1F8E => 1F06 03B9
"\xE1\xBE\x8F" => "\x{1F07}\x{03B9}",         # U+1F8F => 1F07 03B9
"\xE1\xBE\x90" => "\x{1F20}\x{03B9}",         # U+1F90 => 1F20 03B9
"\xE1\xBE\x91" => "\x{1F21}\x{03B9}",         # U+1F91 => 1F21 03B9
"\xE1\xBE\x92" => "\x{1F22}\x{03B9}",         # U+1F92 => 1F22 03B9
"\xE1\xBE\x93" => "\x{1F23}\x{03B9}",         # U+1F93 => 1F23 03B9
"\xE1\xBE\x94" => "\x{1F24}\x{03B9}",         # U+1F94 => 1F24 03B9
"\xE1\xBE\x95" => "\x{1F25}\x{03B9}",         # U+1F95 => 1F25 03B9
"\xE1\xBE\x96" => "\x{1F26}\x{03B9}",         # U+1F96 => 1F26 03B9
"\xE1\xBE\x97" => "\x{1F27}\x{03B9}",         # U+1F97 => 1F27 03B9
"\xE1\xBE\x98" => "\x{1F20}\x{03B9}",         # U+1F98 => 1F20 03B9
"\xE1\xBE\x99" => "\x{1F21}\x{03B9}",         # U+1F99 => 1F21 03B9
"\xE1\xBE\x9A" => "\x{1F22}\x{03B9}",         # U+1F9A => 1F22 03B9
"\xE1\xBE\x9B" => "\x{1F23}\x{03B9}",         # U+1F9B => 1F23 03B9
"\xE1\xBE\x9C" => "\x{1F24}\x{03B9}",         # U+1F9C => 1F24 03B9
"\xE1\xBE\x9D" => "\x{1F25}\x{03B9}",         # U+1F9D => 1F25 03B9
"\xE1\xBE\x9E" => "\x{1F26}\x{03B9}",         # U+1F9E => 1F26 03B9
"\xE1\xBE\x9F" => "\x{1F27}\x{03B9}",         # U+1F9F => 1F27 03B9
"\xE1\xBE\xA0" => "\x{1F60}\x{03B9}",         # U+1FA0 => 1F60 03B9
"\xE1\xBE\xA1" => "\x{1F61}\x{03B9}",         # U+1FA1 => 1F61 03B9
"\xE1\xBE\xA2" => "\x{1F62}\x{03B9}",         # U+1FA2 => 1F62 03B9
"\xE1\xBE\xA3" => "\x{1F63}\x{03B9}",         # U+1FA3 => 1F63 03B9
"\xE1\xBE\xA4" => "\x{1F64}\x{03B9}",         # U+1FA4 => 1F64 03B9
"\xE1\xBE\xA5" => "\x{1F65}\x{03B9}",         # U+1FA5 => 1F65 03B9
"\xE1\xBE\xA6" => "\x{1F66}\x{03B9}",         # U+1FA6 => 1F66 03B9
"\xE1\xBE\xA7" => "\x{1F67}\x{03B9}",         # U+1FA7 => 1F67 03B9
"\xE1\xBE\xA8" => "\x{1F60}\x{03B9}",         # U+1FA8 => 1F60 03B9
"\xE1\xBE\xA9" => "\x{1F61}\x{03B9}",         # U+1FA9 => 1F61 03B9
"\xE1\xBE\xAA" => "\x{1F62}\x{03B9}",         # U+1FAA => 1F62 03B9
"\xE1\xBE\xAB" => "\x{1F63}\x{03B9}",         # U+1FAB => 1F63 03B9
"\xE1\xBE\xAC" => "\x{1F64}\x{03B9}",         # U+1FAC => 1F64 03B9
"\xE1\xBE\xAD" => "\x{1F65}\x{03B9}",         # U+1FAD => 1F65 03B9
"\xE1\xBE\xAE" => "\x{1F66}\x{03B9}",         # U+1FAE => 1F66 03B9
"\xE1\xBE\xAF" => "\x{1F67}\x{03B9}",         # U+1FAF => 1F67 03B9
"\xE1\xBE\xB2" => "\x{1F70}\x{03B9}",         # U+1FB2 => 1F70 03B9
"\xE1\xBE\xB3" => "\x{03B1}\x{03B9}",         # U+1FB3 => 03B1 03B9
"\xE1\xBE\xB4" => "\x{03AC}\x{03B9}",         # U+1FB4 => 03AC 03B9
"\xE1\xBE\xB6" => "\x{03B1}\x{0342}",         # U+1FB6 => 03B1 0342
"\xE1\xBE\xB7" => "\x{03B1}\x{0342}\x{03B9}", # U+1FB7 => 03B1 0342 03B9
"\xE1\xBE\xBC" => "\x{03B1}\x{03B9}",         # U+1FBC => 03B1 03B9
"\xE1\xBF\x82" => "\x{1F74}\x{03B9}",         # U+1FC2 => 1F74 03B9
"\xE1\xBF\x83" => "\x{03B7}\x{03B9}",         # U+1FC3 => 03B7 03B9
"\xE1\xBF\x84" => "\x{03AE}\x{03B9}",         # U+1FC4 => 03AE 03B9
"\xE1\xBF\x86" => "\x{03B7}\x{0342}",         # U+1FC6 => 03B7 0342
"\xE1\xBF\x87" => "\x{03B7}\x{0342}\x{03B9}", # U+1FC7 => 03B7 0342 03B9
"\xE1\xBF\x8C" => "\x{03B7}\x{03B9}",         # U+1FCC => 03B7 03B9
"\xE1\xBF\x92" => "\x{03B9}\x{0308}\x{0300}", # U+1FD2 => 03B9 0308 0300
"\xE1\xBF\x93" => "\x{03B9}\x{0308}\x{0301}", # U+1FD3 => 03B9 0308 0301
"\xE1\xBF\x96" => "\x{03B9}\x{0342}",         # U+1FD6 => 03B9 0342
"\xE1\xBF\x97" => "\x{03B9}\x{0308}\x{0342}", # U+1FD7 => 03B9 0308 0342
"\xE1\xBF\xA2" => "\x{03C5}\x{0308}\x{0300}", # U+1FE2 => 03C5 0308 0300
"\xE1\xBF\xA3" => "\x{03C5}\x{0308}\x{0301}", # U+1FE3 => 03C5 0308 0301
"\xE1\xBF\xA4" => "\x{03C1}\x{0313}",         # U+1FE4 => 03C1 0313
"\xE1\xBF\xA6" => "\x{03C5}\x{0342}",         # U+1FE6 => 03C5 0342
"\xE1\xBF\xA7" => "\x{03C5}\x{0308}\x{0342}", # U+1FE7 => 03C5 0308 0342
"\xE1\xBF\xB2" => "\x{1F7C}\x{03B9}",         # U+1FF2 => 1F7C 03B9
"\xE1\xBF\xB3" => "\x{03C9}\x{03B9}",         # U+1FF3 => 03C9 03B9
"\xE1\xBF\xB4" => "\x{03CE}\x{03B9}",         # U+1FF4 => 03CE 03B9
"\xE1\xBF\xB6" => "\x{03C9}\x{0342}",         # U+1FF6 => 03C9 0342
"\xE1\xBF\xB7" => "\x{03C9}\x{0342}\x{03B9}", # U+1FF7 => 03C9 0342 03B9
"\xE1\xBF\xBC" => "\x{03C9}\x{03B9}",         # U+1FFC => 03C9 03B9
"\xEF\xAC\x80" => "\x{0066}\x{0066}",         # U+FB00 => 0066 0066
"\xEF\xAC\x81" => "\x{0066}\x{0069}",         # U+FB01 => 0066 0069
"\xEF\xAC\x82" => "\x{0066}\x{006C}",         # U+FB02 => 0066 006C
"\xEF\xAC\x83" => "\x{0066}\x{0066}\x{0069}", # U+FB03 => 0066 0066 0069
"\xEF\xAC\x84" => "\x{0066}\x{0066}\x{006C}", # U+FB04 => 0066 0066 006C
"\xEF\xAC\x85" => "\x{0073}\x{0074}",         # U+FB05 => 0073 0074
"\xEF\xAC\x86" => "\x{0073}\x{0074}",         # U+FB06 => 0073 0074
"\xEF\xAC\x93" => "\x{0574}\x{0576}",         # U+FB13 => 0574 0576
"\xEF\xAC\x94" => "\x{0574}\x{0565}",         # U+FB14 => 0574 0565
"\xEF\xAC\x95" => "\x{0574}\x{056B}",         # U+FB15 => 0574 056B
"\xEF\xAC\x96" => "\x{057E}\x{0576}",         # U+FB16 => 057E 0576
"\xEF\xAC\x97" => "\x{0574}\x{056D}",         # U+FB17 => 0574 056D
);

return <<'END';
0041		0061
0042		0062
0043		0063
0044		0064
0045		0065
0046		0066
0047		0067
0048		0068
0049		0069
004A		006A
004B		006B
004C		006C
004D		006D
004E		006E
004F		006F
0050		0070
0051		0071
0052		0072
0053		0073
0054		0074
0055		0075
0056		0076
0057		0077
0058		0078
0059		0079
005A		007A
00B5		03BC
00C0		00E0
00C1		00E1
00C2		00E2
00C3		00E3
00C4		00E4
00C5		00E5
00C6		00E6
00C7		00E7
00C8		00E8
00C9		00E9
00CA		00EA
00CB		00EB
00CC		00EC
00CD		00ED
00CE		00EE
00CF		00EF
00D0		00F0
00D1		00F1
00D2		00F2
00D3		00F3
00D4		00F4
00D5		00F5
00D6		00F6
00D8		00F8
00D9		00F9
00DA		00FA
00DB		00FB
00DC		00FC
00DD		00FD
00DE		00FE
0100		0101
0102		0103
0104		0105
0106		0107
0108		0109
010A		010B
010C		010D
010E		010F
0110		0111
0112		0113
0114		0115
0116		0117
0118		0119
011A		011B
011C		011D
011E		011F
0120		0121
0122		0123
0124		0125
0126		0127
0128		0129
012A		012B
012C		012D
012E		012F
0132		0133
0134		0135
0136		0137
0139		013A
013B		013C
013D		013E
013F		0140
0141		0142
0143		0144
0145		0146
0147		0148
014A		014B
014C		014D
014E		014F
0150		0151
0152		0153
0154		0155
0156		0157
0158		0159
015A		015B
015C		015D
015E		015F
0160		0161
0162		0163
0164		0165
0166		0167
0168		0169
016A		016B
016C		016D
016E		016F
0170		0171
0172		0173
0174		0175
0176		0177
0178		00FF
0179		017A
017B		017C
017D		017E
017F		0073
0181		0253
0182		0183
0184		0185
0186		0254
0187		0188
0189		0256
018A		0257
018B		018C
018E		01DD
018F		0259
0190		025B
0191		0192
0193		0260
0194		0263
0196		0269
0197		0268
0198		0199
019C		026F
019D		0272
019F		0275
01A0		01A1
01A2		01A3
01A4		01A5
01A6		0280
01A7		01A8
01A9		0283
01AC		01AD
01AE		0288
01AF		01B0
01B1		028A
01B2		028B
01B3		01B4
01B5		01B6
01B7		0292
01B8		01B9
01BC		01BD
01C4		01C6
01C5		01C6
01C7		01C9
01C8		01C9
01CA		01CC
01CB		01CC
01CD		01CE
01CF		01D0
01D1		01D2
01D3		01D4
01D5		01D6
01D7		01D8
01D9		01DA
01DB		01DC
01DE		01DF
01E0		01E1
01E2		01E3
01E4		01E5
01E6		01E7
01E8		01E9
01EA		01EB
01EC		01ED
01EE		01EF
01F1		01F3
01F2		01F3
01F4		01F5
01F6		0195
01F7		01BF
01F8		01F9
01FA		01FB
01FC		01FD
01FE		01FF
0200		0201
0202		0203
0204		0205
0206		0207
0208		0209
020A		020B
020C		020D
020E		020F
0210		0211
0212		0213
0214		0215
0216		0217
0218		0219
021A		021B
021C		021D
021E		021F
0220		019E
0222		0223
0224		0225
0226		0227
0228		0229
022A		022B
022C		022D
022E		022F
0230		0231
0232		0233
023A		2C65
023B		023C
023D		019A
023E		2C66
0241		0242
0243		0180
0244		0289
0245		028C
0246		0247
0248		0249
024A		024B
024C		024D
024E		024F
0345		03B9
0370		0371
0372		0373
0376		0377
037F		03F3
0386		03AC
0388		03AD
0389		03AE
038A		03AF
038C		03CC
038E		03CD
038F		03CE
0391		03B1
0392		03B2
0393		03B3
0394		03B4
0395		03B5
0396		03B6
0397		03B7
0398		03B8
0399		03B9
039A		03BA
039B		03BB
039C		03BC
039D		03BD
039E		03BE
039F		03BF
03A0		03C0
03A1		03C1
03A3		03C3
03A4		03C4
03A5		03C5
03A6		03C6
03A7		03C7
03A8		03C8
03A9		03C9
03AA		03CA
03AB		03CB
03C2		03C3
03CF		03D7
03D0		03B2
03D1		03B8
03D5		03C6
03D6		03C0
03D8		03D9
03DA		03DB
03DC		03DD
03DE		03DF
03E0		03E1
03E2		03E3
03E4		03E5
03E6		03E7
03E8		03E9
03EA		03EB
03EC		03ED
03EE		03EF
03F0		03BA
03F1		03C1
03F4		03B8
03F5		03B5
03F7		03F8
03F9		03F2
03FA		03FB
03FD		037B
03FE		037C
03FF		037D
0400		0450
0401		0451
0402		0452
0403		0453
0404		0454
0405		0455
0406		0456
0407		0457
0408		0458
0409		0459
040A		045A
040B		045B
040C		045C
040D		045D
040E		045E
040F		045F
0410		0430
0411		0431
0412		0432
0413		0433
0414		0434
0415		0435
0416		0436
0417		0437
0418		0438
0419		0439
041A		043A
041B		043B
041C		043C
041D		043D
041E		043E
041F		043F
0420		0440
0421		0441
0422		0442
0423		0443
0424		0444
0425		0445
0426		0446
0427		0447
0428		0448
0429		0449
042A		044A
042B		044B
042C		044C
042D		044D
042E		044E
042F		044F
0460		0461
0462		0463
0464		0465
0466		0467
0468		0469
046A		046B
046C		046D
046E		046F
0470		0471
0472		0473
0474		0475
0476		0477
0478		0479
047A		047B
047C		047D
047E		047F
0480		0481
048A		048B
048C		048D
048E		048F
0490		0491
0492		0493
0494		0495
0496		0497
0498		0499
049A		049B
049C		049D
049E		049F
04A0		04A1
04A2		04A3
04A4		04A5
04A6		04A7
04A8		04A9
04AA		04AB
04AC		04AD
04AE		04AF
04B0		04B1
04B2		04B3
04B4		04B5
04B6		04B7
04B8		04B9
04BA		04BB
04BC		04BD
04BE		04BF
04C0		04CF
04C1		04C2
04C3		04C4
04C5		04C6
04C7		04C8
04C9		04CA
04CB		04CC
04CD		04CE
04D0		04D1
04D2		04D3
04D4		04D5
04D6		04D7
04D8		04D9
04DA		04DB
04DC		04DD
04DE		04DF
04E0		04E1
04E2		04E3
04E4		04E5
04E6		04E7
04E8		04E9
04EA		04EB
04EC		04ED
04EE		04EF
04F0		04F1
04F2		04F3
04F4		04F5
04F6		04F7
04F8		04F9
04FA		04FB
04FC		04FD
04FE		04FF
0500		0501
0502		0503
0504		0505
0506		0507
0508		0509
050A		050B
050C		050D
050E		050F
0510		0511
0512		0513
0514		0515
0516		0517
0518		0519
051A		051B
051C		051D
051E		051F
0520		0521
0522		0523
0524		0525
0526		0527
0528		0529
052A		052B
052C		052D
052E		052F
0531		0561
0532		0562
0533		0563
0534		0564
0535		0565
0536		0566
0537		0567
0538		0568
0539		0569
053A		056A
053B		056B
053C		056C
053D		056D
053E		056E
053F		056F
0540		0570
0541		0571
0542		0572
0543		0573
0544		0574
0545		0575
0546		0576
0547		0577
0548		0578
0549		0579
054A		057A
054B		057B
054C		057C
054D		057D
054E		057E
054F		057F
0550		0580
0551		0581
0552		0582
0553		0583
0554		0584
0555		0585
0556		0586
10A0		2D00
10A1		2D01
10A2		2D02
10A3		2D03
10A4		2D04
10A5		2D05
10A6		2D06
10A7		2D07
10A8		2D08
10A9		2D09
10AA		2D0A
10AB		2D0B
10AC		2D0C
10AD		2D0D
10AE		2D0E
10AF		2D0F
10B0		2D10
10B1		2D11
10B2		2D12
10B3		2D13
10B4		2D14
10B5		2D15
10B6		2D16
10B7		2D17
10B8		2D18
10B9		2D19
10BA		2D1A
10BB		2D1B
10BC		2D1C
10BD		2D1D
10BE		2D1E
10BF		2D1F
10C0		2D20
10C1		2D21
10C2		2D22
10C3		2D23
10C4		2D24
10C5		2D25
10C7		2D27
10CD		2D2D
1E00		1E01
1E02		1E03
1E04		1E05
1E06		1E07
1E08		1E09
1E0A		1E0B
1E0C		1E0D
1E0E		1E0F
1E10		1E11
1E12		1E13
1E14		1E15
1E16		1E17
1E18		1E19
1E1A		1E1B
1E1C		1E1D
1E1E		1E1F
1E20		1E21
1E22		1E23
1E24		1E25
1E26		1E27
1E28		1E29
1E2A		1E2B
1E2C		1E2D
1E2E		1E2F
1E30		1E31
1E32		1E33
1E34		1E35
1E36		1E37
1E38		1E39
1E3A		1E3B
1E3C		1E3D
1E3E		1E3F
1E40		1E41
1E42		1E43
1E44		1E45
1E46		1E47
1E48		1E49
1E4A		1E4B
1E4C		1E4D
1E4E		1E4F
1E50		1E51
1E52		1E53
1E54		1E55
1E56		1E57
1E58		1E59
1E5A		1E5B
1E5C		1E5D
1E5E		1E5F
1E60		1E61
1E62		1E63
1E64		1E65
1E66		1E67
1E68		1E69
1E6A		1E6B
1E6C		1E6D
1E6E		1E6F
1E70		1E71
1E72		1E73
1E74		1E75
1E76		1E77
1E78		1E79
1E7A		1E7B
1E7C		1E7D
1E7E		1E7F
1E80		1E81
1E82		1E83
1E84		1E85
1E86		1E87
1E88		1E89
1E8A		1E8B
1E8C		1E8D
1E8E		1E8F
1E90		1E91
1E92		1E93
1E94		1E95
1E9B		1E61
1E9E		00DF
1EA0		1EA1
1EA2		1EA3
1EA4		1EA5
1EA6		1EA7
1EA8		1EA9
1EAA		1EAB
1EAC		1EAD
1EAE		1EAF
1EB0		1EB1
1EB2		1EB3
1EB4		1EB5
1EB6		1EB7
1EB8		1EB9
1EBA		1EBB
1EBC		1EBD
1EBE		1EBF
1EC0		1EC1
1EC2		1EC3
1EC4		1EC5
1EC6		1EC7
1EC8		1EC9
1ECA		1ECB
1ECC		1ECD
1ECE		1ECF
1ED0		1ED1
1ED2		1ED3
1ED4		1ED5
1ED6		1ED7
1ED8		1ED9
1EDA		1EDB
1EDC		1EDD
1EDE		1EDF
1EE0		1EE1
1EE2		1EE3
1EE4		1EE5
1EE6		1EE7
1EE8		1EE9
1EEA		1EEB
1EEC		1EED
1EEE		1EEF
1EF0		1EF1
1EF2		1EF3
1EF4		1EF5
1EF6		1EF7
1EF8		1EF9
1EFA		1EFB
1EFC		1EFD
1EFE		1EFF
1F08		1F00
1F09		1F01
1F0A		1F02
1F0B		1F03
1F0C		1F04
1F0D		1F05
1F0E		1F06
1F0F		1F07
1F18		1F10
1F19		1F11
1F1A		1F12
1F1B		1F13
1F1C		1F14
1F1D		1F15
1F28		1F20
1F29		1F21
1F2A		1F22
1F2B		1F23
1F2C		1F24
1F2D		1F25
1F2E		1F26
1F2F		1F27
1F38		1F30
1F39		1F31
1F3A		1F32
1F3B		1F33
1F3C		1F34
1F3D		1F35
1F3E		1F36
1F3F		1F37
1F48		1F40
1F49		1F41
1F4A		1F42
1F4B		1F43
1F4C		1F44
1F4D		1F45
1F59		1F51
1F5B		1F53
1F5D		1F55
1F5F		1F57
1F68		1F60
1F69		1F61
1F6A		1F62
1F6B		1F63
1F6C		1F64
1F6D		1F65
1F6E		1F66
1F6F		1F67
1F88		1F80
1F89		1F81
1F8A		1F82
1F8B		1F83
1F8C		1F84
1F8D		1F85
1F8E		1F86
1F8F		1F87
1F98		1F90
1F99		1F91
1F9A		1F92
1F9B		1F93
1F9C		1F94
1F9D		1F95
1F9E		1F96
1F9F		1F97
1FA8		1FA0
1FA9		1FA1
1FAA		1FA2
1FAB		1FA3
1FAC		1FA4
1FAD		1FA5
1FAE		1FA6
1FAF		1FA7
1FB8		1FB0
1FB9		1FB1
1FBA		1F70
1FBB		1F71
1FBC		1FB3
1FBE		03B9
1FC8		1F72
1FC9		1F73
1FCA		1F74
1FCB		1F75
1FCC		1FC3
1FD8		1FD0
1FD9		1FD1
1FDA		1F76
1FDB		1F77
1FE8		1FE0
1FE9		1FE1
1FEA		1F7A
1FEB		1F7B
1FEC		1FE5
1FF8		1F78
1FF9		1F79
1FFA		1F7C
1FFB		1F7D
1FFC		1FF3
2126		03C9
212A		006B
212B		00E5
2132		214E
2160		2170
2161		2171
2162		2172
2163		2173
2164		2174
2165		2175
2166		2176
2167		2177
2168		2178
2169		2179
216A		217A
216B		217B
216C		217C
216D		217D
216E		217E
216F		217F
2183		2184
24B6		24D0
24B7		24D1
24B8		24D2
24B9		24D3
24BA		24D4
24BB		24D5
24BC		24D6
24BD		24D7
24BE		24D8
24BF		24D9
24C0		24DA
24C1		24DB
24C2		24DC
24C3		24DD
24C4		24DE
24C5		24DF
24C6		24E0
24C7		24E1
24C8		24E2
24C9		24E3
24CA		24E4
24CB		24E5
24CC		24E6
24CD		24E7
24CE		24E8
24CF		24E9
2C00		2C30
2C01		2C31
2C02		2C32
2C03		2C33
2C04		2C34
2C05		2C35
2C06		2C36
2C07		2C37
2C08		2C38
2C09		2C39
2C0A		2C3A
2C0B		2C3B
2C0C		2C3C
2C0D		2C3D
2C0E		2C3E
2C0F		2C3F
2C10		2C40
2C11		2C41
2C12		2C42
2C13		2C43
2C14		2C44
2C15		2C45
2C16		2C46
2C17		2C47
2C18		2C48
2C19		2C49
2C1A		2C4A
2C1B		2C4B
2C1C		2C4C
2C1D		2C4D
2C1E		2C4E
2C1F		2C4F
2C20		2C50
2C21		2C51
2C22		2C52
2C23		2C53
2C24		2C54
2C25		2C55
2C26		2C56
2C27		2C57
2C28		2C58
2C29		2C59
2C2A		2C5A
2C2B		2C5B
2C2C		2C5C
2C2D		2C5D
2C2E		2C5E
2C60		2C61
2C62		026B
2C63		1D7D
2C64		027D
2C67		2C68
2C69		2C6A
2C6B		2C6C
2C6D		0251
2C6E		0271
2C6F		0250
2C70		0252
2C72		2C73
2C75		2C76
2C7E		023F
2C7F		0240
2C80		2C81
2C82		2C83
2C84		2C85
2C86		2C87
2C88		2C89
2C8A		2C8B
2C8C		2C8D
2C8E		2C8F
2C90		2C91
2C92		2C93
2C94		2C95
2C96		2C97
2C98		2C99
2C9A		2C9B
2C9C		2C9D
2C9E		2C9F
2CA0		2CA1
2CA2		2CA3
2CA4		2CA5
2CA6		2CA7
2CA8		2CA9
2CAA		2CAB
2CAC		2CAD
2CAE		2CAF
2CB0		2CB1
2CB2		2CB3
2CB4		2CB5
2CB6		2CB7
2CB8		2CB9
2CBA		2CBB
2CBC		2CBD
2CBE		2CBF
2CC0		2CC1
2CC2		2CC3
2CC4		2CC5
2CC6		2CC7
2CC8		2CC9
2CCA		2CCB
2CCC		2CCD
2CCE		2CCF
2CD0		2CD1
2CD2		2CD3
2CD4		2CD5
2CD6		2CD7
2CD8		2CD9
2CDA		2CDB
2CDC		2CDD
2CDE		2CDF
2CE0		2CE1
2CE2		2CE3
2CEB		2CEC
2CED		2CEE
2CF2		2CF3
A640		A641
A642		A643
A644		A645
A646		A647
A648		A649
A64A		A64B
A64C		A64D
A64E		A64F
A650		A651
A652		A653
A654		A655
A656		A657
A658		A659
A65A		A65B
A65C		A65D
A65E		A65F
A660		A661
A662		A663
A664		A665
A666		A667
A668		A669
A66A		A66B
A66C		A66D
A680		A681
A682		A683
A684		A685
A686		A687
A688		A689
A68A		A68B
A68C		A68D
A68E		A68F
A690		A691
A692		A693
A694		A695
A696		A697
A698		A699
A69A		A69B
A722		A723
A724		A725
A726		A727
A728		A729
A72A		A72B
A72C		A72D
A72E		A72F
A732		A733
A734		A735
A736		A737
A738		A739
A73A		A73B
A73C		A73D
A73E		A73F
A740		A741
A742		A743
A744		A745
A746		A747
A748		A749
A74A		A74B
A74C		A74D
A74E		A74F
A750		A751
A752		A753
A754		A755
A756		A757
A758		A759
A75A		A75B
A75C		A75D
A75E		A75F
A760		A761
A762		A763
A764		A765
A766		A767
A768		A769
A76A		A76B
A76C		A76D
A76E		A76F
A779		A77A
A77B		A77C
A77D		1D79
A77E		A77F
A780		A781
A782		A783
A784		A785
A786		A787
A78B		A78C
A78D		0265
A790		A791
A792		A793
A796		A797
A798		A799
A79A		A79B
A79C		A79D
A79E		A79F
A7A0		A7A1
A7A2		A7A3
A7A4		A7A5
A7A6		A7A7
A7A8		A7A9
A7AA		0266
A7AB		025C
A7AC		0261
A7AD		026C
A7B0		029E
A7B1		0287
FF21		FF41
FF22		FF42
FF23		FF43
FF24		FF44
FF25		FF45
FF26		FF46
FF27		FF47
FF28		FF48
FF29		FF49
FF2A		FF4A
FF2B		FF4B
FF2C		FF4C
FF2D		FF4D
FF2E		FF4E
FF2F		FF4F
FF30		FF50
FF31		FF51
FF32		FF52
FF33		FF53
FF34		FF54
FF35		FF55
FF36		FF56
FF37		FF57
FF38		FF58
FF39		FF59
FF3A		FF5A
10400		10428
10401		10429
10402		1042A
10403		1042B
10404		1042C
10405		1042D
10406		1042E
10407		1042F
10408		10430
10409		10431
1040A		10432
1040B		10433
1040C		10434
1040D		10435
1040E		10436
1040F		10437
10410		10438
10411		10439
10412		1043A
10413		1043B
10414		1043C
10415		1043D
10416		1043E
10417		1043F
10418		10440
10419		10441
1041A		10442
1041B		10443
1041C		10444
1041D		10445
1041E		10446
1041F		10447
10420		10448
10421		10449
10422		1044A
10423		1044B
10424		1044C
10425		1044D
10426		1044E
10427		1044F
118A0		118C0
118A1		118C1
118A2		118C2
118A3		118C3
118A4		118C4
118A5		118C5
118A6		118C6
118A7		118C7
118A8		118C8
118A9		118C9
118AA		118CA
118AB		118CB
118AC		118CC
118AD		118CD
118AE		118CE
118AF		118CF
118B0		118D0
118B1		118D1
118B2		118D2
118B3		118D3
118B4		118D4
118B5		118D5
118B6		118D6
118B7		118D7
118B8		118D8
118B9		118D9
118BA		118DA
118BB		118DB
118BC		118DC
118BD		118DD
118BE		118DE
118BF		118DF
END
