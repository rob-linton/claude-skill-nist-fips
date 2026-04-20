// Fixture: Rust using ChaCha20-Poly1305 (non-FIPS). Expected: FAIL.

use chacha20poly1305::{
    aead::{Aead, KeyInit, OsRng},
    ChaCha20Poly1305, Nonce,
};

pub fn encrypt(plaintext: &[u8], key: &[u8; 32], nonce: &[u8; 12]) -> Vec<u8> {
    let cipher = ChaCha20Poly1305::new(key.into());
    let nonce = Nonce::from_slice(nonce);
    cipher.encrypt(nonce, plaintext).expect("encryption failed")
}
