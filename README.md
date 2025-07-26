# 🎓 University SSI Issuer Cloud Agent

This is a **Verifiable Credential Issuer Application** used by universities to issue digital **degree credentials** to students using **Self-Sovereign Identity (SSI)** principles.

Built with a **cloud-based Veramo agent**, it issues W3C-compliant credentials that students can receive in their SSI wallets.

---

## 🏗️ Tech Stack

- 🌐 Node.js (Express)
- 🧠 Veramo (Core + Credential W3C + DID JWT)
- ☁️ Cloud-ready (Dockerized, deployable to any cloud server)
- 🔑 DID methods (e.g., did:ethr, did:key, did:web)

---

## 🧑‍🎓 Use Case

> A university administrator uses this backend to issue **degree credentials** to students who have completed their studies. The credential is cryptographically signed and sent to the student's DID.

---

## 📄 Credential Example (Degree VC)

```json
{
  "@context": ["https://www.w3.org/2018/credentials/v1"],
  "type": ["VerifiableCredential", "DegreeCredential"],
  "issuer": "did:ethr:0x1234...abcd",
  "credentialSubject": {
    "id": "did:key:z6Mk...",
    "name": "John Doe",
    "degree": {
      "type": "BachelorDegree",
      "name": "B.Sc. in Computer Science"
    },
    "university": "University of Example"
  },
  "issuanceDate": "2025-07-25T00:00:00Z",
  "proof": {
    "type": "JwtProof2020",
    "created": "...",
    "proofPurpose": "assertionMethod",
    ...
  }
}
