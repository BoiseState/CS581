# Attack Surface Verification — Digital Control System (DCS)
## CS 581 Workshop 1 | Jordan Reyes | Sep 8, 2026

**Sources used for verification:**
1. NIST SP 800-82 Rev. 3 — Guide to Operational Technology (OT) Security (September 2023)
2. ICS-CERT Advisory ICSA-22-172-06 — OPC Foundation OPC UA .NET Standard (June 2022)

**Verification method:** I loaded each source into Claude Sonnet, then asked it to read each row of my three layer files and flag any claim that contradicted, overstated, or could not be substantiated by the source. I then independently verified each flag against the source text.

---

## Corrections Table

| Layer | Original Claim | Error Type | Corrected Entry | Source |
|---|---|---|---|---|
| IT | "OPC-UA security profiles (Sign, Sign & Encrypt) are optional — many deployments leave encryption disabled" | Overstated as universal — the advisory is specific to the .NET Standard implementation | "OPC-UA security profiles are optional in the OPC UA .NET Standard implementation; enforcement is configuration-dependent. The advisory does not generalize to all OPC-UA stacks." | ICSA-22-172-06, Section 2 |
| OT | "Controller firmware authenticity verification is not mandated under 10 CFR 73.54" | Incomplete — 10 CFR 73.54 requires a cyber security plan that addresses supply chain; the gap is in vendor implementation, not the rule itself | "10 CFR 73.54 requires licensees to address supply chain risks in their cyber security plan; firmware authenticity verification is not explicitly mandated in the rule text but is addressed indirectly through supply chain requirements in Appendix E" | NIST SP 800-82r3, Section 5.5.2 |
| OT | "Modbus was designed in 1979 for isolated serial links" | The date is correct but the implication that this means no security controls exist is overstated | "Modbus was designed in 1979 without authentication or encryption. NIST SP 800-82r3 identifies compensating controls (network segmentation, anomaly detection) as the primary mitigation — the protocol itself cannot be fixed." | NIST SP 800-82r3, Section 6.2.4 |
| Physical | "Physical tamper detection on DCS cabinets is not uniformly required" | Accurate but I attributed this to RG 5.71 Section 4 — RG 5.71 does not address cabinet tamper detection directly | "RG 5.71 does not specify physical tamper detection requirements for DCS cabinets. IAEA NSS No. 17-T addresses this but it is a guidance document, not a US regulatory requirement." | RG 5.71 (absence of text); IAEA NSS No. 17-T |

---

## Confidence Adjustments After Verification

- **OPC-UA encryption claim**: downgraded from `documented` to `documented (scoped)` — the advisory is specific to the .NET Standard implementation; the general claim about widespread disabled encryption is industry-common knowledge but not directly supported by this advisory alone.
- **Modbus / Purdue model interaction**: confidence unchanged — NIST SP 800-82r3 Section 6.2.4 is explicit and directly supports the claim.
- **10 CFR 73.54 firmware mandate**: revised to note that supply chain requirements exist but are implementation-delegated; the gap I identified is real but more nuanced than the original claim.

---

## What This Verification Cannot Resolve

1. **Vendor-specific vulnerability data.** Neither source contains CVE lists for specific DCS vendors. Verification against NIST NVD for Ovation or ABB 800xA would require a separate pass — I did not do this for W1.

2. **Current patch posture.** No public source can tell me whether a specific plant is running patched firmware. The verification exercise confirms that the threat vectors are real and documented; it cannot tell me whether a specific facility has mitigated them.

3. **Implementation gaps vs. regulatory gaps.** Several of my original "notable gaps" are implementation problems at specific plants, not gaps in the regulatory framework. The verification exercise helped me distinguish these — but it cannot tell me what specific plants actually do.

**Bottom line:** The verification exercise caught three material errors in my original output — two were scope overstatements, one was a wrong citation. None changed the core threat analysis, but they would have been wrong in a submission to a real client. The column-by-column format forced me to check every claim rather than skimming for obvious errors. I will use this format for all subsequent workshops.
