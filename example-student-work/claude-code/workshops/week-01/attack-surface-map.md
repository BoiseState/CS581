# Workshop 1 — Nuclear Plant Attack Surface Map
## CS 581 · Week 1 · Foundations

**Student:** [Your Name] | **Date:** Week 1
**Tool used:** Claude Code (claude-opus-4, extended thinking: high)

---

## Overview

This map characterizes the attack surface of a generic large US nuclear power plant based on public-domain architecture documentation, NRC regulatory guidance, and ICS/SCADA security literature. It is explicitly generic — no facility-specific information is used or implied. The map is organized by three layers corresponding to the standard IT/OT/physical taxonomy, with threat vectors and notable gaps identified for each.

---

## Layer 1 — IT (Corporate / Business Network)

| Component | Role | Threat Vectors | Notable Gaps | Confidence & Provenance |
|---|---|---|---|---|
| Corporate email infrastructure | Business communication | Phishing (primary initial access vector for most ICS incidents); BEC for procurement fraud | Email security controls often lag behind enterprise IT; legacy mail servers at some utilities | `documented` — CISA ICS-CERT reporting; Dragos ICS threat reports |
| Business applications (ERP, procurement, HR) | Plant operations support | Supply chain fraud; credential theft; lateral movement to IT/OT bridge systems | ERP systems with connections to maintenance scheduling can be pivot to OT | `inferred` — from general IT/OT architecture literature; no nuclear-specific public incident cited |
| Corporate VPN / remote access | Off-site workforce access | Credential stuffing; MFA bypass; session hijacking | VPN concentrators are high-value targets; not all nuclear IT environments have MFA uniformly deployed | `documented` — CISA advisory AA21-008A and related VPN vulnerability advisories |
| Document management systems | Technical documentation storage | Sensitive document exfiltration; reconnaissance for OT targeting | Technical specifications for control systems may reside in IT document stores | `inferred` — standard IT security architecture; no nuclear-specific public incident cited |
| Vendor/contractor remote access portals | Third-party maintenance | Supply chain compromise; compromised vendor credentials; malicious insider at vendor | Vendor access is a documented attack vector; contractual constraints limit monitoring | `documented` — multiple ICS vendor compromise incidents (public); NEI 08-09 acknowledges this vector |
| Historian servers (IT-facing) | Data aggregation from OT | Pivot point between IT and OT networks | Historians are the most common IT-OT bridge; security controls vary widely | `documented` — named in NIST SP 800-82 as a primary IT-OT bridge risk; Dragos and Claroty research |
| Active Directory / identity infrastructure | Authentication and authorization | Domain compromise enables lateral movement across IT and potentially to IT-OT bridges | Single AD forest spanning IT and OT is a documented risk | `documented` — CISA guidance on Active Directory hardening; Volt Typhoon TTP reporting |

**IT layer summary:** The IT layer is the most exposed to external threats and the most familiar to conventional cybersecurity defenders. The primary risk is not direct impact from IT compromise but rather using IT access as a staging point for OT intrusion — particularly via historian servers, vendor access portals, and identity infrastructure.

---

## Layer 2 — OT (Operational Technology / Industrial Control Systems)

| Component | Role | Threat Vectors | Notable Gaps | Confidence & Provenance |
|---|---|---|---|---|
| Distributed Control System (DCS) | Primary control of non-safety plant processes | Firmware manipulation; HMI compromise; engineering workstation as initial access | DCS from major vendors have documented vulnerability histories; patch cadence constrained by outage schedule | `documented` — ICS-CERT advisories for Emerson, Honeywell, Siemens DCS platforms (public) |
| Safety Instrumented Systems (SIS) / Reactor Protection System (RPS) | Automatic safety function actuation | Stuxnet-class attacks targeting safety logic; intentional defeat to prevent automatic shutdown | Highest consequence target; often air-gapped but with maintenance interfaces | `documented` — Stuxnet (public); TRITON/TRISIS SIS attack (2017, public post-incident reporting) |
| Human-Machine Interfaces (HMIs) | Operator visibility and control | HMI-based malware; display manipulation to mislead operators | HMIs often run Windows with limited patch capability; operator trust in display is a cognitive attack surface | `documented` — CRASHOVERRIDE/Industroyer (2016 Ukraine); ICS-CERT HMI advisories |
| Engineering Workstations | Configuration, programming, diagnostics of OT systems | Primary vector for OT malware introduction (removable media, software updates) | Engineering workstations frequently bridge IT and OT; anti-malware coverage inconsistent | `documented` — Stuxnet (removable media vector); multiple ICS-CERT advisories |
| Industrial protocols (Modbus, DNP3, OPC-UA) | Inter-device communication | Protocol-level attacks (replay, spoofing, injection) — most legacy protocols have no authentication | Legacy protocols designed for reliability, not security | `documented` — DNP3 lack of authentication documented in IEC TC57 working group reports; Modbus specification is public |
| Wireless systems (if present) | Portable instruments, some monitoring | RF interception; rogue access point injection | Wireless in nuclear plants is regulated but present for some monitoring functions | `inferred` — from ICS wireless security literature; no nuclear-specific public incident cited |
| Removable media | Software updates, data transfer | Deliberate or inadvertent malware introduction | Removable media controls are a regulatory requirement but enforcement is procedural | `documented` — Stuxnet primary vector (public); NRC information notices on removable media |
| Safety logic controllers (PLC/DCS safety modules) | Implementing safety functions | Logic manipulation targeting specific failure modes | Most critical component; most constrained in terms of defensible modification | `documented` — TRITON/TRISIS (2017) targeted safety controllers specifically; public post-incident analysis |

