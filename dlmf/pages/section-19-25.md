# §19.25 Relations to Other Functions

Source: [https://dlmf.nist.gov/19.25](https://dlmf.nist.gov/19.25)

Observed version: 1.2.7, release date 2026-06-15.

## Purpose

Documents the `19.25` section of Chapter 19, Elliptic Integrals. The page focuses on Relations to Other Functions.

## Page Structure

- Legendre's Integrals as Symmetric Integrals.
- Bulirsch's Integrals as Symmetric Integrals.
- Symmetric Integrals as Legendre's Integrals.
- Theta Functions.
- Jacobian Elliptic Functions.
- Weierstrass Elliptic Functions.
- Hypergeometric Function.

## Signals

- Keywords: Legendre's elliptic integrals, relations to other functions, symmetric elliptic integrals, transformations replaced by symmetry, Bulirsch's elliptic integrals, relation to symmetric elliptic integrals, theta functions, Jacobian elliptic functions, interrelations, Weierstrass elliptic functions, Appell functions, Lauricella's function, hypergeometric function.
- Formula blocks detected: 50.
- Tables detected: 0.
- Figures detected: 0.

## Notes

- ( 19.25.1 ), ( 19.25.2 ), and ( 19.25.3 ) are derived from the incomplete cases. For ( 19.25.4 ) put c = 1 in ( 19.25.16 ). ( 19.25.5 ) and ( 19.25.7 ) come from Carlson ( 1977b , (9.3-2) and (9.3-3)) . For ( 19.25.6 ) and ( 19.25.12 ) apply ( 19.18.4 ) to ( 19.25.5 ) and ( 19.25.8 ), respectively. ( 19.25.8 ) and ( 19.25.15 ) are special cases of ( 19.16.12 ). To get ( 19.25.9 ), ( 19.25.10 ), and ( 19.25.11 ), let ( c - 1 , c - k 2 , c ) = ( x , y , z ) and eliminate R G between ( 19.25.7 ) and each of the three forms of ( 19.25.10 ) obtained by permuting x , y and z . For ( 19.25.13 ) combine ( 19.2.6 ) and ( 19.25.9 ). For ( 19.25.14 ) see Zill and Carlson ( 1970 , (2.5)) . For ( 19.25.16 ) substitute ( 19.25.14 ) in ( 19.7.8 ) and use ( 19.2.20 ).
- Rewrite Bulirsch's integrals ( 19.2(iii) ) in terms of Legendre's integrals, then use  19.25(i) to convert them to R -functions.
- Define c = csc 2   , write ( x , y , z , p ) / ( z - x ) = ( c - 1 , c - k 2 , c , c -  2 ) , then use ( 19.25.5 ), ( 19.25.9 ), ( 19.25.14 ), and ( 19.25.7 ) to prove ( 19.25.24 ), ( 19.25.25 ), ( 19.25.26 ), and ( 19.25.27 ), respectively.
- To prove ( 19.25.29 ) use ( cs , ds , ns ) = ( cn , dn , 1 ) / sn (suppressing variables (u,k)). For ( 19.25.30 ) see Carlson ( 2006a , Comments following proof of Proposition 4.1) . For ( 19.25.31 ) see Carlson ( 2004 , (1.8)) . In ( 19.25.32 ), ( 19.25.33 ), and ( 19.25.34 ), substitute x = p  s  ( u , k ) , s  p  ( u , k ) , and p  q  ( u , k ) , respectively, to recover ( 19.25.31 ).
- To prove ( 19.25.35 ) use ( 23.6.36 ), with z =   (  ) as prescribed in the text that follows ( 23.6.36 ), substitute u = t +   (  ) and compare with ( 19.16.1 ). The undetermined  in ( 19.25.35 ) is a consequence of the multivaluedness of the square-roots in ( 19.16.4 ). For ( 19.25.37 ) we combine its derivative with ( 19.18.7 ) and obtain from ( 19.25.35 ) that ( 19.25.37 ) holds modulo a constant of integration. Combining  23.2(ii) with ( 19.23.6_5 ) shows us that both sides of ( 19.25.37 ) are ( z + 2   ) - 1 + O  ( z + 2   ) , as z  - 2   , and hence the constant of integration is zero. For ( 19.25.38 ) and ( 19.25.39 ) take z = -  in ( 19.25.35 ) and ( 19.25.37 ), respectively. For ( 19.25.40 ) combine Erdlyi et al. ( 1953b , 13.12(22), 13.13(22)) , ( 19.25.35 ) and ( 19.16.1 ).
