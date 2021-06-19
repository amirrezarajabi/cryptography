# cryptography

## cryptosystem(P, E, K, **ε**, D):

   * P is a finite set of possible plaintexts;

   * E is a finite set of possible ciphertexts;

   * K is a finite set of possible keys;

   * For each k ∈ K, there is an encryption rule  ek ∈  **ε** corresponding decryption rule  dk ∈  D. each ek: P**→** E and dk: E **→** P are functions such that: `d_k(e_k(x)) = x` for every element plain text x ∈ P.
  
 
 ## Cryptography methods
 
 * ### [Shift Cipher](https://github.com/amirrezarajabi/cryptography/blob/main/SHIFT_CIPHER.py)
 
  * P = E = K = [0:26]
 
  * for k in K define: `e_k(x) = (x + k) % 26` and `d_k(y) = (y - k) % 26`
 
  * example: `wewillmeetatmidnight` and `k = 11` encrypt to `hphtwwxppelextoytrse`
 
