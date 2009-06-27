# $ANTLR 3.0.1 /home/staal/devel/arff/arff.g 2008-01-16 11:17:08

from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EXPONENT=8
WS=10
LINE_COMMENT=9
INT=4
FLOAT=5
QSTRING=6
EOF=-1
STRING=7

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "INT", "FLOAT", "QSTRING", "STRING", "EXPONENT", "LINE_COMMENT", "WS", 
    "'@relation'", "'@RELATION'", "'@Relation'", "'@attribute'", "'@Attribute'", 
    "'@ATTRIBUTE'", "'numeric'", "'Numeric'", "'NUMERIC'", "'integer'", 
    "'Integer'", "'INTEGER'", "'real'", "'Real'", "'REAL'", "'string'", 
    "'String'", "'STRING'", "'relational'", "'Relational'", "'RELATIONAL'", 
    "'@end'", "'@End'", "'@END'", "'{'", "'}'", "'date'", "'DATE'", "'Date'", 
    "'@data'", "'@Data'", "'@DATA'", "','", "'?'"
]



class arffParser(Parser):
    grammarFileName = "/home/staal/devel/arff/arff.g"
    tokenNames = tokenNames

    def __init__(self, input):
        Parser.__init__(self, input)


               
        self.m = [];         # data 'matrix' (LoL)
        self.alist = [];     # list of (attribute_name, type_code, range/format/sub)
        self.rname = 'None'; # relation name
        self.sparse = False; # sparse arff format? (self.m contains the tuples)
        self.anyErrors = False;  # use this to check if we had any errors            


                


              
    def reportError(self, e):  # modified to set self.anyErrors to True
        if self.errorRecovery:
            return
        self.errorRecovery = True
        self.displayRecognitionError(self.tokenNames, e)
        self.anyErrors = True



    # $ANTLR start file
    # /home/staal/devel/arff/arff.g:111:1: file : header data ;
    def file(self, ):

        try:
            try:
                # /home/staal/devel/arff/arff.g:112:5: ( header data )
                # /home/staal/devel/arff/arff.g:113:9: header data
                self.following.append(self.FOLLOW_header_in_file57)
                self.header()
                self.following.pop()

                self.following.append(self.FOLLOW_data_in_file67)
                self.data()
                self.following.pop()





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end file


    # $ANTLR start header
    # /home/staal/devel/arff/arff.g:118:1: header : ( '@relation' | '@RELATION' | '@Relation' ) string adecls ;
    def header(self, ):

        string1 = None

        adecls2 = None


        try:
            try:
                # /home/staal/devel/arff/arff.g:119:5: ( ( '@relation' | '@RELATION' | '@Relation' ) string adecls )
                # /home/staal/devel/arff/arff.g:120:9: ( '@relation' | '@RELATION' | '@Relation' ) string adecls
                if (11 <= self.input.LA(1) <= 13):
                    self.input.consume();
                    self.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_header93
                        )
                    raise mse


                self.following.append(self.FOLLOW_string_in_header113)
                string1 = self.string()
                self.following.pop()

                #action start
                         
                self.rname = string1;
                        
                #action end
                self.following.append(self.FOLLOW_adecls_in_header133)
                adecls2 = self.adecls()
                self.following.pop()

                #action start
                         
                self.alist = adecls2;
                        
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end header


    # $ANTLR start adecls
    # /home/staal/devel/arff/arff.g:133:1: adecls returns [atups] : a1= adecl (a2= adecl )* ;
    def adecls(self, ):

        atups = None

        a1 = None

        a2 = None


               
        atups = [];

        try:
            try:
                # /home/staal/devel/arff/arff.g:138:5: (a1= adecl (a2= adecl )* )
                # /home/staal/devel/arff/arff.g:139:9: a1= adecl (a2= adecl )*
                self.following.append(self.FOLLOW_adecl_in_adecls181)
                a1 = self.adecl()
                self.following.pop()

                #action start
                         
                atups.append(a1);
                        
                #action end
                # /home/staal/devel/arff/arff.g:143:9: (a2= adecl )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((14 <= LA1_0 <= 16)) :
                        alt1 = 1


                    if alt1 == 1:
                        # /home/staal/devel/arff/arff.g:144:13: a2= adecl
                        self.following.append(self.FOLLOW_adecl_in_adecls217)
                        a2 = self.adecl()
                        self.following.pop()

                        #action start
                                     
                        atups.append(a2);
                                    
                        #action end


                    else:
                        break #loop1






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return atups

    # $ANTLR end adecls


    # $ANTLR start adecl
    # /home/staal/devel/arff/arff.g:152:1: adecl returns [atup] : ( '@attribute' | '@Attribute' | '@ATTRIBUTE' ) string datatype ;
    def adecl(self, ):

        atup = None

        string3 = None

        datatype4 = None


        try:
            try:
                # /home/staal/devel/arff/arff.g:154:5: ( ( '@attribute' | '@Attribute' | '@ATTRIBUTE' ) string datatype )
                # /home/staal/devel/arff/arff.g:155:9: ( '@attribute' | '@Attribute' | '@ATTRIBUTE' ) string datatype
                if (14 <= self.input.LA(1) <= 16):
                    self.input.consume();
                    self.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_adecl272
                        )
                    raise mse


                self.following.append(self.FOLLOW_string_in_adecl292)
                string3 = self.string()
                self.following.pop()

                self.following.append(self.FOLLOW_datatype_in_adecl302)
                datatype4 = self.datatype()
                self.following.pop()

                #action start
                         
                atup =  (string3, datatype4.typecode, datatype4.nlist)
                        
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return atup

    # $ANTLR end adecl

    class datatype_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.typecode = None
            self.nlist = None


    # $ANTLR start datatype
    # /home/staal/devel/arff/arff.g:165:1: datatype returns [typecode, nlist] : ( ( 'numeric' | 'Numeric' | 'NUMERIC' ) | ( 'integer' | 'Integer' | 'INTEGER' ) | ( 'real' | 'Real' | 'REAL' ) | ( 'string' | 'String' | 'STRING' ) | ( 'relational' | 'Relational' | 'RELATIONAL' ) adecls ( '@end' | '@End' | '@END' ) string | date | '{' values '}' );
    def datatype(self, ):

        retval = self.datatype_return()
        retval.start = self.input.LT(1)

        adecls5 = None

        date6 = None

        values7 = None


               
        retval.typecode = 0 
        retval.nlist = []

        try:
            try:
                # /home/staal/devel/arff/arff.g:171:2: ( ( 'numeric' | 'Numeric' | 'NUMERIC' ) | ( 'integer' | 'Integer' | 'INTEGER' ) | ( 'real' | 'Real' | 'REAL' ) | ( 'string' | 'String' | 'STRING' ) | ( 'relational' | 'Relational' | 'RELATIONAL' ) adecls ( '@end' | '@End' | '@END' ) string | date | '{' values '}' )
                alt2 = 7
                LA2 = self.input.LA(1)
                if LA2 == 17 or LA2 == 18 or LA2 == 19:
                    alt2 = 1
                elif LA2 == 20 or LA2 == 21 or LA2 == 22:
                    alt2 = 2
                elif LA2 == 23 or LA2 == 24 or LA2 == 25:
                    alt2 = 3
                elif LA2 == 26 or LA2 == 27 or LA2 == 28:
                    alt2 = 4
                elif LA2 == 29 or LA2 == 30 or LA2 == 31:
                    alt2 = 5
                elif LA2 == 37 or LA2 == 38 or LA2 == 39:
                    alt2 = 6
                elif LA2 == 35:
                    alt2 = 7
                else:
                    nvae = NoViableAltException("165:1: datatype returns [typecode, nlist] : ( ( 'numeric' | 'Numeric' | 'NUMERIC' ) | ( 'integer' | 'Integer' | 'INTEGER' ) | ( 'real' | 'Real' | 'REAL' ) | ( 'string' | 'String' | 'STRING' ) | ( 'relational' | 'Relational' | 'RELATIONAL' ) adecls ( '@end' | '@End' | '@END' ) string | date | '{' values '}' );", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # /home/staal/devel/arff/arff.g:172:9: ( 'numeric' | 'Numeric' | 'NUMERIC' )
                    if (17 <= self.input.LA(1) <= 19):
                        self.input.consume();
                        self.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_datatype348
                            )
                        raise mse


                    #action start
                    retval.typecode=1
                    #action end


                elif alt2 == 2:
                    # /home/staal/devel/arff/arff.g:173:9: ( 'integer' | 'Integer' | 'INTEGER' )
                    if (20 <= self.input.LA(1) <= 22):
                        self.input.consume();
                        self.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_datatype366
                            )
                        raise mse


                    #action start
                    retval.typecode=1
                    #action end


                elif alt2 == 3:
                    # /home/staal/devel/arff/arff.g:174:9: ( 'real' | 'Real' | 'REAL' )
                    if (23 <= self.input.LA(1) <= 25):
                        self.input.consume();
                        self.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_datatype384
                            )
                        raise mse


                    #action start
                    retval.typecode=1
                    #action end


                elif alt2 == 4:
                    # /home/staal/devel/arff/arff.g:175:9: ( 'string' | 'String' | 'STRING' )
                    if (26 <= self.input.LA(1) <= 28):
                        self.input.consume();
                        self.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_datatype411
                            )
                        raise mse




                elif alt2 == 5:
                    # /home/staal/devel/arff/arff.g:176:9: ( 'relational' | 'Relational' | 'RELATIONAL' ) adecls ( '@end' | '@End' | '@END' ) string
                    if (29 <= self.input.LA(1) <= 31):
                        self.input.consume();
                        self.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_datatype429
                            )
                        raise mse


                    self.following.append(self.FOLLOW_adecls_in_datatype445)
                    adecls5 = self.adecls()
                    self.following.pop()

                    if (32 <= self.input.LA(1) <= 34):
                        self.input.consume();
                        self.errorRecovery = False

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_datatype455
                            )
                        raise mse


                    self.following.append(self.FOLLOW_string_in_datatype476)
                    self.string()
                    self.following.pop()

                    #action start
                             
                    retval.typecode =  3
                    retval.nlist =  adecls5
                            
                    #action end


                elif alt2 == 6:
                    # /home/staal/devel/arff/arff.g:184:9: date
                    self.following.append(self.FOLLOW_date_in_datatype496)
                    date6 = self.date()
                    self.following.pop()

                    #action start
                             
                    retval.typecode = 2
                    retval.nlist =  [date6]
                            
                    #action end


                elif alt2 == 7:
                    # /home/staal/devel/arff/arff.g:189:9: '{' values '}'
                    self.match(self.input, 35, self.FOLLOW_35_in_datatype516)

                    self.following.append(self.FOLLOW_values_in_datatype518)
                    values7 = self.values()
                    self.following.pop()

                    self.match(self.input, 36, self.FOLLOW_36_in_datatype520)

                    #action start
                             
                    retval.nlist =  values7
                            
                    #action end


                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end datatype


    # $ANTLR start date
    # /home/staal/devel/arff/arff.g:196:1: date returns [format] : ( 'date' | 'DATE' | 'Date' ) ( string )? ;
    def date(self, ):

        format = None

        string8 = None


               
        format =  'yyyy-MM-ddTHH:mm:ss'

        try:
            try:
                # /home/staal/devel/arff/arff.g:201:5: ( ( 'date' | 'DATE' | 'Date' ) ( string )? )
                # /home/staal/devel/arff/arff.g:202:9: ( 'date' | 'DATE' | 'Date' ) ( string )?
                if (37 <= self.input.LA(1) <= 39):
                    self.input.consume();
                    self.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_date565
                        )
                    raise mse


                # /home/staal/devel/arff/arff.g:203:9: ( string )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((QSTRING <= LA3_0 <= STRING) or (17 <= LA3_0 <= 31) or (37 <= LA3_0 <= 39)) :
                    alt3 = 1
                if alt3 == 1:
                    # /home/staal/devel/arff/arff.g:204:13: string
                    self.following.append(self.FOLLOW_string_in_date599)
                    string8 = self.string()
                    self.following.pop()

                    #action start
                                 
                    format =  string8
                                
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return format

    # $ANTLR end date


    # $ANTLR start data
    # /home/staal/devel/arff/arff.g:213:1: data : ( '@data' | '@Data' | '@DATA' ) ( ( pairs )+ | ( values )+ ) ;
    def data(self, ):

        pairs9 = None

        values10 = None


        try:
            try:
                # /home/staal/devel/arff/arff.g:214:5: ( ( '@data' | '@Data' | '@DATA' ) ( ( pairs )+ | ( values )+ ) )
                # /home/staal/devel/arff/arff.g:215:9: ( '@data' | '@Data' | '@DATA' ) ( ( pairs )+ | ( values )+ )
                if (40 <= self.input.LA(1) <= 42):
                    self.input.consume();
                    self.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_data651
                        )
                    raise mse


                # /home/staal/devel/arff/arff.g:216:9: ( ( pairs )+ | ( values )+ )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 35) :
                    alt6 = 1
                elif ((INT <= LA6_0 <= STRING) or (17 <= LA6_0 <= 31) or (37 <= LA6_0 <= 39) or LA6_0 == 44) :
                    alt6 = 2
                else:
                    nvae = NoViableAltException("216:9: ( ( pairs )+ | ( values )+ )", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # /home/staal/devel/arff/arff.g:217:13: ( pairs )+
                    # /home/staal/devel/arff/arff.g:217:13: ( pairs )+
                    cnt4 = 0
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == 35) :
                            alt4 = 1


                        if alt4 == 1:
                            # /home/staal/devel/arff/arff.g:218:17: pairs
                            self.following.append(self.FOLLOW_pairs_in_data702)
                            pairs9 = self.pairs()
                            self.following.pop()

                            #action start
                                             
                            self.m.append(pairs9);
                                            
                            #action end


                        else:
                            if cnt4 >= 1:
                                break #loop4

                            eee = EarlyExitException(4, self.input)
                            raise eee

                        cnt4 += 1


                    #action start
                                 
                    self.sparse = True;
                                
                    #action end


                elif alt6 == 2:
                    # /home/staal/devel/arff/arff.g:228:13: ( values )+
                    # /home/staal/devel/arff/arff.g:228:13: ( values )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if ((INT <= LA5_0 <= STRING) or (17 <= LA5_0 <= 31) or (37 <= LA5_0 <= 39) or LA5_0 == 44) :
                            alt5 = 1


                        if alt5 == 1:
                            # /home/staal/devel/arff/arff.g:229:17: values
                            self.following.append(self.FOLLOW_values_in_data808)
                            values10 = self.values()
                            self.following.pop()

                            #action start
                                             
                            self.m.append(values10);
                                            
                            #action end


                        else:
                            if cnt5 >= 1:
                                break #loop5

                            eee = EarlyExitException(5, self.input)
                            raise eee

                        cnt5 += 1









            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end data


    # $ANTLR start pairs
    # /home/staal/devel/arff/arff.g:238:1: pairs returns [v] : '{' p1= pair ( ',' p2= pair )* '}' ;
    def pairs(self, ):

        v = None

        p1 = None

        p2 = None


               
        v = [];

        try:
            try:
                # /home/staal/devel/arff/arff.g:243:5: ( '{' p1= pair ( ',' p2= pair )* '}' )
                # /home/staal/devel/arff/arff.g:244:9: '{' p1= pair ( ',' p2= pair )* '}'
                self.match(self.input, 35, self.FOLLOW_35_in_pairs886)

                self.following.append(self.FOLLOW_pair_in_pairs898)
                p1 = self.pair()
                self.following.pop()

                #action start
                         
                v.append(p1);
                        
                #action end
                # /home/staal/devel/arff/arff.g:249:9: ( ',' p2= pair )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 43) :
                        alt7 = 1


                    if alt7 == 1:
                        # /home/staal/devel/arff/arff.g:250:13: ',' p2= pair
                        self.match(self.input, 43, self.FOLLOW_43_in_pairs932)

                        self.following.append(self.FOLLOW_pair_in_pairs948)
                        p2 = self.pair()
                        self.following.pop()

                        #action start
                                     
                        v.append(p2);
                                    
                        #action end


                    else:
                        break #loop7


                self.match(self.input, 36, self.FOLLOW_36_in_pairs983)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return v

    # $ANTLR end pairs


    # $ANTLR start pair
    # /home/staal/devel/arff/arff.g:260:1: pair returns [t] : INT value ;
    def pair(self, ):

        t = None

        INT11 = None
        value12 = None


        try:
            try:
                # /home/staal/devel/arff/arff.g:262:5: ( INT value )
                # /home/staal/devel/arff/arff.g:263:9: INT value
                INT11 = self.input.LT(1)
                self.match(self.input, INT, self.FOLLOW_INT_in_pair1013)

                self.following.append(self.FOLLOW_value_in_pair1023)
                value12 = self.value()
                self.following.pop()

                #action start
                         
                t =  (int(INT11.text), value12)
                        
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return t

    # $ANTLR end pair


    # $ANTLR start values
    # /home/staal/devel/arff/arff.g:271:1: values returns [v] : v1= value ( ',' v2= value )* ;
    def values(self, ):

        v = None

        v1 = None

        v2 = None


               
        v = [];

        try:
            try:
                # /home/staal/devel/arff/arff.g:276:5: (v1= value ( ',' v2= value )* )
                # /home/staal/devel/arff/arff.g:277:9: v1= value ( ',' v2= value )*
                self.following.append(self.FOLLOW_value_in_values1070)
                v1 = self.value()
                self.following.pop()

                #action start
                         
                v.append(v1);
                        
                #action end
                # /home/staal/devel/arff/arff.g:281:9: ( ',' v2= value )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 43) :
                        alt8 = 1


                    if alt8 == 1:
                        # /home/staal/devel/arff/arff.g:282:13: ',' v2= value
                        self.match(self.input, 43, self.FOLLOW_43_in_values1104)

                        self.following.append(self.FOLLOW_value_in_values1120)
                        v2 = self.value()
                        self.following.pop()

                        #action start
                                     
                        v.append(v2);
                                    
                        #action end


                    else:
                        break #loop8






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return v

    # $ANTLR end values


    # $ANTLR start value
    # /home/staal/devel/arff/arff.g:291:1: value returns [val] : ( '?' | FLOAT | INT | string );
    def value(self, ):

        val = None

        FLOAT13 = None
        INT14 = None
        string15 = None


               
        val = None;

        try:
            try:
                # /home/staal/devel/arff/arff.g:296:5: ( '?' | FLOAT | INT | string )
                alt9 = 4
                LA9 = self.input.LA(1)
                if LA9 == 44:
                    alt9 = 1
                elif LA9 == FLOAT:
                    alt9 = 2
                elif LA9 == INT:
                    alt9 = 3
                elif LA9 == QSTRING or LA9 == STRING or LA9 == 17 or LA9 == 18 or LA9 == 19 or LA9 == 20 or LA9 == 21 or LA9 == 22 or LA9 == 23 or LA9 == 24 or LA9 == 25 or LA9 == 26 or LA9 == 27 or LA9 == 28 or LA9 == 29 or LA9 == 30 or LA9 == 31 or LA9 == 37 or LA9 == 38 or LA9 == 39:
                    alt9 = 4
                else:
                    nvae = NoViableAltException("291:1: value returns [val] : ( '?' | FLOAT | INT | string );", 9, 0, self.input)

                    raise nvae

                if alt9 == 1:
                    # /home/staal/devel/arff/arff.g:297:9: '?'
                    self.match(self.input, 44, self.FOLLOW_44_in_value1180)

                    #action start
                             
                    val =  '?'
                            
                    #action end


                elif alt9 == 2:
                    # /home/staal/devel/arff/arff.g:302:9: FLOAT
                    FLOAT13 = self.input.LT(1)
                    self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_value1207)

                    #action start
                             
                    val =  float(FLOAT13.text)
                            
                    #action end


                elif alt9 == 3:
                    # /home/staal/devel/arff/arff.g:307:9: INT
                    INT14 = self.input.LT(1)
                    self.match(self.input, INT, self.FOLLOW_INT_in_value1234)

                    #action start
                             
                    val =  int(INT14.text)
                            
                    #action end


                elif alt9 == 4:
                    # /home/staal/devel/arff/arff.g:312:9: string
                    self.following.append(self.FOLLOW_string_in_value1261)
                    string15 = self.string()
                    self.following.pop()

                    #action start
                             
                    val =  string15
                            
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return val

    # $ANTLR end value

    class keyword_return(object):
        def __init__(self):
            self.start = None
            self.stop = None



    # $ANTLR start keyword
    # /home/staal/devel/arff/arff.g:319:1: keyword : ( ( 'numeric' | 'Numeric' | 'NUMERIC' ) | ( 'integer' | 'Integer' | 'INTEGER' ) | ( 'real' | 'Real' | 'REAL' ) | ( 'string' | 'String' | 'STRING' ) | ( 'relational' | 'Relational' | 'RELATIONAL' ) | ( 'date' | 'DATE' | 'Date' ) );
    def keyword(self, ):

        retval = self.keyword_return()
        retval.start = self.input.LT(1)

        try:
            try:
                # /home/staal/devel/arff/arff.g:320:5: ( ( 'numeric' | 'Numeric' | 'NUMERIC' ) | ( 'integer' | 'Integer' | 'INTEGER' ) | ( 'real' | 'Real' | 'REAL' ) | ( 'string' | 'String' | 'STRING' ) | ( 'relational' | 'Relational' | 'RELATIONAL' ) | ( 'date' | 'DATE' | 'Date' ) )
                # /home/staal/devel/arff/arff.g:
                if (17 <= self.input.LA(1) <= 31) or (37 <= self.input.LA(1) <= 39):
                    self.input.consume();
                    self.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_keyword0
                        )
                    raise mse





                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end keyword


    # $ANTLR start string
    # /home/staal/devel/arff/arff.g:329:1: string returns [s] : ( QSTRING | STRING | keyword );
    def string(self, ):

        s = None

        QSTRING16 = None
        STRING17 = None
        keyword18 = None


        try:
            try:
                # /home/staal/devel/arff/arff.g:331:5: ( QSTRING | STRING | keyword )
                alt10 = 3
                LA10 = self.input.LA(1)
                if LA10 == QSTRING:
                    alt10 = 1
                elif LA10 == STRING:
                    alt10 = 2
                elif LA10 == 17 or LA10 == 18 or LA10 == 19 or LA10 == 20 or LA10 == 21 or LA10 == 22 or LA10 == 23 or LA10 == 24 or LA10 == 25 or LA10 == 26 or LA10 == 27 or LA10 == 28 or LA10 == 29 or LA10 == 30 or LA10 == 31 or LA10 == 37 or LA10 == 38 or LA10 == 39:
                    alt10 = 3
                else:
                    nvae = NoViableAltException("329:1: string returns [s] : ( QSTRING | STRING | keyword );", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # /home/staal/devel/arff/arff.g:332:9: QSTRING
                    QSTRING16 = self.input.LT(1)
                    self.match(self.input, QSTRING, self.FOLLOW_QSTRING_in_string1430)

                    #action start
                             
                    s =  QSTRING16.text[1:-1]
                            
                    #action end


                elif alt10 == 2:
                    # /home/staal/devel/arff/arff.g:337:9: STRING
                    STRING17 = self.input.LT(1)
                    self.match(self.input, STRING, self.FOLLOW_STRING_in_string1456)

                    #action start
                             
                    s =  STRING17.text
                            
                    #action end


                elif alt10 == 3:
                    # /home/staal/devel/arff/arff.g:341:9: keyword
                    self.following.append(self.FOLLOW_keyword_in_string1476)
                    keyword18 = self.keyword()
                    self.following.pop()

                    #action start
                             
                    s =  self.input.toString(keyword18.start,keyword18.stop)
                            
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return s

    # $ANTLR end string


 

    FOLLOW_header_in_file57 = frozenset([40, 41, 42])
    FOLLOW_data_in_file67 = frozenset([1])
    FOLLOW_set_in_header93 = frozenset([6, 7, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 37, 38, 39])
    FOLLOW_string_in_header113 = frozenset([14, 15, 16])
    FOLLOW_adecls_in_header133 = frozenset([1])
    FOLLOW_adecl_in_adecls181 = frozenset([1, 14, 15, 16])
    FOLLOW_adecl_in_adecls217 = frozenset([1, 14, 15, 16])
    FOLLOW_set_in_adecl272 = frozenset([6, 7, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 37, 38, 39])
    FOLLOW_string_in_adecl292 = frozenset([17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 35, 37, 38, 39])
    FOLLOW_datatype_in_adecl302 = frozenset([1])
    FOLLOW_set_in_datatype348 = frozenset([1])
    FOLLOW_set_in_datatype366 = frozenset([1])
    FOLLOW_set_in_datatype384 = frozenset([1])
    FOLLOW_set_in_datatype411 = frozenset([1])
    FOLLOW_set_in_datatype429 = frozenset([14, 15, 16])
    FOLLOW_adecls_in_datatype445 = frozenset([32, 33, 34])
    FOLLOW_set_in_datatype455 = frozenset([6, 7, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 37, 38, 39])
    FOLLOW_string_in_datatype476 = frozenset([1])
    FOLLOW_date_in_datatype496 = frozenset([1])
    FOLLOW_35_in_datatype516 = frozenset([4, 5, 6, 7, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 37, 38, 39, 44])
    FOLLOW_values_in_datatype518 = frozenset([36])
    FOLLOW_36_in_datatype520 = frozenset([1])
    FOLLOW_set_in_date565 = frozenset([1, 6, 7, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 37, 38, 39])
    FOLLOW_string_in_date599 = frozenset([1])
    FOLLOW_set_in_data651 = frozenset([4, 5, 6, 7, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 35, 37, 38, 39, 44])
    FOLLOW_pairs_in_data702 = frozenset([1, 35])
    FOLLOW_values_in_data808 = frozenset([1, 4, 5, 6, 7, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 37, 38, 39, 44])
    FOLLOW_35_in_pairs886 = frozenset([4])
    FOLLOW_pair_in_pairs898 = frozenset([36, 43])
    FOLLOW_43_in_pairs932 = frozenset([4])
    FOLLOW_pair_in_pairs948 = frozenset([36, 43])
    FOLLOW_36_in_pairs983 = frozenset([1])
    FOLLOW_INT_in_pair1013 = frozenset([4, 5, 6, 7, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 37, 38, 39, 44])
    FOLLOW_value_in_pair1023 = frozenset([1])
    FOLLOW_value_in_values1070 = frozenset([1, 43])
    FOLLOW_43_in_values1104 = frozenset([4, 5, 6, 7, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 37, 38, 39, 44])
    FOLLOW_value_in_values1120 = frozenset([1, 43])
    FOLLOW_44_in_value1180 = frozenset([1])
    FOLLOW_FLOAT_in_value1207 = frozenset([1])
    FOLLOW_INT_in_value1234 = frozenset([1])
    FOLLOW_string_in_value1261 = frozenset([1])
    FOLLOW_set_in_keyword0 = frozenset([1])
    FOLLOW_QSTRING_in_string1430 = frozenset([1])
    FOLLOW_STRING_in_string1456 = frozenset([1])
    FOLLOW_keyword_in_string1476 = frozenset([1])

