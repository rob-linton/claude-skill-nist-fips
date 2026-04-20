// Fixture: Go program using AES-GCM but without FIPS mode enabled.
// Expected: library-check FAIL (no FIPS mode), startup-assertion FAIL.
package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"fmt"
)

func main() {
	key := make([]byte, 32)
	_, _ = rand.Read(key)
	block, _ := aes.NewCipher(key)
	gcm, _ := cipher.NewGCM(block)
	nonce := make([]byte, gcm.NonceSize())
	_, _ = rand.Read(nonce)
	ct := gcm.Seal(nil, nonce, []byte("hello"), nil)
	fmt.Printf("%x\n", ct)
}