**OT layer summary:** The OT layer is where cyber attacks translate into physical consequences. The primary challenge is the combination of legacy systems (limited patchability), safety primacy (controls cannot impair safety function availability), and the specialized knowledge required to understand OT attack paths — most IT security professionals cannot evaluate OT risk without ICS-specific training.

---

## Layer 3 — Physical / Cyber Intersection

| Component | Role | Threat Vectors | Notable Gaps | Confidence & Provenance |
|---|---|---|---|---|
| Electronic Physical Access Control Systems (ePACS) | Badge-based access to protected area and vital areas | Cloning badge credentials; compromising ePACS server to grant unauthorized access | ePACS are networked; cybersecurity governed by both 10 CFR 73 and 73.54 — overlap creates regulatory ambiguity | `inferred` — from physical security and access control literature; nuclear-specific ePACS incidents not publicly documented |
| IP-based surveillance systems (CCTV) | Physical security monitoring | CCTV systems as network pivot points; camera manipulation to blind security monitoring | IP cameras frequently under-patched; compromise provides reconnaissance and network access | `documented` — Mirai botnet and derivatives (IP camera exploitation); CISA advisories on IP camera vulnerabilities |
| Environmental and radiation monitoring systems | Detect abnormal conditions | Sensor manipulation to mask abnormal conditions or trigger false alarms | Some monitoring systems have data connections; spoofed readings can mislead operators | `theoretical` — no public incident of radiation monitor manipulation cited; plausible from architecture |
| HVAC and facility management systems | Environmental control for electronics and personnel | Disruption of cooling for critical electronics; building management as network entry point | Building automation systems often poorly segmented; physical consequences (temperature) plus network connectivity | `documented` — building management system attacks documented in enterprise sector; nuclear-specific cases not public |
| Uninterruptible Power Supplies (UPS) with network management | Backup power for critical systems | Exploitation of network management cards; pivot to internal network | UPS network management cards have documented critical vulnerabilities; often overlooked in OT programs | `documented` — CISA advisory AA22-091A (UPS network management card vulnerabilities, 2022) |
| Emergency diesel generator control interfaces | Backup power for safety systems | Manipulation to prevent startup during loss of offsite power | Generator control interfaces vary in cyber exposure; some have remote monitoring with inadequate protection | `theoretical` — no public incident of EDG control manipulation; plausible and high-consequence |

**Physical/cyber summary:** This layer is where cyber attacks can directly affect physical security functions — bypassing access controls, blinding surveillance, or disrupting power to critical systems. The regulatory framework splits responsibility between physical security (10 CFR 73) and cybersecurity (10 CFR 73.54), creating potential gaps at the intersection.

---

## What This Map Cannot Tell You

This map is a generic characterization based on public-domain knowledge. The following information would be required to convert it into a facility-specific assessment — and obtaining it without authorization would be illegal and potentially a federal crime.

1. **Actual network topology.** Which systems are truly air-gapped vs. which have maintenance connections, data historians, or vendor access links. "Air-gapped" in the regulatory sense often means "no persistent connection" — not "no connection ever."

2. **Historian server configuration.** Whether the IT-OT historian bridge is properly segmented, what data flows across it, and whether security controls on the historian are adequate. This single component represents the highest-probability OT intrusion path in most nuclear plant architectures.

3. **Vendor access specifics.** Which vendors have remote diagnostic capability, what credentials they use, how sessions are monitored, and whether the plant can unilaterally terminate access. Some vendor contracts make this access a maintenance requirement.

4. **Patch status of every listed component.** The actual vulnerability exposure of DCS, HMI, and OT components depends entirely on their patch status, which varies by outage schedule and vendor support.

5. **CDA determination.** Which systems the licensee has formally identified as Critical Digital Assets under their NRC-approved Cyber Security Plan. Systems excluded from the CDA list receive different levels of protection.

6. **Physical/cyber separation specifics.** Whether ePACS, surveillance, and facility management systems share any network infrastructure with OT systems — a configuration that regulatory guidance discourages but that exists at some facilities due to legacy architecture.

7. **Insider threat profile.** The human element of the attack surface — which personnel have access to which systems, what behavioral monitoring is in place, and how the licensee implements its insider mitigation program under 10 CFR 73.56.

**The gap between this map and a real assessment is significant.** A practitioner conducting an authorized assessment at a specific facility would spend significant time filling in these unknowns before making any risk prioritization decisions. The map above represents the starting hypothesis — not the finding.

---

*Committed to primary-repo/workshops/week-01/attack-surface-map.md*
*Session log: see session-log.md*
