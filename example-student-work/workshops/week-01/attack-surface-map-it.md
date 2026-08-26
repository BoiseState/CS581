# Attack Surface Map — Digital Control System (DCS): IT Layer
## CS 581 Workshop 1 | Jordan Reyes | Sep 8, 2026

**System:** Digital Control System (DCS)  
**Purdue Zone:** Level 2 — Supervisory  
**Regulatory classification:** Critical Digital Asset (CDA) under 10 CFR 73.54  
**Representative implementations:** Westinghouse Ovation, ABB System 800xA, Yokogawa CENTUM VP, Emerson DeltaV

---

## Layer 1 — IT (Corporate / Level 4)

| Component | Role | Threat Vectors | Notable Gaps | Confidence & Provenance |
|---|---|---|---|---|
| Vendor remote access tunnels | Vendors require periodic remote access for maintenance and updates; typically VPN-gated | Supply chain compromise of vendor credentials; malicious update package; vendor network pivot into plant | No public standard for how nuclear plants authenticate vendor remote sessions under RG 5.71 | `inferred` — RG 5.71 Section 3.1.5 addresses vendor access; specifics are implementation-dependent |
| Corporate Active Directory / identity federation | Enterprise identity system that may share authentication infrastructure with plant engineering workstations | Credential theft from corporate network used to pivot to plant-side accounts; pass-the-hash attacks | The boundary between corporate AD and plant-side identity is not defined in any public document I found | `inferred` — NIST SP 800-82r3 Section 5.2; ICS-CERT Advisory ICSA-21-336-02 |
| OPC-UA gateway to historian (PPC) | Data bridge from DCS to Plant Process Computer; exports process data upward to Level 3 | Historian exploitation used to reverse-engineer DCS process states; malformed OPC-UA packets pushed back into DCS namespace | OPC-UA security profiles (Sign, Sign & Encrypt) are optional — many deployments leave encryption disabled | `documented` — ICS-CERT Advisory ICSA-22-172-06; Dragos Year in Review 2023; NIST SP 800-82r3 |

**Layer summary:** The IT layer is where the DCS connects to enterprise infrastructure. The two highest-risk entry points are vendor remote access (supply chain risk) and the OPC-UA gateway (where process data crosses the Level 2/3 boundary). Both are documented threat vectors with confirmed real-world exploitation precedent. The identity federation gap is the least documented but potentially the widest: if corporate AD credentials can be used to reach plant engineering workstations, the entire Purdue model separation fails at the credential layer.
