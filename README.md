# cryptography

## cryptosystem(P, E, K, **ε**, D):

###					P is a finite set of possible plaintexts;

###     		E is a finite set of possible ciphertexts;

### 		K is a finite set of possible keys;

### 		For each k ∈ K, there is an encryption rule  ek ∈  **ε**        

				### 			corresponding decryption rule  dk ∈ D. each ek: P **→** E 

### 			and dk: E **→** P are functions such that :

$$
d_k(e_k(x)) = x
$$

###  			for every element plain text x ∈ P.







