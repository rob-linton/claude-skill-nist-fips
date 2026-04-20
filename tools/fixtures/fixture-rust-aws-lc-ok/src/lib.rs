// Fixture: Rust using aws-lc-rs AES-256-GCM in FIPS mode. Expected: OK.

use aws_lc_rs::aead::{Aad, LessSafeKey, Nonce, UnboundKey, AES_256_GCM};
use aws_lc_rs::rand::{SecureRandom, SystemRandom};

pub fn encrypt(plaintext: &mut Vec<u8>, key_bytes: &[u8; 32]) -> [u8; 12] {
    let rng = SystemRandom::new();
    let mut nonce_bytes = [0u8; 12];
    rng.fill(&mut nonce_bytes).unwrap();
    let unbound = UnboundKey::new(&AES_256_GCM, key_bytes).unwrap();
    let key = LessSafeKey::new(unbound);
    let nonce = Nonce::assume_unique_for_key(nonce_bytes);
    key.seal_in_place_append_tag(nonce, Aad::empty(), plaintext)
        .expect("encryption failed");
    nonce_bytes
}
