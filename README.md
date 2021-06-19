# cryptography

## cryptosystem(P, E, K, **ε**, D):

   * P is a finite set of possible plaintexts;

   * E is a finite set of possible ciphertexts;

   * K is a finite set of possible keys;

   * For each k ∈ K, there is an encryption rule  ek ∈  **ε** corresponding decryption rule  dk ∈  D. each ek: P**→** E and dk: E **→** P are functions such that: `d_k(e_k(x)) = x` for every element plain text x ∈ P.
  
 
 ## Cryptography methods
 
  * ### [Shift Cipher](https://github.com/amirrezarajabi/cryptography/blob/main/cryptography_methods/AFFINE_CIPHER.py)
 
    * P = E = K = [0:26]
 
    * for k in K define: `e_k(x) = (x + k) % 26` and `d_k(y) = (y - k) % 26`
 
    * example: `wewillmeetatmidnight` and `k = 11` encrypt to `hphtwwxppelextoytrse`

  * ### [Substitution Cipher](https://github.com/amirrezarajabi/cryptography/blob/main/cryptography_methods/SUBSTITUTION_CIPHER.py)
  
    * P = E = [0:26]
    
    * K consists of all possible permutation of the 26 symobols [0:26]

    * for each permutation π ∈ K, define: `e_π(x) = π(x)` and `d_π(y) = arcπ(y)`
    
    * example: `wewillmeetatmidnight` and `k = 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 0 1 2 3 4 5 6 7 8 9 10` encrypt to `hphtwwxppelextoytrse`
  
  * ### [Substitution Cipher](https://github.com/amirrezarajabi/cryptography/blob/main/cryptography_methods/AFFINE_CIPHER.py)
  
    * P = E = [0:26]
    
    * K = {(a, b) ∈ [0:25] * [0:26] : gcd(a, 26) = 1}

    * for K = (a, b) ∈ K, define: `e_k(x) = (ax + b) % 26` and `d_k(y) = arca(y - b)`
    
    * example: `wewillmeetatmidnight` and `k = 1 11` encrypt to `hphtwwxppelextoytrse`
