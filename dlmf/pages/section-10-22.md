# §10.22 Integrals

Source: [https://dlmf.nist.gov/10.22](https://dlmf.nist.gov/10.22)

Observed version: 1.2.7, release date 2026-06-15.

## Purpose

Documents the `10.22` section of Chapter 10, Bessel Functions. The page focuses on Integrals.

## Page Structure

- Indefinite Integrals.
- Integrals over Finite Intervals.
- Integrals over the Interval ( x , infinity ).
- Integrals over the Interval ( 0 , infinity ).
- Hankel Transform.
- Compendia.

## Signals

- Keywords: cylinder functions, indefinite, integrals, integrals of Bessel and Hankel functions, products, over finite intervals, trigonometric arguments, convolutions, fractional, Bessel functions, orthogonal properties, orthogonality, over infinite intervals, Mellin transform, Laplace transform, Weber-Schafheitlin discontinuous integrals, area of triangle, triple.
- Formula blocks detected: 67.
- Tables detected: 0.
- Figures detected: 0.

## Notes

- See Watson ( 1944 , pp. 132-136) . For ( 10.22.1 )-( 10.22.3 ) differentiate and use ( 10.6.2 ), ( 11.4.27 ), ( 11.4.28 ).
- For ( 10.22.8 )-( 10.22.12 ) see Luke ( 1962 , pp. 51-53) . To verify ( 10.22.13 ) construct the expansion of the left-hand side in powers of z by use of ( 10.2.2 ), followed by term-by-term integration with the aid of ( 5.12.5 ) and ( 5.12.1 ). Then compare the result with the corresponding expansion of the right-hand side obtained from ( 10.8.3 ). Next, the result  0 2   J 2    ( 2  z  sin   )  e  2  i      d  =   e  i      J  +   ( z )  J  -   ( z ) ,    > - 1 2 , is proved in a similar manner with the aid of ( 5.12.6 ) in place of ( 5.12.5 )-from which ( 10.22.14 ) and ( 10.22.15 ) both follow. ( 10.22.17 ) follows by combining ( 10.22.13 ) and ( 10.2.3 ); ( 10.22.16 ) is a special case of ( 10.22.14 ). For ( 10.22.18 ) replace  by 1 2   -  and set  = n in ( 10.22.17 ); then apply ( 10.2.3 ) and let   0 . For ( 10.22.19 ), ( 10.22.22 ), ( 10.22.25 ), ( 10.22.26 ) see Watson ( 1944 , Chapter 12) . (In the case of ( 10.22.25 ), page 374 of this reference lacks a factor 1 2 on the right-hand side.) The verification of ( 10.22.20 ) is similar to that of ( 10.22.13 ), the role of ( 5.12.5 ) now being played by ( 5.12.2 ). For ( 10.22.21 ) combine ( 10.2.3 ) and ( 10.22.20 ). For ( 10.22.23 ) and ( 10.22.24 ) see Luke ( 1962 , p. 302 (36) and p. 303 (39), respectively) . For ( 10.22.27 ) see Watson ( 1944 , p. 151) . For ( 10.22.28 ), ( 10.22.29 ) differentiate and use ( 10.6.2 ). For ( 10.22.30 ) with n  1 it follows by differentiation and use of ( 10.6.2 ) that the left-hand side equals  0 x t - 1  J n 2  ( t )  d t - 1 2  J n 2  ( x ) ; application of Watson ( 1944 , p. 152) yields the second result, then for the first result refer to ( 10.23.3 ). Some modifications of the proof of ( 10.22.30 ) are needed when n = 0 . For ( 10.22.31 )-( 10.22.35 ) see Watson ( 1944 , p. 380) . For ( 10.22.36 ) replace t by z - t , substitute for t  via ( 10.23.15 ) (with z replaced by t , and  replaced by  ), and then apply ( 10.22.34 ). For ( 10.22.37 ) use ( 10.22.4 ) and ( 10.22.5 ); a similar proof applies to ( 10.22.38 ) after replacing    1  ( a  z ) and    1  ( b  z ) by      ( a  z ) and      ( b  z ) , respectively, by means of ( 10.6.2 ).
- For the first result in ( 10.22.39 ) use ( 10.22.43 ) with  = 0 and  replaced by  - 1 , split the integration range at t = x and take limits as   0 ; for the second result substitute into the first result by ( 10.2.2 ) and integrate term by term. ( 10.22.40 ), is proved in a similar manner, starting from ( 10.22.44 ) and substituting by means of ( 10.8.2 ) and ( 10.2.2 ) with  = 0 for the term-by-term integration.
- For ( 10.22.41 )-( 10.22.45 ) see Luke ( 1962 , pp. 56-57) . For ( 10.22.46 ) see Erdlyi et al. ( 1953b , p. 96) . ( 10.22.47 ) is the special case of Eq. (6) of Watson ( 1944 , 13.53) obtained by setting  = b = 0 ,  =  + 1 , and subsequently replacing k by b . For ( 10.22.48 ) see Sneddon ( 1966 , Eq. (2.1.32)) . For ( 10.22.49 )-( 10.22.59 ) see Watson ( 1944 , pp. 385, 394, 403-405, 407; there is an error in Eq. (1), p. 407) . For ( 10.22.60 ) differentiate ( 10.22.59 ) with respect to  and use ( 10.2.4 ) with n = 0 . For ( 10.22.61 ) see Watson ( 1944 , p. 405) . ( 10.22.62 ) follows from ( 10.22.56 ) with  =  -  - 1 and ( 15.4.6 ). For ( 10.22.63 ), ( 10.22.64 ) see Watson ( 1944 , p. 404) . For ( 10.22.65 ) apply ( 10.22.56 ) with  =  = 0 , then let   1 . For ( 10.22.66 ), ( 10.22.67 ) see Watson ( 1944 , pp. 389, 395) . For ( 10.22.68 ) set a = b in ( 10.22.67 ), differentiate with respect to  and apply ( 10.2.4 ) and ( 10.27.5 ) with n = 0 . For ( 10.22.69 ), ( 10.22.70 ), see Watson ( 1944 , p. 429, Eqs. (3),(4), with  =  + 1 in (3)) . For ( 10.22.71 ), ( 10.22.72 ) see Watson ( 1944 , pp. 411, 412) . For ( 10.22.74 ), ( 10.22.75 ) see Watson ( 1944 , p. 411) and Askey et al. ( 1986 ) .
