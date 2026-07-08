# Generic US Nuclear Power Plant Attack Surface Map

This map is generic and uses public architectural knowledge plus well-known documented incidents. It does not imply the configuration, vulnerabilities, vendors, network paths, or weaknesses of any specific facility.

## IT Layer: Corporate and Business Systems

| Component | Role | Threat Vectors | Notable Gaps |
|---|---|---|---|
| Enterprise identity and access management | Authenticates corporate users and supports role-based access | Phishing, credential theft, password reuse, MFA fatigue, privileged account misuse | Public information does not reveal account tiers, privileged-access workflows, or actual federation boundaries |
| Email and collaboration platforms | Routine business communication, document exchange, scheduling | Phishing, malicious attachments, business email compromise, social engineering | Cannot infer filtering rules, user training quality, or incident reporting behavior |
| Corporate network and workstations | General business computing environment | Malware, drive-by compromise, stolen laptops, vulnerable applications | Actual endpoint controls, patch latency, asset inventory quality, and segmentation are facility-specific |
| Engineering document repositories | Stores procedures, diagrams, design packages, and change documentation | Unauthorized access, sensitive information leakage, tampering with reference material | Public sources do not show document sensitivity markings, access control groups, or review workflows |
| Vendor and contractor portals | Supports maintenance, procurement, and external coordination | Compromised vendor credentials, malicious uploads, supplier impersonation | Vendor population, remote-access controls, and contract security requirements are not public |
| Backup and recovery infrastructure | Restores business systems after failure or attack | Ransomware targeting backups, credential compromise, deletion or encryption of recovery data | Backup isolation, recovery time objectives, and test frequency cannot be known externally |

Layer summary: The corporate IT layer is usually the most exposed to commodity attack paths because it touches email, internet services, contractors, and business applications. Its main risk to nuclear cybersecurity is not that it directly controls safety systems, but that compromise can provide credentials, documents, social-engineering context, or staging infrastructure for attempts to move toward protected plant functions.

## OT Layer: Operational Technology and Plant Digital Systems

| Component | Role | Threat Vectors | Notable Gaps |
|---|---|---|---|
| Plant process monitoring systems | Provides operators and engineers with plant status and process data | Malware on supporting Windows hosts, compromised data paths, loss of display availability | Public information does not reveal specific architectures, isolation mechanisms, or failover designs |
| Digital control systems and PLCs | Automates or assists control of plant processes and balance-of-plant equipment | Unauthorized logic changes, engineering workstation compromise, malicious firmware or configuration changes | Actual PLC models, logic, maintenance paths, and safety significance are facility-specific |
| Safety-related digital systems and CDAs | Supports safety, security, or emergency preparedness functions where classified as CDAs | Insider misuse, configuration drift, weak maintenance controls, supply-chain compromise | CDA determinations are licensee-specific and not visible from generic public sources |
| Engineering workstations | Configures, tests, and maintains OT devices | Malware, unauthorized project file changes, compromised removable media, misuse of engineering privileges | Public data rarely shows workstation hardening, access control, or media transfer procedure quality |
| Historian and data gateways | Transfers plant data for trending, analysis, and reporting | One-way path failure, misconfigured firewall rules, compromised intermediate servers | Directionality, filtering, and security level boundaries are not knowable without plant documentation |
| Patch and configuration management processes | Maintains approved baselines and evaluates changes | Delayed remediation, untested updates, undocumented exceptions, inconsistent baselines | The real risk depends on asset age, vendor support, testing facilities, and outage schedules |

Layer summary: The OT layer contains the highest-consequence digital assets, but public information cannot support claims about a specific plant's control network. The recurring generic concern is the pathway from engineering and maintenance activity into systems that are otherwise isolated or tightly controlled.

## Physical/Cyber Intersection

| Component | Role | Threat Vectors | Notable Gaps |
|---|---|---|---|
| Physical access control systems | Controls access to protected areas, vital areas, and equipment rooms | Badge misuse, tailgating, insider manipulation, access-control system compromise | Physical layout, zone definitions, access logs, and alarm response procedures are protected details |
| Security monitoring and alarm systems | Supports detection and response for physical intrusion or abnormal conditions | Sensor tampering, alarm flooding, loss of monitoring availability, insider suppression | Public sources cannot reveal sensor coverage, guard-force procedures, or backup monitoring paths |
| Removable media control points | Enables controlled transfer of software, updates, logs, and files | Infected USB media, unauthorized file movement, weak scanning process | Actual media kiosks, scanning tools, exception procedures, and enforcement culture are site-specific |
| Vendor maintenance activity | Provides specialized support for installed systems | Trusted-access abuse, compromised tools, temporary network connections, unmanaged laptops | Vendor lists, visit schedules, tooling, supervision, and cleanup practices are not public |
| Emergency preparedness communications | Supports event notification, coordination, and response | Availability attacks, account compromise, false or delayed notifications | Real communications paths, backup channels, and dependencies are facility-specific |
| Insider work processes | Human operation of procedures, overrides, maintenance, and approvals | Authority pressure, shared credentials, procedural shortcuts, coerced or disgruntled insiders | Insider-risk indicators and cultural factors cannot be inferred from architecture alone |

Layer summary: The physical/cyber intersection is where Anderson's human and economic observations matter most. Nuclear plants can have strong technical separation, but authorized people, maintenance tools, physical access, and emergency workflows still create paths that an adversary may try to exploit.

## Documented Incident Flags

- Documented incident: the 2003 Slammer worm infection at Davis-Besse is commonly cited as an example of malware affecting a nuclear plant network and causing loss of a safety-parameter display function for several hours. This supports treating business and support networks as relevant even when they are not supposed to control safety equipment.

- Documented incident: Stuxnet demonstrated that malware can target industrial control systems through Windows hosts, engineering software, removable media, PLC logic, and deceptive process feedback. It was not a US commercial nuclear power plant incident, so it should be used as a control-system attack pattern, not as evidence about any US plant's specific exposure.

- General architectural knowledge: segmentation, CDA programs, defense in depth, physical access control, media control, and compensating controls are drawn from the public regulatory and industry guidance summarized in the prompt, not from a facility-specific assessment.

## What This Map Cannot Tell You

- Actual CDA boundaries: CDA determinations are made by the licensee for its own systems and reviewed through the regulatory process. Without those determinations, a generic map cannot say which digital assets are legally and operationally in scope.

- Network topology and data-flow direction: converting this map into a real assessment requires diagrams, firewall rules, one-way device details, remote access paths, and trust relationships. Without those, the map cannot identify reachable attack paths.

- Installed vendors, models, and versions: exploitability depends on actual hardware, software, firmware, support status, and configuration. Public architectural categories are too broad to support vulnerability conclusions.

- Control implementation quality: policies such as media protection or configuration management only matter if they are enforced. A real assessment needs logs, procedures, interviews, walkdowns, and sampling evidence.

- Operational constraints: patching, scanning, and replacement options depend on plant mode, outage schedules, licensing basis, qualification status, and vendor support. Without those constraints, recommendations could create more operational risk than they reduce.

- Security culture and human behavior: phishing resilience, workaround frequency, insider-risk controls, and willingness to report anomalies cannot be read from architecture. They require observation, interviews, training records, and incident history.

- Consequence analysis: a generic map can identify possible surfaces, but it cannot determine safety, security, or emergency-preparedness consequence without plant-specific engineering analysis.
