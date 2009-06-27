# $ANTLR 3.0.1 /home/staal/devel/arff/arff.g 2008-01-16 11:17:08

from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EXPONENT=8
FLOAT=5
T29=29
T28=28
T27=27
T26=26
T25=25
EOF=-1
T24=24
T23=23
T22=22
T21=21
T20=20
T38=38
QSTRING=6
T37=37
T39=39
T34=34
T33=33
T36=36
T35=35
T30=30
T32=32
T31=31
LINE_COMMENT=9
INT=4
T43=43
Tokens=45
T42=42
T41=41
T40=40
T44=44
WS=10
T11=11
T12=12
T13=13
T14=14
T15=15
T16=16
T17=17
T18=18
T19=19
STRING=7

class arffLexer(Lexer):

    grammarFileName = "/home/staal/devel/arff/arff.g"

    def __init__(self, input=None):
        Lexer.__init__(self, input)
        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )
        self.dfa18 = self.DFA18(
            self, 18,
            eot = self.DFA18_eot,
            eof = self.DFA18_eof,
            min = self.DFA18_min,
            max = self.DFA18_max,
            accept = self.DFA18_accept,
            special = self.DFA18_special,
            transition = self.DFA18_transition
            )






    # $ANTLR start T11
    def mT11(self, ):

        try:
            self.type = T11

            # /home/staal/devel/arff/arff.g:7:5: ( '@relation' )
            # /home/staal/devel/arff/arff.g:7:7: '@relation'
            self.match("@relation")






        finally:

            pass

    # $ANTLR end T11



    # $ANTLR start T12
    def mT12(self, ):

        try:
            self.type = T12

            # /home/staal/devel/arff/arff.g:8:5: ( '@RELATION' )
            # /home/staal/devel/arff/arff.g:8:7: '@RELATION'
            self.match("@RELATION")






        finally:

            pass

    # $ANTLR end T12



    # $ANTLR start T13
    def mT13(self, ):

        try:
            self.type = T13

            # /home/staal/devel/arff/arff.g:9:5: ( '@Relation' )
            # /home/staal/devel/arff/arff.g:9:7: '@Relation'
            self.match("@Relation")






        finally:

            pass

    # $ANTLR end T13



    # $ANTLR start T14
    def mT14(self, ):

        try:
            self.type = T14

            # /home/staal/devel/arff/arff.g:10:5: ( '@attribute' )
            # /home/staal/devel/arff/arff.g:10:7: '@attribute'
            self.match("@attribute")






        finally:

            pass

    # $ANTLR end T14



    # $ANTLR start T15
    def mT15(self, ):

        try:
            self.type = T15

            # /home/staal/devel/arff/arff.g:11:5: ( '@Attribute' )
            # /home/staal/devel/arff/arff.g:11:7: '@Attribute'
            self.match("@Attribute")






        finally:

            pass

    # $ANTLR end T15



    # $ANTLR start T16
    def mT16(self, ):

        try:
            self.type = T16

            # /home/staal/devel/arff/arff.g:12:5: ( '@ATTRIBUTE' )
            # /home/staal/devel/arff/arff.g:12:7: '@ATTRIBUTE'
            self.match("@ATTRIBUTE")






        finally:

            pass

    # $ANTLR end T16



    # $ANTLR start T17
    def mT17(self, ):

        try:
            self.type = T17

            # /home/staal/devel/arff/arff.g:13:5: ( 'numeric' )
            # /home/staal/devel/arff/arff.g:13:7: 'numeric'
            self.match("numeric")






        finally:

            pass

    # $ANTLR end T17



    # $ANTLR start T18
    def mT18(self, ):

        try:
            self.type = T18

            # /home/staal/devel/arff/arff.g:14:5: ( 'Numeric' )
            # /home/staal/devel/arff/arff.g:14:7: 'Numeric'
            self.match("Numeric")






        finally:

            pass

    # $ANTLR end T18



    # $ANTLR start T19
    def mT19(self, ):

        try:
            self.type = T19

            # /home/staal/devel/arff/arff.g:15:5: ( 'NUMERIC' )
            # /home/staal/devel/arff/arff.g:15:7: 'NUMERIC'
            self.match("NUMERIC")






        finally:

            pass

    # $ANTLR end T19



    # $ANTLR start T20
    def mT20(self, ):

        try:
            self.type = T20

            # /home/staal/devel/arff/arff.g:16:5: ( 'integer' )
            # /home/staal/devel/arff/arff.g:16:7: 'integer'
            self.match("integer")






        finally:

            pass

    # $ANTLR end T20



    # $ANTLR start T21
    def mT21(self, ):

        try:
            self.type = T21

            # /home/staal/devel/arff/arff.g:17:5: ( 'Integer' )
            # /home/staal/devel/arff/arff.g:17:7: 'Integer'
            self.match("Integer")






        finally:

            pass

    # $ANTLR end T21



    # $ANTLR start T22
    def mT22(self, ):

        try:
            self.type = T22

            # /home/staal/devel/arff/arff.g:18:5: ( 'INTEGER' )
            # /home/staal/devel/arff/arff.g:18:7: 'INTEGER'
            self.match("INTEGER")






        finally:

            pass

    # $ANTLR end T22



    # $ANTLR start T23
    def mT23(self, ):

        try:
            self.type = T23

            # /home/staal/devel/arff/arff.g:19:5: ( 'real' )
            # /home/staal/devel/arff/arff.g:19:7: 'real'
            self.match("real")






        finally:

            pass

    # $ANTLR end T23



    # $ANTLR start T24
    def mT24(self, ):

        try:
            self.type = T24

            # /home/staal/devel/arff/arff.g:20:5: ( 'Real' )
            # /home/staal/devel/arff/arff.g:20:7: 'Real'
            self.match("Real")






        finally:

            pass

    # $ANTLR end T24



    # $ANTLR start T25
    def mT25(self, ):

        try:
            self.type = T25

            # /home/staal/devel/arff/arff.g:21:5: ( 'REAL' )
            # /home/staal/devel/arff/arff.g:21:7: 'REAL'
            self.match("REAL")






        finally:

            pass

    # $ANTLR end T25



    # $ANTLR start T26
    def mT26(self, ):

        try:
            self.type = T26

            # /home/staal/devel/arff/arff.g:22:5: ( 'string' )
            # /home/staal/devel/arff/arff.g:22:7: 'string'
            self.match("string")






        finally:

            pass

    # $ANTLR end T26



    # $ANTLR start T27
    def mT27(self, ):

        try:
            self.type = T27

            # /home/staal/devel/arff/arff.g:23:5: ( 'String' )
            # /home/staal/devel/arff/arff.g:23:7: 'String'
            self.match("String")






        finally:

            pass

    # $ANTLR end T27



    # $ANTLR start T28
    def mT28(self, ):

        try:
            self.type = T28

            # /home/staal/devel/arff/arff.g:24:5: ( 'STRING' )
            # /home/staal/devel/arff/arff.g:24:7: 'STRING'
            self.match("STRING")






        finally:

            pass

    # $ANTLR end T28



    # $ANTLR start T29
    def mT29(self, ):

        try:
            self.type = T29

            # /home/staal/devel/arff/arff.g:25:5: ( 'relational' )
            # /home/staal/devel/arff/arff.g:25:7: 'relational'
            self.match("relational")






        finally:

            pass

    # $ANTLR end T29



    # $ANTLR start T30
    def mT30(self, ):

        try:
            self.type = T30

            # /home/staal/devel/arff/arff.g:26:5: ( 'Relational' )
            # /home/staal/devel/arff/arff.g:26:7: 'Relational'
            self.match("Relational")






        finally:

            pass

    # $ANTLR end T30



    # $ANTLR start T31
    def mT31(self, ):

        try:
            self.type = T31

            # /home/staal/devel/arff/arff.g:27:5: ( 'RELATIONAL' )
            # /home/staal/devel/arff/arff.g:27:7: 'RELATIONAL'
            self.match("RELATIONAL")






        finally:

            pass

    # $ANTLR end T31



    # $ANTLR start T32
    def mT32(self, ):

        try:
            self.type = T32

            # /home/staal/devel/arff/arff.g:28:5: ( '@end' )
            # /home/staal/devel/arff/arff.g:28:7: '@end'
            self.match("@end")






        finally:

            pass

    # $ANTLR end T32



    # $ANTLR start T33
    def mT33(self, ):

        try:
            self.type = T33

            # /home/staal/devel/arff/arff.g:29:5: ( '@End' )
            # /home/staal/devel/arff/arff.g:29:7: '@End'
            self.match("@End")






        finally:

            pass

    # $ANTLR end T33



    # $ANTLR start T34
    def mT34(self, ):

        try:
            self.type = T34

            # /home/staal/devel/arff/arff.g:30:5: ( '@END' )
            # /home/staal/devel/arff/arff.g:30:7: '@END'
            self.match("@END")






        finally:

            pass

    # $ANTLR end T34



    # $ANTLR start T35
    def mT35(self, ):

        try:
            self.type = T35

            # /home/staal/devel/arff/arff.g:31:5: ( '{' )
            # /home/staal/devel/arff/arff.g:31:7: '{'
            self.match(u'{')





        finally:

            pass

    # $ANTLR end T35



    # $ANTLR start T36
    def mT36(self, ):

        try:
            self.type = T36

            # /home/staal/devel/arff/arff.g:32:5: ( '}' )
            # /home/staal/devel/arff/arff.g:32:7: '}'
            self.match(u'}')





        finally:

            pass

    # $ANTLR end T36



    # $ANTLR start T37
    def mT37(self, ):

        try:
            self.type = T37

            # /home/staal/devel/arff/arff.g:33:5: ( 'date' )
            # /home/staal/devel/arff/arff.g:33:7: 'date'
            self.match("date")






        finally:

            pass

    # $ANTLR end T37



    # $ANTLR start T38
    def mT38(self, ):

        try:
            self.type = T38

            # /home/staal/devel/arff/arff.g:34:5: ( 'DATE' )
            # /home/staal/devel/arff/arff.g:34:7: 'DATE'
            self.match("DATE")






        finally:

            pass

    # $ANTLR end T38



    # $ANTLR start T39
    def mT39(self, ):

        try:
            self.type = T39

            # /home/staal/devel/arff/arff.g:35:5: ( 'Date' )
            # /home/staal/devel/arff/arff.g:35:7: 'Date'
            self.match("Date")






        finally:

            pass

    # $ANTLR end T39



    # $ANTLR start T40
    def mT40(self, ):

        try:
            self.type = T40

            # /home/staal/devel/arff/arff.g:36:5: ( '@data' )
            # /home/staal/devel/arff/arff.g:36:7: '@data'
            self.match("@data")






        finally:

            pass

    # $ANTLR end T40



    # $ANTLR start T41
    def mT41(self, ):

        try:
            self.type = T41

            # /home/staal/devel/arff/arff.g:37:5: ( '@Data' )
            # /home/staal/devel/arff/arff.g:37:7: '@Data'
            self.match("@Data")






        finally:

            pass

    # $ANTLR end T41



    # $ANTLR start T42
    def mT42(self, ):

        try:
            self.type = T42

            # /home/staal/devel/arff/arff.g:38:5: ( '@DATA' )
            # /home/staal/devel/arff/arff.g:38:7: '@DATA'
            self.match("@DATA")






        finally:

            pass

    # $ANTLR end T42



    # $ANTLR start T43
    def mT43(self, ):

        try:
            self.type = T43

            # /home/staal/devel/arff/arff.g:39:5: ( ',' )
            # /home/staal/devel/arff/arff.g:39:7: ','
            self.match(u',')





        finally:

            pass

    # $ANTLR end T43



    # $ANTLR start T44
    def mT44(self, ):

        try:
            self.type = T44

            # /home/staal/devel/arff/arff.g:40:5: ( '?' )
            # /home/staal/devel/arff/arff.g:40:7: '?'
            self.match(u'?')





        finally:

            pass

    # $ANTLR end T44



    # $ANTLR start INT
    def mINT(self, ):

        try:
            self.type = INT

            # /home/staal/devel/arff/arff.g:351:5: ( ( '+' | '-' )? ( '0' .. '9' )+ )
            # /home/staal/devel/arff/arff.g:351:7: ( '+' | '-' )? ( '0' .. '9' )+
            # /home/staal/devel/arff/arff.g:351:7: ( '+' | '-' )?
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == u'+' or LA1_0 == u'-') :
                alt1 = 1
            if alt1 == 1:
                # /home/staal/devel/arff/arff.g:
                if self.input.LA(1) == u'+' or self.input.LA(1) == u'-':
                    self.input.consume();

                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse





            # /home/staal/devel/arff/arff.g:351:19: ( '0' .. '9' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((u'0' <= LA2_0 <= u'9')) :
                    alt2 = 1


                if alt2 == 1:
                    # /home/staal/devel/arff/arff.g:351:20: '0' .. '9'
                    self.matchRange(u'0', u'9')



                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1






        finally:

            pass

    # $ANTLR end INT



    # $ANTLR start FLOAT
    def mFLOAT(self, ):

        try:
            self.type = FLOAT

            # /home/staal/devel/arff/arff.g:356:5: ( ( '+' | '-' )? ( ( ( '0' .. '9' )+ )? '.' ( '0' .. '9' )+ ( EXPONENT )? | ( '0' .. '9' )+ EXPONENT ) )
            # /home/staal/devel/arff/arff.g:356:7: ( '+' | '-' )? ( ( ( '0' .. '9' )+ )? '.' ( '0' .. '9' )+ ( EXPONENT )? | ( '0' .. '9' )+ EXPONENT )
            # /home/staal/devel/arff/arff.g:356:7: ( '+' | '-' )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == u'+' or LA3_0 == u'-') :
                alt3 = 1
            if alt3 == 1:
                # /home/staal/devel/arff/arff.g:
                if self.input.LA(1) == u'+' or self.input.LA(1) == u'-':
                    self.input.consume();

                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse





            # /home/staal/devel/arff/arff.g:357:9: ( ( ( '0' .. '9' )+ )? '.' ( '0' .. '9' )+ ( EXPONENT )? | ( '0' .. '9' )+ EXPONENT )
            alt9 = 2
            alt9 = self.dfa9.predict(self.input)
            if alt9 == 1:
                # /home/staal/devel/arff/arff.g:358:13: ( ( '0' .. '9' )+ )? '.' ( '0' .. '9' )+ ( EXPONENT )?
                # /home/staal/devel/arff/arff.g:358:13: ( ( '0' .. '9' )+ )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((u'0' <= LA5_0 <= u'9')) :
                    alt5 = 1
                if alt5 == 1:
                    # /home/staal/devel/arff/arff.g:358:14: ( '0' .. '9' )+
                    # /home/staal/devel/arff/arff.g:358:14: ( '0' .. '9' )+
                    cnt4 = 0
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if ((u'0' <= LA4_0 <= u'9')) :
                            alt4 = 1


                        if alt4 == 1:
                            # /home/staal/devel/arff/arff.g:358:15: '0' .. '9'
                            self.matchRange(u'0', u'9')



                        else:
                            if cnt4 >= 1:
                                break #loop4

                            eee = EarlyExitException(4, self.input)
                            raise eee

                        cnt4 += 1





                self.match(u'.')

                # /home/staal/devel/arff/arff.g:358:32: ( '0' .. '9' )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if ((u'0' <= LA6_0 <= u'9')) :
                        alt6 = 1


                    if alt6 == 1:
                        # /home/staal/devel/arff/arff.g:358:33: '0' .. '9'
                        self.matchRange(u'0', u'9')



                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1


                # /home/staal/devel/arff/arff.g:358:44: ( EXPONENT )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == u'E' or LA7_0 == u'e') :
                    alt7 = 1
                if alt7 == 1:
                    # /home/staal/devel/arff/arff.g:358:44: EXPONENT
                    self.mEXPONENT()






            elif alt9 == 2:
                # /home/staal/devel/arff/arff.g:360:13: ( '0' .. '9' )+ EXPONENT
                # /home/staal/devel/arff/arff.g:360:13: ( '0' .. '9' )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if ((u'0' <= LA8_0 <= u'9')) :
                        alt8 = 1


                    if alt8 == 1:
                        # /home/staal/devel/arff/arff.g:360:14: '0' .. '9'
                        self.matchRange(u'0', u'9')



                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1


                self.mEXPONENT()








        finally:

            pass

    # $ANTLR end FLOAT



    # $ANTLR start EXPONENT
    def mEXPONENT(self, ):

        try:
            # /home/staal/devel/arff/arff.g:366:5: ( ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+ )
            # /home/staal/devel/arff/arff.g:366:7: ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+
            if self.input.LA(1) == u'E' or self.input.LA(1) == u'e':
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse


            # /home/staal/devel/arff/arff.g:366:17: ( '+' | '-' )?
            alt10 = 2
            LA10_0 = self.input.LA(1)

            if (LA10_0 == u'+' or LA10_0 == u'-') :
                alt10 = 1
            if alt10 == 1:
                # /home/staal/devel/arff/arff.g:
                if self.input.LA(1) == u'+' or self.input.LA(1) == u'-':
                    self.input.consume();

                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse





            # /home/staal/devel/arff/arff.g:366:28: ( '0' .. '9' )+
            cnt11 = 0
            while True: #loop11
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if ((u'0' <= LA11_0 <= u'9')) :
                    alt11 = 1


                if alt11 == 1:
                    # /home/staal/devel/arff/arff.g:366:29: '0' .. '9'
                    self.matchRange(u'0', u'9')



                else:
                    if cnt11 >= 1:
                        break #loop11

                    eee = EarlyExitException(11, self.input)
                    raise eee

                cnt11 += 1






        finally:

            pass

    # $ANTLR end EXPONENT



    # $ANTLR start QSTRING
    def mQSTRING(self, ):

        try:
            self.type = QSTRING

            # /home/staal/devel/arff/arff.g:371:2: ( ( '\"' (~ ( '\"' ) )* '\"' ) | ( '\\'' (~ ( '\\'' ) )* '\\'' ) )
            alt14 = 2
            LA14_0 = self.input.LA(1)

            if (LA14_0 == u'"') :
                alt14 = 1
            elif (LA14_0 == u'\'') :
                alt14 = 2
            else:
                nvae = NoViableAltException("370:1: QSTRING : ( ( '\"' (~ ( '\"' ) )* '\"' ) | ( '\\'' (~ ( '\\'' ) )* '\\'' ) );", 14, 0, self.input)

                raise nvae

            if alt14 == 1:
                # /home/staal/devel/arff/arff.g:371:4: ( '\"' (~ ( '\"' ) )* '\"' )
                # /home/staal/devel/arff/arff.g:371:4: ( '\"' (~ ( '\"' ) )* '\"' )
                # /home/staal/devel/arff/arff.g:371:5: '\"' (~ ( '\"' ) )* '\"'
                self.match(u'"')

                # /home/staal/devel/arff/arff.g:371:10: (~ ( '\"' ) )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if ((u'\u0000' <= LA12_0 <= u'!') or (u'#' <= LA12_0 <= u'\uFFFE')) :
                        alt12 = 1


                    if alt12 == 1:
                        # /home/staal/devel/arff/arff.g:371:11: ~ ( '\"' )
                        if (u'\u0000' <= self.input.LA(1) <= u'!') or (u'#' <= self.input.LA(1) <= u'\uFFFE'):
                            self.input.consume();

                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop12


                self.match(u'"')






            elif alt14 == 2:
                # /home/staal/devel/arff/arff.g:372:4: ( '\\'' (~ ( '\\'' ) )* '\\'' )
                # /home/staal/devel/arff/arff.g:372:4: ( '\\'' (~ ( '\\'' ) )* '\\'' )
                # /home/staal/devel/arff/arff.g:372:5: '\\'' (~ ( '\\'' ) )* '\\''
                self.match(u'\'')

                # /home/staal/devel/arff/arff.g:372:10: (~ ( '\\'' ) )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if ((u'\u0000' <= LA13_0 <= u'&') or (u'(' <= LA13_0 <= u'\uFFFE')) :
                        alt13 = 1


                    if alt13 == 1:
                        # /home/staal/devel/arff/arff.g:372:11: ~ ( '\\'' )
                        if (u'\u0000' <= self.input.LA(1) <= u'&') or (u'(' <= self.input.LA(1) <= u'\uFFFE'):
                            self.input.consume();

                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop13


                self.match(u'\'')







        finally:

            pass

    # $ANTLR end QSTRING



    # $ANTLR start STRING
    def mSTRING(self, ):

        try:
            self.type = STRING

            # /home/staal/devel/arff/arff.g:378:5: ( (~ ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' | ',' | '{' | '}' | '\\'' | '\\\"' ) | '\\\\' ( ',' | '{' | '}' | '\\'' | '\\\"' ) )+ )
            # /home/staal/devel/arff/arff.g:379:9: (~ ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' | ',' | '{' | '}' | '\\'' | '\\\"' ) | '\\\\' ( ',' | '{' | '}' | '\\'' | '\\\"' ) )+
            # /home/staal/devel/arff/arff.g:379:9: (~ ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' | ',' | '{' | '}' | '\\'' | '\\\"' ) | '\\\\' ( ',' | '{' | '}' | '\\'' | '\\\"' ) )+
            cnt15 = 0
            while True: #loop15
                alt15 = 3
                LA15_0 = self.input.LA(1)

                if (LA15_0 == u'\\') :
                    LA15_2 = self.input.LA(2)

                    if (LA15_2 == u'"' or LA15_2 == u'\'' or LA15_2 == u',' or LA15_2 == u'{' or LA15_2 == u'}') :
                        alt15 = 2

                    else:
                        alt15 = 1


                elif ((u'\u0000' <= LA15_0 <= u'\b') or LA15_0 == u'\u000B' or (u'\u000E' <= LA15_0 <= u'\u001F') or LA15_0 == u'!' or (u'#' <= LA15_0 <= u'&') or (u'(' <= LA15_0 <= u'+') or (u'-' <= LA15_0 <= u'[') or (u']' <= LA15_0 <= u'z') or LA15_0 == u'|' or (u'~' <= LA15_0 <= u'\uFFFE')) :
                    alt15 = 1


                if alt15 == 1:
                    # /home/staal/devel/arff/arff.g:380:13: ~ ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' | ',' | '{' | '}' | '\\'' | '\\\"' )
                    if (u'\u0000' <= self.input.LA(1) <= u'\b') or self.input.LA(1) == u'\u000B' or (u'\u000E' <= self.input.LA(1) <= u'\u001F') or self.input.LA(1) == u'!' or (u'#' <= self.input.LA(1) <= u'&') or (u'(' <= self.input.LA(1) <= u'+') or (u'-' <= self.input.LA(1) <= u'z') or self.input.LA(1) == u'|' or (u'~' <= self.input.LA(1) <= u'\uFFFE'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                elif alt15 == 2:
                    # /home/staal/devel/arff/arff.g:382:13: '\\\\' ( ',' | '{' | '}' | '\\'' | '\\\"' )
                    self.match(u'\\')

                    if self.input.LA(1) == u'"' or self.input.LA(1) == u'\'' or self.input.LA(1) == u',' or self.input.LA(1) == u'{' or self.input.LA(1) == u'}':
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt15 >= 1:
                        break #loop15

                    eee = EarlyExitException(15, self.input)
                    raise eee

                cnt15 += 1






        finally:

            pass

    # $ANTLR end STRING



    # $ANTLR start LINE_COMMENT
    def mLINE_COMMENT(self, ):

        try:
            self.type = LINE_COMMENT

            # /home/staal/devel/arff/arff.g:388:17: ( '%' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # /home/staal/devel/arff/arff.g:388:19: '%' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            self.match(u'%')

            # /home/staal/devel/arff/arff.g:388:23: (~ ( '\\n' | '\\r' ) )*
            while True: #loop16
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if ((u'\u0000' <= LA16_0 <= u'\t') or (u'\u000B' <= LA16_0 <= u'\f') or (u'\u000E' <= LA16_0 <= u'\uFFFE')) :
                    alt16 = 1


                if alt16 == 1:
                    # /home/staal/devel/arff/arff.g:388:23: ~ ( '\\n' | '\\r' )
                    if (u'\u0000' <= self.input.LA(1) <= u'\t') or (u'\u000B' <= self.input.LA(1) <= u'\f') or (u'\u000E' <= self.input.LA(1) <= u'\uFFFE'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop16


            # /home/staal/devel/arff/arff.g:388:37: ( '\\r' )?
            alt17 = 2
            LA17_0 = self.input.LA(1)

            if (LA17_0 == u'\r') :
                alt17 = 1
            if alt17 == 1:
                # /home/staal/devel/arff/arff.g:388:37: '\\r'
                self.match(u'\r')




            self.match(u'\n')

            #action start
            self.channel=HIDDEN;
            #action end




        finally:

            pass

    # $ANTLR end LINE_COMMENT



    # $ANTLR start WS
    def mWS(self, ):

        try:
            self.type = WS

            # /home/staal/devel/arff/arff.g:389:5: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # /home/staal/devel/arff/arff.g:389:8: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
            if (u'\t' <= self.input.LA(1) <= u'\n') or (u'\f' <= self.input.LA(1) <= u'\r') or self.input.LA(1) == u' ':
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse


            #action start
            self.channel=HIDDEN;
            #action end




        finally:

            pass

    # $ANTLR end WS



    def mTokens(self):
        # /home/staal/devel/arff/arff.g:1:8: ( T11 | T12 | T13 | T14 | T15 | T16 | T17 | T18 | T19 | T20 | T21 | T22 | T23 | T24 | T25 | T26 | T27 | T28 | T29 | T30 | T31 | T32 | T33 | T34 | T35 | T36 | T37 | T38 | T39 | T40 | T41 | T42 | T43 | T44 | INT | FLOAT | QSTRING | STRING | LINE_COMMENT | WS )
        alt18 = 40
        alt18 = self.dfa18.predict(self.input)
        if alt18 == 1:
            # /home/staal/devel/arff/arff.g:1:10: T11
            self.mT11()



        elif alt18 == 2:
            # /home/staal/devel/arff/arff.g:1:14: T12
            self.mT12()



        elif alt18 == 3:
            # /home/staal/devel/arff/arff.g:1:18: T13
            self.mT13()



        elif alt18 == 4:
            # /home/staal/devel/arff/arff.g:1:22: T14
            self.mT14()



        elif alt18 == 5:
            # /home/staal/devel/arff/arff.g:1:26: T15
            self.mT15()



        elif alt18 == 6:
            # /home/staal/devel/arff/arff.g:1:30: T16
            self.mT16()



        elif alt18 == 7:
            # /home/staal/devel/arff/arff.g:1:34: T17
            self.mT17()



        elif alt18 == 8:
            # /home/staal/devel/arff/arff.g:1:38: T18
            self.mT18()



        elif alt18 == 9:
            # /home/staal/devel/arff/arff.g:1:42: T19
            self.mT19()



        elif alt18 == 10:
            # /home/staal/devel/arff/arff.g:1:46: T20
            self.mT20()



        elif alt18 == 11:
            # /home/staal/devel/arff/arff.g:1:50: T21
            self.mT21()



        elif alt18 == 12:
            # /home/staal/devel/arff/arff.g:1:54: T22
            self.mT22()



        elif alt18 == 13:
            # /home/staal/devel/arff/arff.g:1:58: T23
            self.mT23()



        elif alt18 == 14:
            # /home/staal/devel/arff/arff.g:1:62: T24
            self.mT24()



        elif alt18 == 15:
            # /home/staal/devel/arff/arff.g:1:66: T25
            self.mT25()



        elif alt18 == 16:
            # /home/staal/devel/arff/arff.g:1:70: T26
            self.mT26()



        elif alt18 == 17:
            # /home/staal/devel/arff/arff.g:1:74: T27
            self.mT27()



        elif alt18 == 18:
            # /home/staal/devel/arff/arff.g:1:78: T28
            self.mT28()



        elif alt18 == 19:
            # /home/staal/devel/arff/arff.g:1:82: T29
            self.mT29()



        elif alt18 == 20:
            # /home/staal/devel/arff/arff.g:1:86: T30
            self.mT30()



        elif alt18 == 21:
            # /home/staal/devel/arff/arff.g:1:90: T31
            self.mT31()



        elif alt18 == 22:
            # /home/staal/devel/arff/arff.g:1:94: T32
            self.mT32()



        elif alt18 == 23:
            # /home/staal/devel/arff/arff.g:1:98: T33
            self.mT33()



        elif alt18 == 24:
            # /home/staal/devel/arff/arff.g:1:102: T34
            self.mT34()



        elif alt18 == 25:
            # /home/staal/devel/arff/arff.g:1:106: T35
            self.mT35()



        elif alt18 == 26:
            # /home/staal/devel/arff/arff.g:1:110: T36
            self.mT36()



        elif alt18 == 27:
            # /home/staal/devel/arff/arff.g:1:114: T37
            self.mT37()



        elif alt18 == 28:
            # /home/staal/devel/arff/arff.g:1:118: T38
            self.mT38()



        elif alt18 == 29:
            # /home/staal/devel/arff/arff.g:1:122: T39
            self.mT39()



        elif alt18 == 30:
            # /home/staal/devel/arff/arff.g:1:126: T40
            self.mT40()



        elif alt18 == 31:
            # /home/staal/devel/arff/arff.g:1:130: T41
            self.mT41()



        elif alt18 == 32:
            # /home/staal/devel/arff/arff.g:1:134: T42
            self.mT42()



        elif alt18 == 33:
            # /home/staal/devel/arff/arff.g:1:138: T43
            self.mT43()



        elif alt18 == 34:
            # /home/staal/devel/arff/arff.g:1:142: T44
            self.mT44()



        elif alt18 == 35:
            # /home/staal/devel/arff/arff.g:1:146: INT
            self.mINT()



        elif alt18 == 36:
            # /home/staal/devel/arff/arff.g:1:150: FLOAT
            self.mFLOAT()



        elif alt18 == 37:
            # /home/staal/devel/arff/arff.g:1:156: QSTRING
            self.mQSTRING()



        elif alt18 == 38:
            # /home/staal/devel/arff/arff.g:1:164: STRING
            self.mSTRING()



        elif alt18 == 39:
            # /home/staal/devel/arff/arff.g:1:171: LINE_COMMENT
            self.mLINE_COMMENT()



        elif alt18 == 40:
            # /home/staal/devel/arff/arff.g:1:184: WS
            self.mWS()








    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\2\56\2\uffff"
        )

    DFA9_max = DFA.unpack(
        u"\1\71\1\145\2\uffff"
        )

    DFA9_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA9_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA9_transition = [
        DFA.unpack(u"\1\2\1\uffff\12\1"),
        DFA.unpack(u"\1\2\1\uffff\12\1\13\uffff\1\3\37\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #9

    DFA9 = DFA
    # lookup tables for DFA #18

    DFA18_eot = DFA.unpack(
        u"\1\uffff\11\24\2\uffff\2\24\1\uffff\1\56\1\24\1\57\1\24\2\uffff"
        u"\1\24\1\uffff\27\24\2\uffff\1\24\1\125\1\24\1\uffff\40\24\1\125"
        u"\1\uffff\2\24\1\170\6\24\1\177\1\u0080\12\24\1\u008b\1\u008c\2"
        u"\24\1\u008f\3\24\1\u0093\1\u0094\1\u0095\1\24\1\125\1\uffff\1\24"
        u"\1\u0097\4\24\2\uffff\1\24\1\u009d\1\u009e\7\24\2\uffff\2\24\1"
        u"\uffff\3\24\3\uffff\1\24\1\uffff\5\24\2\uffff\11\24\1\u00ba\1\u00bb"
        u"\1\u00bc\6\24\1\u00c3\1\u00c4\1\u00c5\1\u00c6\1\u00c7\1\u00c8\3"
        u"\24\3\uffff\6\24\6\uffff\3\24\1\u00d5\2\24\1\u00d8\1\u00d9\4\24"
        u"\1\uffff\1\u00de\1\u00df\2\uffff\1\u00e0\1\u00e1\1\u00e2\1\u00e3"
        u"\6\uffff"
        )

    DFA18_eof = DFA.unpack(
        u"\u00e4\uffff"
        )

    DFA18_min = DFA.unpack(
        u"\1\0\1\101\1\165\1\125\1\156\1\116\1\145\1\105\1\164\1\124\2\uffff"
        u"\1\141\1\101\1\uffff\1\0\1\56\1\0\1\60\2\uffff\1\0\1\uffff\1\156"
        u"\1\145\1\141\1\124\1\105\1\116\1\164\1\101\1\155\1\115\1\155\2"
        u"\164\1\124\1\141\1\101\1\141\1\162\1\122\1\162\2\164\1\124\2\uffff"
        u"\1\53\2\0\1\uffff\1\0\1\144\1\154\2\164\1\124\1\114\1\154\1\144"
        u"\1\104\1\164\1\124\1\164\1\145\1\105\3\145\1\105\1\141\1\154\1"
        u"\114\1\101\1\141\1\154\1\151\1\111\1\151\2\145\1\105\1\60\1\0\1"
        u"\uffff\1\53\2\0\2\141\1\162\1\122\1\101\1\141\2\0\1\162\1\101\1"
        u"\141\1\162\1\122\1\162\2\147\1\107\1\164\2\0\1\124\1\164\1\0\1"
        u"\156\1\116\1\156\3\0\1\60\1\0\1\uffff\1\164\1\0\1\151\1\111\1\124"
        u"\1\164\2\uffff\1\151\2\0\1\151\1\111\1\151\2\145\1\105\1\151\2"
        u"\uffff\1\111\1\151\1\uffff\1\147\1\107\1\147\3\uffff\1\151\1\uffff"
        u"\1\142\1\102\1\111\1\151\1\142\2\uffff\1\143\1\103\1\143\2\162"
        u"\1\122\1\157\1\117\1\157\3\0\1\157\1\165\1\125\1\117\1\157\1\165"
        u"\6\0\1\156\1\116\1\156\3\uffff\1\156\1\164\1\124\1\116\1\156\1"
        u"\164\6\uffff\1\141\1\101\1\141\1\0\1\145\1\105\2\0\1\145\1\154"
        u"\1\114\1\154\1\uffff\2\0\2\uffff\4\0\6\uffff"
        )

    DFA18_max = DFA.unpack(
        u"\1\ufffe\1\162\2\165\2\156\2\145\2\164\2\uffff\2\141\1\uffff\1"
        u"\ufffe\1\71\1\ufffe\1\71\2\uffff\1\ufffe\1\uffff\1\156\1\145\1"
        u"\141\1\164\1\145\1\156\1\164\1\141\1\155\1\115\1\155\2\164\1\124"
        u"\1\154\1\114\1\154\1\162\1\122\1\162\2\164\1\124\2\uffff\1\71\2"
        u"\ufffe\1\uffff\1\ufffe\1\144\1\154\2\164\1\124\1\114\1\154\1\144"
        u"\1\104\1\164\1\124\1\164\1\145\1\105\3\145\1\105\1\141\1\154\1"
        u"\114\1\101\1\141\1\154\1\151\1\111\1\151\2\145\1\105\1\71\1\ufffe"
        u"\1\uffff\1\71\2\ufffe\2\141\1\162\1\122\1\101\1\141\2\ufffe\1\162"
        u"\1\101\1\141\1\162\1\122\1\162\2\147\1\107\1\164\2\ufffe\1\124"
        u"\1\164\1\ufffe\1\156\1\116\1\156\3\ufffe\1\71\1\ufffe\1\uffff\1"
        u"\164\1\ufffe\1\151\1\111\1\124\1\164\2\uffff\1\151\2\ufffe\1\151"
        u"\1\111\1\151\2\145\1\105\1\151\2\uffff\1\111\1\151\1\uffff\1\147"
        u"\1\107\1\147\3\uffff\1\151\1\uffff\1\142\1\102\1\111\1\151\1\142"
        u"\2\uffff\1\143\1\103\1\143\2\162\1\122\1\157\1\117\1\157\3\ufffe"
        u"\1\157\1\165\1\125\1\117\1\157\1\165\6\ufffe\1\156\1\116\1\156"
        u"\3\uffff\1\156\1\164\1\124\1\116\1\156\1\164\6\uffff\1\141\1\101"
        u"\1\141\1\ufffe\1\145\1\105\2\ufffe\1\145\1\154\1\114\1\154\1\uffff"
        u"\2\ufffe\2\uffff\4\ufffe\6\uffff"
        )

    DFA18_accept = DFA.unpack(
        u"\12\uffff\1\31\1\32\2\uffff\1\41\4\uffff\1\45\1\46\1\uffff\1\50"
        u"\27\uffff\1\42\1\43\3\uffff\1\47\41\uffff\1\44\42\uffff\1\26\6"
        u"\uffff\1\27\1\30\12\uffff\1\15\1\17\2\uffff\1\16\3\uffff\1\33\1"
        u"\35\1\34\1\uffff\1\36\5\uffff\1\40\1\37\33\uffff\1\20\1\22\1\21"
        u"\6\uffff\1\7\1\11\1\10\1\12\1\13\1\14\14\uffff\1\1\2\uffff\1\2"
        u"\1\3\4\uffff\1\5\1\6\1\4\1\23\1\25\1\24"
        )

    DFA18_special = DFA.unpack(
        u"\u00e4\uffff"
        )

            
    DFA18_transition = [
        DFA.unpack(u"\11\24\2\26\1\24\2\26\22\24\1\26\1\24\1\23\2\24\1\25"
        u"\1\24\1\23\3\24\1\20\1\16\1\20\1\22\1\24\12\21\5\24\1\17\1\1\3"
        u"\24\1\15\4\24\1\5\4\24\1\3\3\24\1\7\1\11\20\24\1\14\4\24\1\4\4"
        u"\24\1\2\3\24\1\6\1\10\7\24\1\12\1\24\1\13\uff81\24"),
        DFA.unpack(u"\1\32\2\uffff\1\36\1\34\14\uffff\1\33\16\uffff\1\35"
        u"\2\uffff\1\31\1\27\14\uffff\1\30"),
        DFA.unpack(u"\1\37"),
        DFA.unpack(u"\1\40\37\uffff\1\41"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u"\1\44\37\uffff\1\43"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46\37\uffff\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u"\1\51\37\uffff\1\52"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u"\1\55\37\uffff\1\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\1\22\1\uffff\12\21"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\1\24\1\22\1\24\12\21\13\24\1\60\37\24"
        u"\1\60\25\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\12\61"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\11\64\2\63\1\64\2\63\22\64\1\63\1\64\1\63\4\64\1\63"
        u"\4\64\1\63\57\64\1\62\36\64\1\63\1\64\1\63\uff81\64"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\71\37\uffff\1\70"),
        DFA.unpack(u"\1\72\37\uffff\1\73"),
        DFA.unpack(u"\1\75\37\uffff\1\74"),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u"\1\77\37\uffff\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u"\1\110\12\uffff\1\107"),
        DFA.unpack(u"\1\111\12\uffff\1\112"),
        DFA.unpack(u"\1\114\12\uffff\1\113"),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u"\1\117"),
        DFA.unpack(u"\1\120"),
        DFA.unpack(u"\1\121"),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\123\1\uffff\1\123\2\uffff\12\124"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\3\24\12\61\13\24\1\126\37\24\1\126\25"
        u"\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\64\2\63\1\64\2\63\22\64\1\63\1\64\1\127\4\64\1\127"
        u"\4\64\1\127\57\64\1\62\36\64\1\127\1\64\1\127\uff81\64"),
        DFA.unpack(u""),
        DFA.unpack(u"\11\64\2\63\1\64\2\63\22\64\1\63\1\64\1\63\4\64\1\63"
        u"\4\64\1\63\57\64\1\62\36\64\1\63\1\64\1\63\uff81\64"),
        DFA.unpack(u"\1\130"),
        DFA.unpack(u"\1\131"),
        DFA.unpack(u"\1\132"),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u"\1\136"),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u"\1\141"),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u"\1\143"),
        DFA.unpack(u"\1\144"),
        DFA.unpack(u"\1\145"),
        DFA.unpack(u"\1\146"),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u"\1\151"),
        DFA.unpack(u"\1\152"),
        DFA.unpack(u"\1\153"),
        DFA.unpack(u"\1\154"),
        DFA.unpack(u"\1\155"),
        DFA.unpack(u"\1\156"),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u"\1\160"),
        DFA.unpack(u"\1\161"),
        DFA.unpack(u"\1\162"),
        DFA.unpack(u"\1\163"),
        DFA.unpack(u"\1\164"),
        DFA.unpack(u"\1\165"),
        DFA.unpack(u"\12\124"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\3\24\12\124\101\24\1\uffff\1\24\1\uffff"
        u"\uff81\24"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\166\1\uffff\1\166\2\uffff\12\167"),
        DFA.unpack(u"\11\64\2\63\1\64\2\63\22\64\1\63\1\64\1\63\4\64\1\63"
        u"\4\64\1\63\57\64\1\62\36\64\1\63\1\64\1\63\uff81\64"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u"\1\172"),
        DFA.unpack(u"\1\173"),
        DFA.unpack(u"\1\174"),
        DFA.unpack(u"\1\175"),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\1\u0081"),
        DFA.unpack(u"\1\u0082"),
        DFA.unpack(u"\1\u0083"),
        DFA.unpack(u"\1\u0084"),
        DFA.unpack(u"\1\u0085"),
        DFA.unpack(u"\1\u0086"),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\1\u0088"),
        DFA.unpack(u"\1\u0089"),
        DFA.unpack(u"\1\u008a"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\1\u008d"),
        DFA.unpack(u"\1\u008e"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\1\u0090"),
        DFA.unpack(u"\1\u0091"),
        DFA.unpack(u"\1\u0092"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\12\167"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\3\24\12\167\101\24\1\uffff\1\24\1\uffff"
        u"\uff81\24"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0096"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\1\u0098"),
        DFA.unpack(u"\1\u0099"),
        DFA.unpack(u"\1\u009a"),
        DFA.unpack(u"\1\u009b"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u009c"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\1\u009f"),
        DFA.unpack(u"\1\u00a0"),
        DFA.unpack(u"\1\u00a1"),
        DFA.unpack(u"\1\u00a2"),
        DFA.unpack(u"\1\u00a3"),
        DFA.unpack(u"\1\u00a4"),
        DFA.unpack(u"\1\u00a5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a6"),
        DFA.unpack(u"\1\u00a7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a8"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u"\1\u00aa"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ab"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ac"),
        DFA.unpack(u"\1\u00ad"),
        DFA.unpack(u"\1\u00ae"),
        DFA.unpack(u"\1\u00af"),
        DFA.unpack(u"\1\u00b0"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00b1"),
        DFA.unpack(u"\1\u00b2"),
        DFA.unpack(u"\1\u00b3"),
        DFA.unpack(u"\1\u00b4"),
        DFA.unpack(u"\1\u00b5"),
        DFA.unpack(u"\1\u00b6"),
        DFA.unpack(u"\1\u00b7"),
        DFA.unpack(u"\1\u00b8"),
        DFA.unpack(u"\1\u00b9"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\1\u00bd"),
        DFA.unpack(u"\1\u00be"),
        DFA.unpack(u"\1\u00bf"),
        DFA.unpack(u"\1\u00c0"),
        DFA.unpack(u"\1\u00c1"),
        DFA.unpack(u"\1\u00c2"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\1\u00c9"),
        DFA.unpack(u"\1\u00ca"),
        DFA.unpack(u"\1\u00cb"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00cc"),
        DFA.unpack(u"\1\u00cd"),
        DFA.unpack(u"\1\u00ce"),
        DFA.unpack(u"\1\u00cf"),
        DFA.unpack(u"\1\u00d0"),
        DFA.unpack(u"\1\u00d1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d2"),
        DFA.unpack(u"\1\u00d3"),
        DFA.unpack(u"\1\u00d4"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\1\u00d6"),
        DFA.unpack(u"\1\u00d7"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\1\u00da"),
        DFA.unpack(u"\1\u00db"),
        DFA.unpack(u"\1\u00dc"),
        DFA.unpack(u"\1\u00dd"),
        DFA.unpack(u""),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u"\11\24\2\uffff\1\24\2\uffff\22\24\1\uffff\1\24\1\uffff"
        u"\4\24\1\uffff\4\24\1\uffff\116\24\1\uffff\1\24\1\uffff\uff81\24"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #18

    DFA18 = DFA
 

