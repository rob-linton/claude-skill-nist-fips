# NistControlCatalogue.md

> **Read [`SKILL.md`](../SKILL.md) §LEGAL NOTICE first.** This file is
> **generated** by `tools/build-data.py` from the NIST OSCAL SP 800-53
> Rev 5 catalogue ([upstream source](https://github.com/usnistgov/oscal-content)).
> Do not hand-edit — CI re-generates and diff-checks on every build. NIST
> OSCAL content is a U.S. Government work (public domain in the U.S.).
> NIST does not endorse this project.

**Catalog version**: 5.2.0
**OSCAL last-modified**: 2025-08-26T14:33:16.00000-00:00
**Built at**: 2026-04-20T01:29:36.667635+00:00
**Families included (v0.1 scope)**: AC, AU, IA, SC

The remaining 16 families (AT, CA, CM, CP, IR, MA, MP, PE, PL, PM, PS, PT,
RA, SA, SR) arrive in v0.2. Each family follows the same structure:
authoritative **OSCAL-sourced** statement + guidance, with a local
"implementation-hint" cross-reference to `data/implementation-hints.json`
(v0.2+).

---

## AC — Access Control

*23 base controls (enhancements listed per-control).*

### AC-1 — Policy and Procedures

**Statement (OSCAL)**

```
a. Develop, document, and disseminate to {{ insert: param, ac-1_prm_1 }}:
b. Designate an {{ insert: param, ac-01_odp.04 }} to manage the development, documentation, and dissemination of the access control policy and procedures; and
c. Review and update the current access control:
```

**Guidance (OSCAL)**

> Access control policy and procedures address the controls in the AC family that are implemented within systems and organizations. The risk management strategy is an important factor in establishing such policies and procedures. Policies and procedures contribute to security and privacy assurance. Therefore, it is important that security and privacy programs collaborate on the development of access control policy and procedures. Security and privacy program policies and procedures at the organization level are preferable, in general, and may obviate the need for mission- or system-specific policies and procedures. The policy can be included as part of the general security and privacy policy or be represented by multiple policies reflecting the complex nature of organizations. Procedures can be established for security and privacy programs, for mission or business processes, and for systems, if needed. Procedures describe how the policies or controls are implemented and can be directed at the individual or role that is the object of the procedure. Procedures can be documented in system security and privacy plans or in one or more separate documents. Events that may precipitate an update to access control policy and procedures include assessment or audit findings, security incidents or breaches, or changes in laws, executive orders, directives, regulations, policies, standards, and guidelines. Simply restating controls does not constitute an organizational policy or procedure.

**Organisation-defined parameters**

- `ac-1_prm_1` ()
- `ac-01_odp.01` (AC-01_ODP[01])
- `ac-01_odp.02` (AC-01_ODP[02])
- `ac-01_odp.03` (AC-01_ODP[03])
- `ac-01_odp.04` (AC-01_ODP[04])
- `ac-01_odp.05` (AC-01_ODP[05])
- `ac-01_odp.06` (AC-01_ODP[06])
- `ac-01_odp.07` (AC-01_ODP[07])
- `ac-01_odp.08` (AC-01_ODP[08])

**Related controls**: IA-1, PM-9, PM-24, PS-8, SI-12

### AC-2 — Account Management

**Statement (OSCAL)**

```
a. Define and document the types of accounts allowed and specifically prohibited for use within the system;
b. Assign account managers;
c. Require {{ insert: param, ac-02_odp.01 }} for group and role membership;
d. Specify:
e. Require approvals by {{ insert: param, ac-02_odp.03 }} for requests to create accounts;
f. Create, enable, modify, disable, and remove accounts in accordance with {{ insert: param, ac-02_odp.04 }};
g. Monitor the use of accounts;
h. Notify account managers and {{ insert: param, ac-02_odp.05 }} within:
i. Authorize access to the system based on:
j. Review accounts for compliance with account management requirements {{ insert: param, ac-02_odp.10 }};
k. Establish and implement a process for changing shared or group account authenticators (if deployed) when individuals are removed from the group; and
l. Align account management processes with personnel termination and transfer processes.
```

**Guidance (OSCAL)**

> Examples of system account types include individual, shared, group, system, guest, anonymous, emergency, developer, temporary, and service. Identification of authorized system users and the specification of access privileges reflect the requirements in other controls in the security plan. Users requiring administrative privileges on system accounts receive additional scrutiny by organizational personnel responsible for approving such accounts and privileged access, including system owner, mission or business owner, senior agency information security officer, or senior agency official for privacy. Types of accounts that organizations may wish to prohibit due to increased risk include shared, group, emergency, anonymous, temporary, and guest accounts.

> Where access involves personally identifiable information, security programs collaborate with the senior agency official for privacy to establish the specific conditions for group and role membership; specify authorized users, group and role membership, and access authorizations for each account; and create, adjust, or remove system accounts in accordance with organizational policies. Policies can include such information as account expiration dates or other factors that trigger the disabling of accounts. Organizations may choose to define access privileges or other attributes by account, type of account, or a combination of the two. Examples of other attributes required for authorizing access include restrictions on time of day, day of week, and point of origin. In defining other system account attributes, organizations consider system-related requirements and mission/business requirements. Failure to consider these factors could affect system availability.

> Temporary and emergency accounts are intended for short-term use. Organizations establish temporary accounts as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation. Organizations establish emergency accounts in response to crisis situations and with the need for rapid account activation. Therefore, emergency account activation may bypass normal account authorization processes. Emergency and temporary accounts are not to be confused with infrequently used accounts, including local logon accounts used for special tasks or when network resources are unavailable (may also be known as accounts of last resort). Such accounts remain available and are not subject to automatic disabling or removal dates. Conditions for disabling or deactivating accounts include when shared/group, emergency, or temporary accounts are no longer required and when individuals are transferred or terminated. Changing shared/group authenticators when members leave the group is intended to ensure that former group members do not retain access to the shared or group account. Some types of system accounts may require specialized training.

**Organisation-defined parameters**

- `ac-02_odp.01` (AC-02_ODP[01])
- `ac-02_odp.02` (AC-02_ODP[02])
- `ac-02_odp.03` (AC-02_ODP[03])
- `ac-02_odp.04` (AC-02_ODP[04])
- `ac-02_odp.05` (AC-02_ODP[05])
- `ac-02_odp.06` (AC-02_ODP[06])
- `ac-02_odp.07` (AC-02_ODP[07])
- `ac-02_odp.08` (AC-02_ODP[08])
- `ac-02_odp.09` (AC-02_ODP[09])
- `ac-02_odp.10` (AC-02_ODP[10])

**Related controls**: AC-3, AC-5, AC-6, AC-17, AC-18, AC-20, AC-24, AU-2, AU-12, CM-5, IA-2, IA-4, IA-5, IA-8, MA-3, MA-5, PE-2, PL-4, PS-2, PS-4, PS-5, PS-7, PT-2, PT-3, SC-7, SC-12, SC-13, SC-37

**Enhancements** (13):

- **AC-2.1** — Automated System Account Management
- **AC-2.2** — Automated Temporary and Emergency Account Management
- **AC-2.3** — Disable Accounts
- **AC-2.4** — Automated Audit Actions
- **AC-2.5** — Inactivity Logout
- **AC-2.6** — Dynamic Privilege Management
- **AC-2.7** — Privileged User Accounts
- **AC-2.8** — Dynamic Account Management
- **AC-2.9** — Restrictions on Use of Shared and Group Accounts
- **AC-2.10** — Shared and Group Account Credential Change
- **AC-2.11** — Usage Conditions
- **AC-2.12** — Account Monitoring for Atypical Usage
- **AC-2.13** — Disable Accounts for High-risk Individuals

### AC-3 — Access Enforcement

**Statement (OSCAL)**

```
Enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.
```

**Guidance (OSCAL)**

> Access control policies control access between active entities or subjects (i.e., users or processes acting on behalf of users) and passive entities or objects (i.e., devices, files, records, domains) in organizational systems. In addition to enforcing authorized access at the system level and recognizing that systems can host many applications and services in support of mission and business functions, access enforcement mechanisms can also be employed at the application and service level to provide increased information security and privacy. In contrast to logical access controls that are implemented within the system, physical access controls are addressed by the controls in the Physical and Environmental Protection ( [PE](#pe) ) family.

**Related controls**: AC-2, AC-4, AC-5, AC-6, AC-16, AC-17, AC-18, AC-19, AC-20, AC-21, AC-22, AC-24, AC-25, AT-2, AT-3, AU-9, CA-9, CM-5, CM-11, IA-2, IA-5, IA-6, IA-7, IA-11, IA-13, MA-3, MA-4, MA-5, MP-4, PM-2, PS-3, PT-2, PT-3, SA-17, SC-2, SC-3, SC-4, SC-12, SC-13, SC-28, SC-31, SC-34, SI-4, SI-8

**Enhancements** (15):

- **AC-3.1** — Restricted Access to Privileged Functions
- **AC-3.2** — Dual Authorization
- **AC-3.3** — Mandatory Access Control
- **AC-3.4** — Discretionary Access Control
- **AC-3.5** — Security-relevant Information
- **AC-3.6** — Protection of User and System Information
- **AC-3.7** — Role-based Access Control
- **AC-3.8** — Revocation of Access Authorizations
- **AC-3.9** — Controlled Release
- **AC-3.10** — Audited Override of Access Control Mechanisms
- **AC-3.11** — Restrict Access to Specific Information Types
- **AC-3.12** — Assert and Enforce Application Access
- **AC-3.13** — Attribute-based Access Control
- **AC-3.14** — Individual Access
- **AC-3.15** — Discretionary and Mandatory Access Control

### AC-4 — Information Flow Enforcement

**Statement (OSCAL)**

```
Enforce approved authorizations for controlling the flow of information within the system and between connected systems based on {{ insert: param, ac-04_odp }}.
```

**Guidance (OSCAL)**

> Information flow control regulates where information can travel within a system and between systems (in contrast to who is allowed to access the information) and without regard to subsequent accesses to that information. Flow control restrictions include blocking external traffic that claims to be from within the organization, keeping export-controlled information from being transmitted in the clear to the Internet, restricting web requests that are not from the internal web proxy server, and limiting information transfers between organizations based on data structures and content. Transferring information between organizations may require an agreement specifying how the information flow is enforced (see [CA-3](#ca-3) ). Transferring information between systems in different security or privacy domains with different security or privacy policies introduces the risk that such transfers violate one or more domain security or privacy policies. In such situations, information owners/stewards provide guidance at designated policy enforcement points between connected systems. Organizations consider mandating specific architectural solutions to enforce specific security and privacy policies. Enforcement includes prohibiting information transfers between connected systems (i.e., allowing access only), verifying write permissions before accepting information from another security or privacy domain or connected system, employing hardware mechanisms to enforce one-way information flows, and implementing trustworthy regrading mechanisms to reassign security or privacy attributes and labels.

> Organizations commonly employ information flow control policies and enforcement mechanisms to control the flow of information between designated sources and destinations within systems and between connected systems. Flow control is based on the characteristics of the information and/or the information path. Enforcement occurs, for example, in boundary protection devices that employ rule sets or establish configuration settings that restrict system services, provide a packet-filtering capability based on header information, or provide a message-filtering capability based on message content. Organizations also consider the trustworthiness of filtering and/or inspection mechanisms (i.e., hardware, firmware, and software components) that are critical to information flow enforcement. Control enhancements 3 through 32 primarily address cross-domain solution needs that focus on more advanced filtering techniques, in-depth analysis, and stronger flow enforcement mechanisms implemented in cross-domain products, such as high-assurance guards. Such capabilities are generally not available in commercial off-the-shelf products. Information flow enforcement also applies to control plane traffic (e.g., routing and DNS).

**Organisation-defined parameters**

- `ac-04_odp` (AC-04_ODP)

**Related controls**: AC-3, AC-6, AC-16, AC-17, AC-19, AC-21, AU-10, CA-3, CA-9, CM-7, PL-9, PM-24, SA-17, SC-4, SC-7, SC-16, SC-31

**Enhancements** (32):

- **AC-4.1** — Object Security and Privacy Attributes
- **AC-4.2** — Processing Domains
- **AC-4.3** — Dynamic Information Flow Control
- **AC-4.4** — Flow Control of Encrypted Information
- **AC-4.5** — Embedded Data Types
- **AC-4.6** — Metadata
- **AC-4.7** — One-way Flow Mechanisms
- **AC-4.8** — Security and Privacy Policy Filters
- **AC-4.9** — Human Reviews
- **AC-4.10** — Enable and Disable Security or Privacy Policy Filters
- **AC-4.11** — Configuration of Security or Privacy Policy Filters
- **AC-4.12** — Data Type Identifiers
- **AC-4.13** — Decomposition into Policy-relevant Subcomponents
- **AC-4.14** — Security or Privacy Policy Filter Constraints
- **AC-4.15** — Detection of Unsanctioned Information
- **AC-4.16** — Information Transfers on Interconnected Systems
- **AC-4.17** — Domain Authentication
- **AC-4.18** — Security Attribute Binding
- **AC-4.19** — Validation of Metadata
- **AC-4.20** — Approved Solutions
- **AC-4.21** — Physical or Logical Separation of Information Flows
- **AC-4.22** — Access Only
- **AC-4.23** — Modify Non-releasable Information
- **AC-4.24** — Internal Normalized Format
- **AC-4.25** — Data Sanitization
- **AC-4.26** — Audit Filtering Actions
- **AC-4.27** — Redundant/Independent Filtering Mechanisms
- **AC-4.28** — Linear Filter Pipelines
- **AC-4.29** — Filter Orchestration Engines
- **AC-4.30** — Filter Mechanisms Using Multiple Processes
- **AC-4.31** — Failed Content Transfer Prevention
- **AC-4.32** — Process Requirements for Information Transfer

### AC-5 — Separation of Duties

**Statement (OSCAL)**

```
a. Identify and document {{ insert: param, ac-05_odp }} ; and
b. Define system access authorizations to support separation of duties.
```

**Guidance (OSCAL)**

> Separation of duties addresses the potential for abuse of authorized privileges and helps to reduce the risk of malevolent activity without collusion. Separation of duties includes dividing mission or business functions and support functions among different individuals or roles, conducting system support functions with different individuals, and ensuring that security personnel who administer access control functions do not also administer audit functions. Because separation of duty violations can span systems and application domains, organizations consider the entirety of systems and system components when developing policy on separation of duties. Separation of duties is enforced through the account management activities in [AC-2](#ac-2) , access control mechanisms in [AC-3](#ac-3) , and identity management activities in [IA-2](#ia-2), [IA-4](#ia-4) , and [IA-12](#ia-12).

**Organisation-defined parameters**

- `ac-05_odp` (AC-05_ODP)

**Related controls**: AC-2, AC-3, AC-6, AU-9, CM-5, CM-11, CP-9, IA-2, IA-4, IA-5, IA-12, MA-3, MA-5, PS-2, SA-8, SA-17

### AC-6 — Least Privilege

**Statement (OSCAL)**

```
Employ the principle of least privilege, allowing only authorized accesses for users (or processes acting on behalf of users) that are necessary to accomplish assigned organizational tasks.
```

**Guidance (OSCAL)**

> Organizations employ least privilege for specific duties and systems. The principle of least privilege is also applied to system processes, ensuring that the processes have access to systems and operate at privilege levels no higher than necessary to accomplish organizational missions or business functions. Organizations consider the creation of additional processes, roles, and accounts as necessary to achieve least privilege. Organizations apply least privilege to the development, implementation, and operation of organizational systems.

**Related controls**: AC-2, AC-3, AC-5, AC-16, CM-5, CM-11, PL-2, PM-12, SA-8, SA-15, SA-17, SC-38

**Enhancements** (10):

- **AC-6.1** — Authorize Access to Security Functions
- **AC-6.2** — Non-privileged Access for Nonsecurity Functions
- **AC-6.3** — Network Access to Privileged Commands
- **AC-6.4** — Separate Processing Domains
- **AC-6.5** — Privileged Accounts
- **AC-6.6** — Privileged Access by Non-organizational Users
- **AC-6.7** — Review of User Privileges
- **AC-6.8** — Privilege Levels for Code Execution
- **AC-6.9** — Log Use of Privileged Functions
- **AC-6.10** — Prohibit Non-privileged Users from Executing Privileged Functions

### AC-7 — Unsuccessful Logon Attempts

**Statement (OSCAL)**

```
a. Enforce a limit of {{ insert: param, ac-07_odp.01 }} consecutive invalid logon attempts by a user during a {{ insert: param, ac-07_odp.02 }} ; and
b. Automatically {{ insert: param, ac-07_odp.03 }} when the maximum number of unsuccessful attempts is exceeded.
```

**Guidance (OSCAL)**

> The need to limit unsuccessful logon attempts and take subsequent action when the maximum number of attempts is exceeded applies regardless of whether the logon occurs via a local or network connection. Due to the potential for denial of service, automatic lockouts initiated by systems are usually temporary and automatically release after a predetermined, organization-defined time period. If a delay algorithm is selected, organizations may employ different algorithms for different components of the system based on the capabilities of those components. Responses to unsuccessful logon attempts may be implemented at the operating system and the application levels. Organization-defined actions that may be taken when the number of allowed consecutive invalid logon attempts is exceeded include prompting the user to answer a secret question in addition to the username and password, invoking a lockdown mode with limited user capabilities (instead of full lockout), allowing users to only logon from specified Internet Protocol (IP) addresses, requiring a CAPTCHA to prevent automated attacks, or applying user profiles such as location, time of day, IP address, device, or Media Access Control (MAC) address. If automatic system lockout or execution of a delay algorithm is not implemented in support of the availability objective, organizations consider a combination of other actions to help prevent brute force attacks. In addition to the above, organizations can prompt users to respond to a secret question before the number of allowed unsuccessful logon attempts is exceeded. Automatically unlocking an account after a specified period of time is generally not permitted. However, exceptions may be required based on operational mission or need.

**Organisation-defined parameters**

- `ac-07_odp.01` (AC-07_ODP[01])
- `ac-07_odp.02` (AC-07_ODP[02])
- `ac-07_odp.03` (AC-07_ODP[03])
- `ac-07_odp.04` (AC-07_ODP[04])
- `ac-07_odp.05` (AC-07_ODP[05])
- `ac-07_odp.06` (AC-07_ODP[06])

**Related controls**: AC-2, AC-9, AU-2, AU-6, IA-5

**Enhancements** (4):

- **AC-7.1** — Automatic Account Lock
- **AC-7.2** — Purge or Wipe Mobile Device
- **AC-7.3** — Biometric Attempt Limiting
- **AC-7.4** — Use of Alternate Authentication Factor

### AC-8 — System Use Notification

**Statement (OSCAL)**

```
a. Display {{ insert: param, ac-08_odp.01 }} to users before granting access to the system that provides privacy and security notices consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines and state that:
b. Retain the notification message or banner on the screen until users acknowledge the usage conditions and take explicit actions to log on to or further access the system; and
c. For publicly accessible systems:
```

**Guidance (OSCAL)**

> System use notifications can be implemented using messages or warning banners displayed before individuals log in to systems. System use notifications are used only for access via logon interfaces with human users. Notifications are not required when human interfaces do not exist. Based on an assessment of risk, organizations consider whether or not a secondary system use notification is needed to access applications or other system resources after the initial network logon. Organizations consider system use notification messages or banners displayed in multiple languages based on organizational needs and the demographics of system users. Organizations consult with the privacy office for input regarding privacy messaging and the Office of the General Counsel or organizational equivalent for legal review and approval of warning banner content.

**Organisation-defined parameters**

- `ac-08_odp.01` (AC-08_ODP[01])
- `ac-08_odp.02` (AC-08_ODP[02])

**Related controls**: AC-14, PL-4, SI-4

### AC-9 — Previous Logon Notification

**Statement (OSCAL)**

```
Notify the user, upon successful logon to the system, of the date and time of the last logon.
```

**Guidance (OSCAL)**

> Previous logon notification is applicable to system access via human user interfaces and access to systems that occurs in other types of architectures. Information about the last successful logon allows the user to recognize if the date and time provided is not consistent with the user’s last access.

**Related controls**: AC-7, PL-4

**Enhancements** (4):

- **AC-9.1** — Unsuccessful Logons
- **AC-9.2** — Successful and Unsuccessful Logons
- **AC-9.3** — Notification of Account Changes
- **AC-9.4** — Additional Logon Information

### AC-10 — Concurrent Session Control

**Statement (OSCAL)**

```
Limit the number of concurrent sessions for each {{ insert: param, ac-10_odp.01 }} to {{ insert: param, ac-10_odp.02 }}.
```

**Guidance (OSCAL)**

> Organizations may define the maximum number of concurrent sessions for system accounts globally, by account type, by account, or any combination thereof. For example, organizations may limit the number of concurrent sessions for system administrators or other individuals working in particularly sensitive domains or mission-critical applications. Concurrent session control addresses concurrent sessions for system accounts. It does not, however, address concurrent sessions by single users via multiple system accounts.

**Organisation-defined parameters**

- `ac-10_odp.01` (AC-10_ODP[01])
- `ac-10_odp.02` (AC-10_ODP[02])

**Related controls**: SC-23

### AC-11 — Device Lock

**Statement (OSCAL)**

```
a. Prevent further access to the system by {{ insert: param, ac-11_odp.01 }} ; and
b. Retain the device lock until the user reestablishes access using established identification and authentication procedures.
```

**Guidance (OSCAL)**

> Device locks are temporary actions taken to prevent logical access to organizational systems when users stop work and move away from the immediate vicinity of those systems but do not want to log out because of the temporary nature of their absences. Device locks can be implemented at the operating system level or at the application level. A proximity lock may be used to initiate the device lock (e.g., via a Bluetooth-enabled device or dongle). User-initiated device locking is behavior or policy-based and, as such, requires users to take physical action to initiate the device lock. Device locks are not an acceptable substitute for logging out of systems, such as when organizations require users to log out at the end of workdays.

**Organisation-defined parameters**

- `ac-11_odp.01` (AC-11_ODP[01])
- `ac-11_odp.02` (AC-11_ODP[02])

**Related controls**: AC-2, AC-7, IA-11, PL-4

**Enhancements** (1):

- **AC-11.1** — Pattern-hiding Displays

### AC-12 — Session Termination

**Statement (OSCAL)**

```
Automatically terminate a user session after {{ insert: param, ac-12_odp }}.
```

**Guidance (OSCAL)**

> Session termination addresses the termination of user-initiated logical sessions (in contrast to [SC-10](#sc-10) , which addresses the termination of network connections associated with communications sessions (i.e., network disconnect)). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational system. Such user sessions can be terminated without terminating network sessions. Session termination ends all processes associated with a user’s logical session except for those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events that require automatic termination of the session include organization-defined periods of user inactivity, targeted responses to certain types of incidents, or time-of-day restrictions on system use.

**Organisation-defined parameters**

- `ac-12_odp` (AC-12_ODP)

**Related controls**: MA-4, SC-10, SC-23

**Enhancements** (3):

- **AC-12.1** — User-initiated Logouts
- **AC-12.2** — Termination Message
- **AC-12.3** — Timeout Warning Message

### AC-14 — Permitted Actions Without Identification or Authentication

**Statement (OSCAL)**

```
a. Identify {{ insert: param, ac-14_odp }} that can be performed on the system without identification or authentication consistent with organizational mission and business functions; and
b. Document and provide supporting rationale in the security plan for the system, user actions not requiring identification or authentication.
```

**Guidance (OSCAL)**

> Specific user actions may be permitted without identification or authentication if organizations determine that identification and authentication are not required for the specified user actions. Organizations may allow a limited number of user actions without identification or authentication, including when individuals access public websites or other publicly accessible federal systems, when individuals use mobile phones to receive calls, or when facsimiles are received. Organizations identify actions that normally require identification or authentication but may, under certain circumstances, allow identification or authentication mechanisms to be bypassed. Such bypasses may occur, for example, via a software-readable physical switch that commands bypass of the logon functionality and is protected from accidental or unmonitored use. Permitting actions without identification or authentication does not apply to situations where identification and authentication have already occurred and are not repeated but rather to situations where identification and authentication have not yet occurred. Organizations may decide that there are no user actions that can be performed on organizational systems without identification and authentication, and therefore, the value for the assignment operation can be "none."

**Organisation-defined parameters**

- `ac-14_odp` (AC-14_ODP)

**Related controls**: AC-8, IA-2, PL-2

**Enhancements** (1):

- **AC-14.1** — Necessary Uses

### AC-16 — Security and Privacy Attributes

**Statement (OSCAL)**

```
a. Provide the means to associate {{ insert: param, ac-16_prm_1 }} with {{ insert: param, ac-16_prm_2 }} for information in storage, in process, and/or in transmission;
b. Ensure that the attribute associations are made and retained with the information;
c. Establish the following permitted security and privacy attributes from the attributes defined in [AC-16a](#ac-16_smt.a) for {{ insert: param, ac-16_prm_3 }}: {{ insert: param, ac-16_prm_4 }};
d. Determine the following permitted attribute values or ranges for each of the established attributes: {{ insert: param, ac-16_odp.09 }};
e. Audit changes to attributes; and
f. Review {{ insert: param, ac-16_prm_6 }} for applicability {{ insert: param, ac-16_prm_7 }}.
```

**Guidance (OSCAL)**

> Information is represented internally within systems using abstractions known as data structures. Internal data structures can represent different types of entities, both active and passive. Active entities, also known as subjects, are typically associated with individuals, devices, or processes acting on behalf of individuals. Passive entities, also known as objects, are typically associated with data structures, such as records, buffers, tables, files, inter-process pipes, and communications ports. Security attributes, a form of metadata, are abstractions that represent the basic properties or characteristics of active and passive entities with respect to safeguarding information. Privacy attributes, which may be used independently or in conjunction with security attributes, represent the basic properties or characteristics of active or passive entities with respect to the management of personally identifiable information. Attributes can be either explicitly or implicitly associated with the information contained in organizational systems or system components.

> Attributes may be associated with active entities (i.e., subjects) that have the potential to send or receive information, cause information to flow among objects, or change the system state. These attributes may also be associated with passive entities (i.e., objects) that contain or receive information. The association of attributes to subjects and objects by a system is referred to as binding and is inclusive of setting the attribute value and the attribute type. Attributes, when bound to data or information, permit the enforcement of security and privacy policies for access control and information flow control, including data retention limits, permitted uses of personally identifiable information, and identification of personal information within data objects. Such enforcement occurs through organizational processes or system functions or mechanisms. The binding techniques implemented by systems affect the strength of attribute binding to information. Binding strength and the assurance associated with binding techniques play important parts in the trust that organizations have in the information flow enforcement process. The binding techniques affect the number and degree of additional reviews required by organizations. The content or assigned values of attributes can directly affect the ability of individuals to access organizational information.

> Organizations can define the types of attributes needed for systems to support missions or business functions. There are many values that can be assigned to a security attribute. By specifying the permitted attribute ranges and values, organizations ensure that attribute values are meaningful and relevant. Labeling refers to the association of attributes with the subjects and objects represented by the internal data structures within systems. This facilitates system-based enforcement of information security and privacy policies. Labels include classification of information in accordance with legal and compliance requirements (e.g., top secret, secret, confidential, controlled unclassified), information impact level; high value asset information, access authorizations, nationality; data life cycle protection (i.e., encryption and data expiration), personally identifiable information processing permissions, including individual consent to personally identifiable information processing, and contractor affiliation. A related term to labeling is marking. Marking refers to the association of attributes with objects in a human-readable form and displayed on system media. Marking enables manual, procedural, or process-based enforcement of information security and privacy policies. Security and privacy labels may have the same value as media markings (e.g., top secret, secret, confidential). See [MP-3](#mp-3) (Media Marking).

**Organisation-defined parameters**

- `ac-16_prm_1` ()
- `ac-16_prm_2` ()
- `ac-16_prm_3` ()
- `ac-16_prm_4` ()
- `ac-16_prm_6` ()
- `ac-16_prm_7` ()
- `ac-16_odp.01` (AC-16_ODP[01])
- `ac-16_odp.02` (AC-16_ODP[02])
- `ac-16_odp.03` (AC-16_ODP[03])
- `ac-16_odp.04` (AC-16_ODP[04])
- `ac-16_odp.05` (AC-16_ODP[05])
- `ac-16_odp.06` (AC-16_ODP[06])
- `ac-16_odp.07` (AC-16_ODP[07])
- `ac-16_odp.08` (AC-16_ODP[08])
- `ac-16_odp.09` (AC-16_ODP[09])
- `ac-16_odp.10` (AC-16_ODP[10])
- `ac-16_odp.11` (AC-16_ODP[11])

**Related controls**: AC-3, AC-4, AC-6, AC-21, AC-25, AU-2, AU-10, MP-3, PE-22, PT-2, PT-3, PT-4, SC-11, SC-16, SI-12, SI-18

**Enhancements** (10):

- **AC-16.1** — Dynamic Attribute Association
- **AC-16.2** — Attribute Value Changes by Authorized Individuals
- **AC-16.3** — Maintenance of Attribute Associations by System
- **AC-16.4** — Association of Attributes by Authorized Individuals
- **AC-16.5** — Attribute Displays on Objects to Be Output
- **AC-16.6** — Maintenance of Attribute Association
- **AC-16.7** — Consistent Attribute Interpretation
- **AC-16.8** — Association Techniques and Technologies
- **AC-16.9** — Attribute Reassignment — Regrading Mechanisms
- **AC-16.10** — Attribute Configuration by Authorized Individuals

### AC-17 — Remote Access

**Statement (OSCAL)**

```
a. Establish and document usage restrictions, configuration/connection requirements, and implementation guidance for each type of remote access allowed; and
b. Authorize each type of remote access to the system prior to allowing such connections.
```

**Guidance (OSCAL)**

> Remote access is access to organizational systems (or processes acting on behalf of users) that communicate through external networks such as the Internet. Types of remote access include dial-up, broadband, and wireless. Organizations use encrypted virtual private networks (VPNs) to enhance confidentiality and integrity for remote connections. The use of encrypted VPNs provides sufficient assurance to the organization that it can effectively treat such connections as internal networks if the cryptographic mechanisms used are implemented in accordance with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines. Still, VPN connections traverse external networks, and the encrypted VPN does not enhance the availability of remote connections. VPNs with encrypted tunnels can also affect the ability to adequately monitor network communications traffic for malicious code. Remote access controls apply to systems other than public web servers or systems designed for public access. Authorization of each remote access type addresses authorization prior to allowing remote access without specifying the specific formats for such authorization. While organizations may use information exchange and system connection security agreements to manage remote access connections to other systems, such agreements are addressed as part of [CA-3](#ca-3) . Enforcing access restrictions for remote access is addressed via [AC-3](#ac-3).

**Related controls**: AC-2, AC-3, AC-4, AC-18, AC-19, AC-20, CA-3, CM-10, IA-2, IA-3, IA-8, MA-4, PE-17, PL-2, PL-4, SC-10, SC-12, SC-13, SI-4

**Enhancements** (10):

- **AC-17.1** — Monitoring and Control
- **AC-17.2** — Protection of Confidentiality and Integrity Using Encryption
- **AC-17.3** — Managed Access Control Points
- **AC-17.4** — Privileged Commands and Access
- **AC-17.5** — Monitoring for Unauthorized Connections
- **AC-17.6** — Protection of Mechanism Information
- **AC-17.7** — Additional Protection for Security Function Access
- **AC-17.8** — Disable Nonsecure Network Protocols
- **AC-17.9** — Disconnect or Disable Access
- **AC-17.10** — Authenticate Remote Commands

### AC-18 — Wireless Access

**Statement (OSCAL)**

```
a. Establish configuration requirements, connection requirements, and implementation guidance for each type of wireless access; and
b. Authorize each type of wireless access to the system prior to allowing such connections.
```

**Guidance (OSCAL)**

> Wireless technologies include microwave, packet radio (ultra-high frequency or very high frequency), 802.11x, and Bluetooth. Wireless networks use authentication protocols that provide authenticator protection and mutual authentication.

**Related controls**: AC-2, AC-3, AC-17, AC-19, CA-9, CM-7, IA-2, IA-3, IA-8, PL-4, SC-40, SC-43, SI-4

**Enhancements** (5):

- **AC-18.1** — Authentication and Encryption
- **AC-18.2** — Monitoring Unauthorized Connections
- **AC-18.3** — Disable Wireless Networking
- **AC-18.4** — Restrict Configurations by Users
- **AC-18.5** — Antennas and Transmission Power Levels

### AC-19 — Access Control for Mobile Devices

**Statement (OSCAL)**

```
a. Establish configuration requirements, connection requirements, and implementation guidance for organization-controlled mobile devices, to include when such devices are outside of controlled areas; and
b. Authorize the connection of mobile devices to organizational systems.
```

**Guidance (OSCAL)**

> A mobile device is a computing device that has a small form factor such that it can easily be carried by a single individual; is designed to operate without a physical connection; possesses local, non-removable or removable data storage; and includes a self-contained power source. Mobile device functionality may also include voice communication capabilities, on-board sensors that allow the device to capture information, and/or built-in features for synchronizing local data with remote locations. Examples include smart phones and tablets. Mobile devices are typically associated with a single individual. The processing, storage, and transmission capability of the mobile device may be comparable to or merely a subset of notebook/desktop systems, depending on the nature and intended purpose of the device. Protection and control of mobile devices is behavior or policy-based and requires users to take physical action to protect and control such devices when outside of controlled areas. Controlled areas are spaces for which organizations provide physical or procedural controls to meet the requirements established for protecting information and systems.

> Due to the large variety of mobile devices with different characteristics and capabilities, organizational restrictions may vary for the different classes or types of such devices. Usage restrictions and specific implementation guidance for mobile devices include configuration management, device identification and authentication, implementation of mandatory protective software, scanning devices for malicious code, updating virus protection software, scanning for critical software updates and patches, conducting primary operating system (and possibly other resident software) integrity checks, and disabling unnecessary hardware.

> Usage restrictions and authorization to connect may vary among organizational systems. For example, the organization may authorize the connection of mobile devices to its network and impose a set of usage restrictions, while a system owner may withhold authorization for mobile device connection to specific applications or impose additional usage restrictions before allowing mobile device connections to a system. Adequate security for mobile devices goes beyond the requirements specified in [AC-19](#ac-19) . Many safeguards for mobile devices are reflected in other controls. [AC-20](#ac-20) addresses mobile devices that are not organization-controlled.

**Related controls**: AC-3, AC-4, AC-7, AC-11, AC-17, AC-18, AC-20, CA-9, CM-2, CM-6, IA-2, IA-3, MP-2, MP-4, MP-5, MP-7, PL-4, SC-7, SC-34, SC-43, SI-3, SI-4

**Enhancements** (5):

- **AC-19.1** — Use of Writable and Portable Storage Devices
- **AC-19.2** — Use of Personally Owned Portable Storage Devices
- **AC-19.3** — Use of Portable Storage Devices with No Identifiable Owner
- **AC-19.4** — Restrictions for Classified Information
- **AC-19.5** — Full Device or Container-based Encryption

### AC-20 — Use of External Systems

**Statement (OSCAL)**

```
a. {{ insert: param, ac-20_odp.01 }} , consistent with the trust relationships established with other organizations owning, operating, and/or maintaining external systems, allowing authorized individuals to:
b. Prohibit the use of {{ insert: param, ac-20_odp.04 }}.
```

**Guidance (OSCAL)**

> External systems are systems that are used by but not part of organizational systems, and for which the organization has no direct control over the implementation of required controls or the assessment of control effectiveness. External systems include personally owned systems, components, or devices; privately owned computing and communications devices in commercial or public facilities; systems owned or controlled by nonfederal organizations; systems managed by contractors; and federal information systems that are not owned by, operated by, or under the direct supervision or authority of the organization. External systems also include systems owned or operated by other components within the same organization and systems within the organization with different authorization boundaries. Organizations have the option to prohibit the use of any type of external system or prohibit the use of specified types of external systems, (e.g., prohibit the use of any external system that is not organizationally owned or prohibit the use of personally-owned systems).

> For some external systems (i.e., systems operated by other organizations), the trust relationships that have been established between those organizations and the originating organization may be such that no explicit terms and conditions are required. Systems within these organizations may not be considered external. These situations occur when, for example, there are pre-existing information exchange agreements (either implicit or explicit) established between organizations or components or when such agreements are specified by applicable laws, executive orders, directives, regulations, policies, or standards. Authorized individuals include organizational personnel, contractors, or other individuals with authorized access to organizational systems and over which organizations have the authority to impose specific rules of behavior regarding system access. Restrictions that organizations impose on authorized individuals need not be uniform, as the restrictions may vary depending on trust relationships between organizations. Therefore, organizations may choose to impose different security restrictions on contractors than on state, local, or tribal governments.

> External systems used to access public interfaces to organizational systems are outside the scope of [AC-20](#ac-20) . Organizations establish specific terms and conditions for the use of external systems in accordance with organizational security policies and procedures. At a minimum, terms and conditions address the specific types of applications that can be accessed on organizational systems from external systems and the highest security category of information that can be processed, stored, or transmitted on external systems. If the terms and conditions with the owners of the external systems cannot be established, organizations may impose restrictions on organizational personnel using those external systems.

**Organisation-defined parameters**

- `ac-20_odp.01` (AC-20_ODP[01])
- `ac-20_odp.02` (AC-20_ODP[02])
- `ac-20_odp.03` (AC-20_ODP[03])
- `ac-20_odp.04` (AC-20_ODP[04])

**Related controls**: AC-2, AC-3, AC-17, AC-19, CA-3, PL-2, PL-4, SA-9, SC-7

**Enhancements** (5):

- **AC-20.1** — Limits on Authorized Use
- **AC-20.2** — Portable Storage Devices — Restricted Use
- **AC-20.3** — Non-organizationally Owned Systems — Restricted Use
- **AC-20.4** — Network Accessible Storage Devices — Prohibited Use
- **AC-20.5** — Portable Storage Devices — Prohibited Use

### AC-21 — Information Sharing

**Statement (OSCAL)**

```
a. Enable authorized users to determine whether access authorizations assigned to a sharing partner match the information’s access and use restrictions for {{ insert: param, ac-21_odp.01 }} ; and
b. Employ {{ insert: param, ac-21_odp.02 }} to assist users in making information sharing and collaboration decisions.
```

**Guidance (OSCAL)**

> Information sharing applies to information that may be restricted in some manner based on some formal or administrative determination. Examples of such information include, contract-sensitive information, classified information related to special access programs or compartments, privileged information, proprietary information, and personally identifiable information. Security and privacy risk assessments as well as applicable laws, regulations, and policies can provide useful inputs to these determinations. Depending on the circumstances, sharing partners may be defined at the individual, group, or organizational level. Information may be defined by content, type, security category, or special access program or compartment. Access restrictions may include non-disclosure agreements (NDA). Information flow techniques and security attributes may be used to provide automated assistance to users making sharing and collaboration decisions.

**Organisation-defined parameters**

- `ac-21_odp.01` (AC-21_ODP[01])
- `ac-21_odp.02` (AC-21_ODP[02])

**Related controls**: AC-3, AC-4, AC-16, PT-2, PT-7, RA-3, SC-15

**Enhancements** (2):

- **AC-21.1** — Automated Decision Support
- **AC-21.2** — Information Search and Retrieval

### AC-22 — Publicly Accessible Content

**Statement (OSCAL)**

```
a. Designate individuals authorized to make information publicly accessible;
b. Train authorized individuals to ensure that publicly accessible information does not contain nonpublic information;
c. Review the proposed content of information prior to posting onto the publicly accessible system to ensure that nonpublic information is not included; and
d. Review the content on the publicly accessible system for nonpublic information {{ insert: param, ac-22_odp }} and remove such information, if discovered.
```

**Guidance (OSCAL)**

> In accordance with applicable laws, executive orders, directives, policies, regulations, standards, and guidelines, the public is not authorized to have access to nonpublic information, including information protected under the [PRIVACT](#18e71fec-c6fd-475a-925a-5d8495cf8455) and proprietary information. Publicly accessible content addresses systems that are controlled by the organization and accessible to the public, typically without identification or authentication. Posting information on non-organizational systems (e.g., non-organizational public websites, forums, and social media) is covered by organizational policy. While organizations may have individuals who are responsible for developing and implementing policies about the information that can be made publicly accessible, publicly accessible content addresses the management of the individuals who make such information publicly accessible.

**Organisation-defined parameters**

- `ac-22_odp` (AC-22_ODP)

**Related controls**: AC-3, AT-2, AT-3, AU-13

### AC-23 — Data Mining Protection

**Statement (OSCAL)**

```
Employ {{ insert: param, ac-23_odp.01 }} for {{ insert: param, ac-23_odp.02 }} to detect and protect against unauthorized data mining.
```

**Guidance (OSCAL)**

> Data mining is an analytical process that attempts to find correlations or patterns in large data sets for the purpose of data or knowledge discovery. Data storage objects include database records and database fields. Sensitive information can be extracted from data mining operations. When information is personally identifiable information, it may lead to unanticipated revelations about individuals and give rise to privacy risks. Prior to performing data mining activities, organizations determine whether such activities are authorized. Organizations may be subject to applicable laws, executive orders, directives, regulations, or policies that address data mining requirements. Organizational personnel consult with the senior agency official for privacy and legal counsel regarding such requirements.

> Data mining prevention and detection techniques include limiting the number and frequency of database queries to increase the work factor needed to determine the contents of databases, limiting types of responses provided to database queries, applying differential privacy techniques or homomorphic encryption, and notifying personnel when atypical database queries or accesses occur. Data mining protection focuses on protecting information from data mining while such information resides in organizational data stores. In contrast, [AU-13](#au-13) focuses on monitoring for organizational information that may have been mined or otherwise obtained from data stores and is available as open-source information residing on external sites, such as social networking or social media websites.

> [EO 13587](#0af071a6-cf8e-48ee-8c82-fe91efa20f94) requires the establishment of an insider threat program for deterring, detecting, and mitigating insider threats, including the safeguarding of sensitive information from exploitation, compromise, or other unauthorized disclosure. Data mining protection requires organizations to identify appropriate techniques to prevent and detect unnecessary or unauthorized data mining. Data mining can be used by an insider to collect organizational information for the purpose of exfiltration.

**Organisation-defined parameters**

- `ac-23_odp.01` (AC-23_ODP[01])
- `ac-23_odp.02` (AC-23_ODP[02])

**Related controls**: PM-12, PT-2

### AC-24 — Access Control Decisions

**Statement (OSCAL)**

```
{{ insert: param, ac-24_odp.01 }} to ensure {{ insert: param, ac-24_odp.02 }} are applied to each access request prior to access enforcement.
```

**Guidance (OSCAL)**

> Access control decisions (also known as authorization decisions) occur when authorization information is applied to specific accesses. In contrast, access enforcement occurs when systems enforce access control decisions. While it is common to have access control decisions and access enforcement implemented by the same entity, it is not required, and it is not always an optimal implementation choice. For some architectures and distributed systems, different entities may make access control decisions and enforce access.

**Organisation-defined parameters**

- `ac-24_odp.01` (AC-24_ODP[01])
- `ac-24_odp.02` (AC-24_ODP[02])

**Related controls**: AC-2, AC-3

**Enhancements** (2):

- **AC-24.1** — Transmit Access Authorization Information
- **AC-24.2** — No User or Process Identity

### AC-25 — Reference Monitor

**Statement (OSCAL)**

```
Implement a reference monitor for {{ insert: param, ac-25_odp }} that is tamperproof, always invoked, and small enough to be subject to analysis and testing, the completeness of which can be assured.
```

**Guidance (OSCAL)**

> A reference monitor is a set of design requirements on a reference validation mechanism that, as a key component of an operating system, enforces an access control policy over all subjects and objects. A reference validation mechanism is always invoked, tamper-proof, and small enough to be subject to analysis and tests, the completeness of which can be assured (i.e., verifiable). Information is represented internally within systems using abstractions known as data structures. Internal data structures can represent different types of entities, both active and passive. Active entities, also known as subjects, are associated with individuals, devices, or processes acting on behalf of individuals. Passive entities, also known as objects, are associated with data structures, such as records, buffers, communications ports, tables, files, and inter-process pipes. Reference monitors enforce access control policies that restrict access to objects based on the identity of subjects or groups to which the subjects belong. The system enforces the access control policy based on the rule set established by the policy. The tamper-proof property of the reference monitor prevents determined adversaries from compromising the functioning of the reference validation mechanism. The always invoked property prevents adversaries from bypassing the mechanism and violating the security policy. The smallness property helps to ensure completeness in the analysis and testing of the mechanism to detect any weaknesses or deficiencies (i.e., latent flaws) that would prevent the enforcement of the security policy.

**Organisation-defined parameters**

- `ac-25_odp` (AC-25_ODP)

**Related controls**: AC-3, AC-16, SA-8, SA-17, SC-3, SC-11, SC-39, SI-13


---

## AU — Audit and Accountability

*15 base controls (enhancements listed per-control).*

### AU-1 — Policy and Procedures

**Statement (OSCAL)**

```
a. Develop, document, and disseminate to {{ insert: param, au-1_prm_1 }}:
b. Designate an {{ insert: param, au-01_odp.04 }} to manage the development, documentation, and dissemination of the audit and accountability policy and procedures; and
c. Review and update the current audit and accountability:
```

**Guidance (OSCAL)**

> Audit and accountability policy and procedures address the controls in the AU family that are implemented within systems and organizations. The risk management strategy is an important factor in establishing such policies and procedures. Policies and procedures contribute to security and privacy assurance. Therefore, it is important that security and privacy programs collaborate on the development of audit and accountability policy and procedures. Security and privacy program policies and procedures at the organization level are preferable, in general, and may obviate the need for mission- or system-specific policies and procedures. The policy can be included as part of the general security and privacy policy or be represented by multiple policies that reflect the complex nature of organizations. Procedures can be established for security and privacy programs, for mission or business processes, and for systems, if needed. Procedures describe how the policies or controls are implemented and can be directed at the individual or role that is the object of the procedure. Procedures can be documented in system security and privacy plans or in one or more separate documents. Events that may precipitate an update to audit and accountability policy and procedures include assessment or audit findings, security incidents or breaches, or changes in applicable laws, executive orders, directives, regulations, policies, standards, and guidelines. Simply restating controls does not constitute an organizational policy or procedure.

**Organisation-defined parameters**

- `au-1_prm_1` ()
- `au-01_odp.01` (AU-01_ODP[01])
- `au-01_odp.02` (AU-01_ODP[02])
- `au-01_odp.03` (AU-01_ODP[03])
- `au-01_odp.04` (AU-01_ODP[04])
- `au-01_odp.05` (AU-01_ODP[05])
- `au-01_odp.06` (AU-01_ODP[06])
- `au-01_odp.07` (AU-01_ODP[07])
- `au-01_odp.08` (AU-01_ODP[08])

**Related controls**: PM-9, PS-8, SI-12

### AU-2 — Event Logging

**Statement (OSCAL)**

```
a. Identify the types of events that the system is capable of logging in support of the audit function: {{ insert: param, au-02_odp.01 }};
b. Coordinate the event logging function with other organizational entities requiring audit-related information to guide and inform the selection criteria for events to be logged;
c. Specify the following event types for logging within the system: {{ insert: param, au-2_prm_2 }};
d. Provide a rationale for why the event types selected for logging are deemed to be adequate to support after-the-fact investigations of incidents; and
e. Review and update the event types selected for logging {{ insert: param, au-02_odp.04 }}.
```

**Guidance (OSCAL)**

> An event is an observable occurrence in a system. The types of events that require logging are those events that are significant and relevant to the security of systems and the privacy of individuals. Event logging also supports specific monitoring and auditing needs. Event types include password changes, failed logons or failed accesses related to systems, security or privacy attribute changes, administrative privilege usage, PIV credential usage, data action changes, query parameters, or external credential usage. In determining the set of event types that require logging, organizations consider the monitoring and auditing appropriate for each of the controls to be implemented. For completeness, event logging includes all protocols that are operational and supported by the system.

> To balance monitoring and auditing requirements with other system needs, event logging requires identifying the subset of event types that are logged at a given point in time. For example, organizations may determine that systems need the capability to log every file access successful and unsuccessful, but not activate that capability except for specific circumstances due to the potential burden on system performance. The types of events that organizations desire to be logged may change. Reviewing and updating the set of logged events is necessary to help ensure that the events remain relevant and continue to support the needs of the organization. Organizations consider how the types of logging events can reveal information about individuals that may give rise to privacy risk and how best to mitigate such risks. For example, there is the potential to reveal personally identifiable information in the audit trail, especially if the logging event is based on patterns or time of usage.

> Event logging requirements, including the need to log specific event types, may be referenced in other controls and control enhancements. These include [AC-2(4)](#ac-2.4), [AC-3(10)](#ac-3.10), [AC-6(9)](#ac-6.9), [AC-17(1)](#ac-17.1), [CM-3f](#cm-3_smt.f), [CM-5(1)](#cm-5.1), [IA-3(3)(b)](#ia-3.3_smt.b), [MA-4(1)](#ma-4.1), [MP-4(2)](#mp-4.2), [PE-3](#pe-3), [PM-21](#pm-21), [PT-7](#pt-7), [RA-8](#ra-8), [SC-7(9)](#sc-7.9), [SC-7(15)](#sc-7.15), [SI-3(8)](#si-3.8), [SI-4(22)](#si-4.22), [SI-7(8)](#si-7.8) , and [SI-10(1)](#si-10.1) . Organizations include event types that are required by applicable laws, executive orders, directives, policies, regulations, standards, and guidelines. Audit records can be generated at various levels, including at the packet level as information traverses the network. Selecting the appropriate level of event logging is an important part of a monitoring and auditing capability and can identify the root causes of problems. When defining event types, organizations consider the logging necessary to cover related event types, such as the steps in distributed, transaction-based processes and the actions that occur in service-oriented architectures.

**Organisation-defined parameters**

- `au-2_prm_2` ()
- `au-02_odp.01` (AU-02_ODP[01])
- `au-02_odp.02` (AU-02_ODP[02])
- `au-02_odp.03` (AU-02_ODP[03])
- `au-02_odp.04` (AU-02_ODP[04])

**Related controls**: AC-2, AC-3, AC-6, AC-7, AC-8, AC-16, AC-17, AU-3, AU-4, AU-5, AU-6, AU-7, AU-11, AU-12, CM-3, CM-5, CM-6, CM-13, IA-3, MA-4, MP-4, PE-3, PM-21, PT-2, PT-7, RA-8, SA-8, SC-7, SC-18, SI-3, SI-4, SI-7, SI-10, SI-11

**Enhancements** (4):

- **AU-2.1** — Compilation of Audit Records from Multiple Sources
- **AU-2.2** — Selection of Audit Events by Component
- **AU-2.3** — Reviews and Updates
- **AU-2.4** — Privileged Functions

### AU-3 — Content of Audit Records

**Statement (OSCAL)**

```
Ensure that audit records contain information that establishes the following:
```

**Guidance (OSCAL)**

> Audit record content that may be necessary to support the auditing function includes event descriptions (item a), time stamps (item b), source and destination addresses (item c), user or process identifiers (items d and f), success or fail indications (item e), and filenames involved (items a, c, e, and f) . Event outcomes include indicators of event success or failure and event-specific results, such as the system security and privacy posture after the event occurred. Organizations consider how audit records can reveal information about individuals that may give rise to privacy risks and how best to mitigate such risks. For example, there is the potential to reveal personally identifiable information in the audit trail, especially if the trail records inputs or is based on patterns or time of usage.

**Related controls**: AU-2, AU-8, AU-12, AU-14, MA-4, PL-9, SA-8, SI-7, SI-11

**Enhancements** (3):

- **AU-3.1** — Additional Audit Information
- **AU-3.2** — Centralized Management of Planned Audit Record Content
- **AU-3.3** — Limit Personally Identifiable Information Elements

### AU-4 — Audit Log Storage Capacity

**Statement (OSCAL)**

```
Allocate audit log storage capacity to accommodate {{ insert: param, au-04_odp }}.
```

**Guidance (OSCAL)**

> Organizations consider the types of audit logging to be performed and the audit log processing requirements when allocating audit log storage capacity. Allocating sufficient audit log storage capacity reduces the likelihood of such capacity being exceeded and resulting in the potential loss or reduction of audit logging capability.

**Organisation-defined parameters**

- `au-04_odp` (AU-04_ODP)

**Related controls**: AU-2, AU-5, AU-6, AU-7, AU-9, AU-11, AU-12, AU-14, SI-4

**Enhancements** (1):

- **AU-4.1** — Transfer to Alternate Storage

### AU-5 — Response to Audit Logging Process Failures

**Statement (OSCAL)**

```
a. Alert {{ insert: param, au-05_odp.01 }} within {{ insert: param, au-05_odp.02 }} in the event of an audit logging process failure; and
b. Take the following additional actions: {{ insert: param, au-05_odp.03 }}.
```

**Guidance (OSCAL)**

> Audit logging process failures include software and hardware errors, failures in audit log capturing mechanisms, and reaching or exceeding audit log storage capacity. Organization-defined actions include overwriting oldest audit records, shutting down the system, and stopping the generation of audit records. Organizations may choose to define additional actions for audit logging process failures based on the type of failure, the location of the failure, the severity of the failure, or a combination of such factors. When the audit logging process failure is related to storage, the response is carried out for the audit log storage repository (i.e., the distinct system component where the audit logs are stored), the system on which the audit logs reside, the total audit log storage capacity of the organization (i.e., all audit log storage repositories combined), or all three. Organizations may decide to take no additional actions after alerting designated roles or personnel.

**Organisation-defined parameters**

- `au-05_odp.01` (AU-05_ODP[01])
- `au-05_odp.02` (AU-05_ODP[02])
- `au-05_odp.03` (AU-05_ODP[03])

**Related controls**: AU-2, AU-4, AU-7, AU-9, AU-11, AU-12, AU-14, SI-4, SI-12

**Enhancements** (5):

- **AU-5.1** — Storage Capacity Warning
- **AU-5.2** — Real-time Alerts
- **AU-5.3** — Configurable Traffic Volume Thresholds
- **AU-5.4** — Shutdown on Failure
- **AU-5.5** — Alternate Audit Logging Capability

### AU-6 — Audit Record Review, Analysis, and Reporting

**Statement (OSCAL)**

```
a. Review and analyze system audit records {{ insert: param, au-06_odp.01 }} for indications of {{ insert: param, au-06_odp.02 }} and the potential impact of the inappropriate or unusual activity;
b. Report findings to {{ insert: param, au-06_odp.03 }} ; and
c. Adjust the level of audit record review, analysis, and reporting within the system when there is a change in risk based on law enforcement information, intelligence information, or other credible sources of information.
```

**Guidance (OSCAL)**

> Audit record review, analysis, and reporting covers information security- and privacy-related logging performed by organizations, including logging that results from the monitoring of account usage, remote access, wireless connectivity, mobile device connection, configuration settings, system component inventory, use of maintenance tools and non-local maintenance, physical access, temperature and humidity, equipment delivery and removal, communications at system interfaces, and use of mobile code or Voice over Internet Protocol (VoIP). Findings can be reported to organizational entities that include the incident response team, help desk, and security or privacy offices. If organizations are prohibited from reviewing and analyzing audit records or unable to conduct such activities, the review or analysis may be carried out by other organizations granted such authority. The frequency, scope, and/or depth of the audit record review, analysis, and reporting may be adjusted to meet organizational needs based on new information received.

**Organisation-defined parameters**

- `au-06_odp.01` (AU-06_ODP[01])
- `au-06_odp.02` (AU-06_ODP[02])
- `au-06_odp.03` (AU-06_ODP[03])

**Related controls**: AC-2, AC-3, AC-5, AC-6, AC-7, AC-17, AU-7, AU-16, CA-2, CA-7, CM-2, CM-5, CM-6, CM-10, CM-11, IA-2, IA-3, IA-5, IA-8, IR-5, MA-4, MP-4, PE-3, PE-6, RA-5, SA-8, SC-7, SI-3, SI-4, SI-7

**Enhancements** (10):

- **AU-6.1** — Automated Process Integration
- **AU-6.2** — Automated Security Alerts
- **AU-6.3** — Correlate Audit Record Repositories
- **AU-6.4** — Central Review and Analysis
- **AU-6.5** — Integrated Analysis of Audit Records
- **AU-6.6** — Correlation with Physical Monitoring
- **AU-6.7** — Permitted Actions
- **AU-6.8** — Full Text Analysis of Privileged Commands
- **AU-6.9** — Correlation with Information from Nontechnical Sources
- **AU-6.10** — Audit Level Adjustment

### AU-7 — Audit Record Reduction and Report Generation

**Statement (OSCAL)**

```
Provide and implement an audit record reduction and report generation capability that:
```

**Guidance (OSCAL)**

> Audit record reduction is a process that manipulates collected audit log information and organizes it into a summary format that is more meaningful to analysts. Audit record reduction and report generation capabilities do not always emanate from the same system or from the same organizational entities that conduct audit logging activities. The audit record reduction capability includes modern data mining techniques with advanced data filters to identify anomalous behavior in audit records. The report generation capability provided by the system can generate customizable reports. Time ordering of audit records can be an issue if the granularity of the timestamp in the record is insufficient.

**Related controls**: AC-2, AU-2, AU-3, AU-4, AU-5, AU-6, AU-12, AU-16, CM-5, IA-5, IR-4, PM-12, SI-4

**Enhancements** (2):

- **AU-7.1** — Automatic Processing
- **AU-7.2** — Automatic Sort and Search

### AU-8 — Time Stamps

**Statement (OSCAL)**

```
a. Use internal system clocks to generate time stamps for audit records; and
b. Record time stamps for audit records that meet {{ insert: param, au-08_odp }} and that use Coordinated Universal Time, have a fixed local time offset from Coordinated Universal Time, or that include the local time offset as part of the time stamp.
```

**Guidance (OSCAL)**

> Time stamps generated by the system include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. Granularity of time measurements refers to the degree of synchronization between system clocks and reference clocks (e.g., clocks synchronizing within hundreds of milliseconds or tens of milliseconds). Organizations may define different time granularities for different system components. Time service can be critical to other security capabilities such as access control and identification and authentication, depending on the nature of the mechanisms used to support those capabilities.

**Organisation-defined parameters**

- `au-08_odp` (AU-08_ODP)

**Related controls**: AU-3, AU-12, AU-14, SC-45

**Enhancements** (2):

- **AU-8.1** — Synchronization with Authoritative Time Source
- **AU-8.2** — Secondary Authoritative Time Source

### AU-9 — Protection of Audit Information

**Statement (OSCAL)**

```
a. Protect audit information and audit logging tools from unauthorized access, modification, and deletion; and
b. Alert {{ insert: param, au-09_odp }} upon detection of unauthorized access, modification, or deletion of audit information.
```

**Guidance (OSCAL)**

> Audit information includes all information needed to successfully audit system activity, such as audit records, audit log settings, audit reports, and personally identifiable information. Audit logging tools are those programs and devices used to conduct system audit and logging activities. Protection of audit information focuses on technical protection and limits the ability to access and execute audit logging tools to authorized individuals. Physical protection of audit information is addressed by both media protection controls and physical and environmental protection controls.

**Organisation-defined parameters**

- `au-09_odp` (AU-09_ODP)

**Related controls**: AC-3, AC-6, AU-6, AU-11, AU-14, AU-15, MP-2, MP-4, PE-2, PE-3, PE-6, SA-8, SC-8, SI-4

**Enhancements** (7):

- **AU-9.1** — Hardware Write-once Media
- **AU-9.2** — Store on Separate Physical Systems or Components
- **AU-9.3** — Cryptographic Protection
- **AU-9.4** — Access by Subset of Privileged Users
- **AU-9.5** — Dual Authorization
- **AU-9.6** — Read-only Access
- **AU-9.7** — Store on Component with Different Operating System

### AU-10 — Non-repudiation

**Statement (OSCAL)**

```
Provide irrefutable evidence that an individual (or process acting on behalf of an individual) has performed {{ insert: param, au-10_odp }}.
```

**Guidance (OSCAL)**

> Types of individual actions covered by non-repudiation include creating information, sending and receiving messages, and approving information. Non-repudiation protects against claims by authors of not having authored certain documents, senders of not having transmitted messages, receivers of not having received messages, and signatories of not having signed documents. Non-repudiation services can be used to determine if information originated from an individual or if an individual took specific actions (e.g., sending an email, signing a contract, approving a procurement request, or receiving specific information). Organizations obtain non-repudiation services by employing various techniques or mechanisms, including digital signatures and digital message receipts.

**Organisation-defined parameters**

- `au-10_odp` (AU-10_ODP)

**Related controls**: AU-9, PM-12, SA-8, SC-8, SC-12, SC-13, SC-16, SC-17, SC-23

**Enhancements** (5):

- **AU-10.1** — Association of Identities
- **AU-10.2** — Validate Binding of Information Producer Identity
- **AU-10.3** — Chain of Custody
- **AU-10.4** — Validate Binding of Information Reviewer Identity
- **AU-10.5** — Digital Signatures

### AU-11 — Audit Record Retention

**Statement (OSCAL)**

```
Retain audit records for {{ insert: param, au-11_odp }} to provide support for after-the-fact investigations of incidents and to meet regulatory and organizational information retention requirements.
```

**Guidance (OSCAL)**

> Organizations retain audit records until it is determined that the records are no longer needed for administrative, legal, audit, or other operational purposes. This includes the retention and availability of audit records relative to Freedom of Information Act (FOIA) requests, subpoenas, and law enforcement actions. Organizations develop standard categories of audit records relative to such types of actions and standard response processes for each type of action. The National Archives and Records Administration (NARA) General Records Schedules provide federal policy on records retention.

**Organisation-defined parameters**

- `au-11_odp` (AU-11_ODP)

**Related controls**: AU-2, AU-4, AU-5, AU-6, AU-9, AU-14, MP-6, RA-5, SI-12

**Enhancements** (1):

- **AU-11.1** — Long-term Retrieval Capability

### AU-12 — Audit Record Generation

**Statement (OSCAL)**

```
a. Provide audit record generation capability for the event types the system is capable of auditing as defined in [AU-2a](#au-2_smt.a) on {{ insert: param, au-12_odp.01 }};
b. Allow {{ insert: param, au-12_odp.02 }} to select the event types that are to be logged by specific components of the system; and
c. Generate audit records for the event types defined in [AU-2c](#au-2_smt.c) that include the audit record content defined in [AU-3](#au-3).
```

**Guidance (OSCAL)**

> Audit records can be generated from many different system components. The event types specified in [AU-2d](#au-2_smt.d) are the event types for which audit logs are to be generated and are a subset of all event types for which the system can generate audit records.

**Organisation-defined parameters**

- `au-12_odp.01` (AU-12_ODP[01])
- `au-12_odp.02` (AU-12_ODP[02])

**Related controls**: AC-6, AC-17, AU-2, AU-3, AU-4, AU-5, AU-6, AU-7, AU-14, CM-5, MA-4, MP-4, PM-12, SA-8, SC-18, SI-3, SI-4, SI-7, SI-10

**Enhancements** (4):

- **AU-12.1** — System-wide and Time-correlated Audit Trail
- **AU-12.2** — Standardized Formats
- **AU-12.3** — Changes by Authorized Individuals
- **AU-12.4** — Query Parameter Audits of Personally Identifiable Information

### AU-13 — Monitoring for Information Disclosure

**Statement (OSCAL)**

```
a. Monitor {{ insert: param, au-13_odp.01 }} {{ insert: param, au-13_odp.02 }} for evidence of unauthorized disclosure of organizational information; and
b. If an information disclosure is discovered:
```

**Guidance (OSCAL)**

> Unauthorized disclosure of information is a form of data leakage. Open-source information includes social networking sites and code-sharing platforms and repositories. Examples of organizational information include personally identifiable information retained by the organization or proprietary information generated by the organization.

**Organisation-defined parameters**

- `au-13_odp.01` (AU-13_ODP[01])
- `au-13_odp.02` (AU-13_ODP[02])
- `au-13_odp.03` (AU-13_ODP[03])
- `au-13_odp.04` (AU-13_ODP[04])

**Related controls**: AC-22, PE-3, PM-12, RA-5, SC-7, SI-20

**Enhancements** (3):

- **AU-13.1** — Use of Automated Tools
- **AU-13.2** — Review of Monitored Sites
- **AU-13.3** — Unauthorized Replication of Information

### AU-14 — Session Audit

**Statement (OSCAL)**

```
a. Provide and implement the capability for {{ insert: param, au-14_odp.01 }} to {{ insert: param, au-14_odp.02 }} the content of a user session under {{ insert: param, au-14_odp.03 }} ; and
b. Develop, integrate, and use session auditing activities in consultation with legal counsel and in accordance with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines.
```

**Guidance (OSCAL)**

> Session audits can include monitoring keystrokes, tracking websites visited, and recording information and/or file transfers. Session audit capability is implemented in addition to event logging and may involve implementation of specialized session capture technology. Organizations consider how session auditing can reveal information about individuals that may give rise to privacy risk as well as how to mitigate those risks. Because session auditing can impact system and network performance, organizations activate the capability under well-defined situations (e.g., the organization is suspicious of a specific individual). Organizations consult with legal counsel, civil liberties officials, and privacy officials to ensure that any legal, privacy, civil rights, or civil liberties issues, including the use of personally identifiable information, are appropriately addressed.

**Organisation-defined parameters**

- `au-14_odp.01` (AU-14_ODP[01])
- `au-14_odp.02` (AU-14_ODP[02])
- `au-14_odp.03` (AU-14_ODP[03])

**Related controls**: AC-3, AC-8, AU-2, AU-3, AU-4, AU-5, AU-8, AU-9, AU-11, AU-12

**Enhancements** (3):

- **AU-14.1** — System Start-up
- **AU-14.2** — Capture and Record Content
- **AU-14.3** — Remote Viewing and Listening

### AU-16 — Cross-organizational Audit Logging

**Statement (OSCAL)**

```
Employ {{ insert: param, au-16_odp.01 }} for coordinating {{ insert: param, au-16_odp.02 }} among external organizations when audit information is transmitted across organizational boundaries.
```

**Guidance (OSCAL)**

> When organizations use systems or services of external organizations, the audit logging capability necessitates a coordinated, cross-organization approach. For example, maintaining the identity of individuals who request specific services across organizational boundaries may often be difficult, and doing so may prove to have significant performance and privacy ramifications. Therefore, it is often the case that cross-organizational audit logging simply captures the identity of individuals who issue requests at the initial system, and subsequent systems record that the requests originated from authorized individuals. Organizations consider including processes for coordinating audit information requirements and protection of audit information in information exchange agreements.

**Organisation-defined parameters**

- `au-16_odp.01` (AU-16_ODP[01])
- `au-16_odp.02` (AU-16_ODP[02])

**Related controls**: AU-3, AU-6, AU-7, CA-3, PT-7

**Enhancements** (3):

- **AU-16.1** — Identity Preservation
- **AU-16.2** — Sharing of Audit Information
- **AU-16.3** — Disassociability


---

## IA — Identification and Authentication

*13 base controls (enhancements listed per-control).*

### IA-1 — Policy and Procedures

**Statement (OSCAL)**

```
a. Develop, document, and disseminate to {{ insert: param, ia-1_prm_1 }}:
b. Designate an {{ insert: param, ia-01_odp.04 }} to manage the development, documentation, and dissemination of the identification and authentication policy and procedures; and
c. Review and update the current identification and authentication:
```

**Guidance (OSCAL)**

> Identification and authentication policy and procedures address the controls in the IA family that are implemented within systems and organizations. The risk management strategy is an important factor in establishing such policies and procedures. Policies and procedures contribute to security and privacy assurance. Therefore, it is important that security and privacy programs collaborate on the development of identification and authentication policy and procedures. Security and privacy program policies and procedures at the organization level are preferable, in general, and may obviate the need for mission- or system-specific policies and procedures. The policy can be included as part of the general security and privacy policy or be represented by multiple policies that reflect the complex nature of organizations. Procedures can be established for security and privacy programs, for mission or business processes, and for systems, if needed. Procedures describe how the policies or controls are implemented and can be directed at the individual or role that is the object of the procedure. Procedures can be documented in system security and privacy plans or in one or more separate documents. Events that may precipitate an update to identification and authentication policy and procedures include assessment or audit findings, security incidents or breaches, or changes in applicable laws, executive orders, directives, regulations, policies, standards, and guidelines. Simply restating controls does not constitute an organizational policy or procedure.

**Organisation-defined parameters**

- `ia-1_prm_1` ()
- `ia-01_odp.01` (IA-01_ODP[01])
- `ia-01_odp.02` (IA-01_ODP[02])
- `ia-01_odp.03` (IA-01_ODP[03])
- `ia-01_odp.04` (IA-01_ODP[04])
- `ia-01_odp.05` (IA-01_ODP[05])
- `ia-01_odp.06` (IA-01_ODP[06])
- `ia-01_odp.07` (IA-01_ODP[07])
- `ia-01_odp.08` (IA-01_ODP[08])

**Related controls**: AC-1, PM-9, PS-8, SI-12

### IA-2 — Identification and Authentication (Organizational Users)

**Statement (OSCAL)**

```
Uniquely identify and authenticate organizational users and associate that unique identification with processes acting on behalf of those users.
```

**Guidance (OSCAL)**

> Organizations can satisfy the identification and authentication requirements by complying with the requirements in [HSPD 12](#f16e438e-7114-4144-bfe2-2dfcad8cb2d0) . Organizational users include employees or individuals who organizations consider to have an equivalent status to employees (e.g., contractors and guest researchers). Unique identification and authentication of users applies to all accesses other than those that are explicitly identified in [AC-14](#ac-14) and that occur through the authorized use of group authenticators without individual authentication. Since processes execute on behalf of groups and roles, organizations may require unique identification of individuals in group accounts or for detailed accountability of individual activity.

> Organizations employ passwords, physical authenticators, or biometrics to authenticate user identities or, in the case of multi-factor authentication, some combination thereof. Access to organizational systems is defined as either local access or network access. Local access is any access to organizational systems by users or processes acting on behalf of users, where access is obtained through direct connections without the use of networks. Network access is access to organizational systems by users (or processes acting on behalf of users) where access is obtained through network connections (i.e., nonlocal accesses). Remote access is a type of network access that involves communication through external networks. Internal networks include local area networks and wide area networks.

> The use of encrypted virtual private networks for network connections between organization-controlled endpoints and non-organization-controlled endpoints may be treated as internal networks with respect to protecting the confidentiality and integrity of information traversing the network. Identification and authentication requirements for non-organizational users are described in [IA-8](#ia-8).

**Related controls**: AC-2, AC-3, AC-4, AC-14, AC-17, AC-18, AU-1, AU-6, IA-4, IA-5, IA-8, IA-13, MA-4, MA-5, PE-2, PL-4, SA-4, SA-8

**Enhancements** (13):

- **IA-2.1** — Multi-factor Authentication to Privileged Accounts
- **IA-2.2** — Multi-factor Authentication to Non-privileged Accounts
- **IA-2.3** — Local Access to Privileged Accounts
- **IA-2.4** — Local Access to Non-privileged Accounts
- **IA-2.5** — Individual Authentication with Group Authentication
- **IA-2.6** — Access to Accounts —separate Device
- **IA-2.7** — Network Access to Non-privileged Accounts — Separate Device
- **IA-2.8** — Access to Accounts — Replay Resistant
- **IA-2.9** — Network Access to Non-privileged Accounts — Replay Resistant
- **IA-2.10** — Single Sign-on
- **IA-2.11** — Remote Access — Separate Device
- **IA-2.12** — Acceptance of PIV Credentials
- **IA-2.13** — Out-of-band Authentication

### IA-3 — Device Identification and Authentication

**Statement (OSCAL)**

```
Uniquely identify and authenticate {{ insert: param, ia-03_odp.01 }} before establishing a {{ insert: param, ia-03_odp.02 }} connection.
```

**Guidance (OSCAL)**

> Devices that require unique device-to-device identification and authentication are defined by type, device, or a combination of type and device. Organization-defined device types include devices that are not owned by the organization. Systems use shared known information (e.g., Media Access Control [MAC], Transmission Control Protocol/Internet Protocol [TCP/IP] addresses) for device identification or organizational authentication solutions (e.g., Institute of Electrical and Electronics Engineers (IEEE) 802.1x and Extensible Authentication Protocol [EAP], RADIUS server with EAP-Transport Layer Security [TLS] authentication, Kerberos) to identify and authenticate devices on local and wide area networks. Organizations determine the required strength of authentication mechanisms based on the security categories of systems and mission or business requirements. Because of the challenges of implementing device authentication on a large scale, organizations can restrict the application of the control to a limited number/type of devices based on mission or business needs.

**Organisation-defined parameters**

- `ia-03_odp.01` (IA-03_ODP[01])
- `ia-03_odp.02` (IA-03_ODP[02])

**Related controls**: AC-17, AC-18, AC-19, AU-6, CA-3, CA-9, IA-4, IA-5, IA-9, IA-11, IA-13, SI-4

**Enhancements** (4):

- **IA-3.1** — Cryptographic Bidirectional Authentication
- **IA-3.2** — Cryptographic Bidirectional Network Authentication
- **IA-3.3** — Dynamic Address Allocation
- **IA-3.4** — Device Attestation

### IA-4 — Identifier Management

**Statement (OSCAL)**

```
Manage system identifiers by:
```

**Guidance (OSCAL)**

> Common device identifiers include Media Access Control (MAC) addresses, Internet Protocol (IP) addresses, or device-unique token identifiers. The management of individual identifiers is not applicable to shared system accounts. Typically, individual identifiers are the usernames of the system accounts assigned to those individuals. In such instances, the account management activities of [AC-2](#ac-2) use account names provided by [IA-4](#ia-4) . Identifier management also addresses individual identifiers not necessarily associated with system accounts. Preventing the reuse of identifiers implies preventing the assignment of previously used individual, group, role, service, or device identifiers to different individuals, groups, roles, services, or devices.

**Organisation-defined parameters**

- `ia-04_odp.01` (IA-04_ODP[01])
- `ia-04_odp.02` (IA-04_ODP[02])

**Related controls**: AC-5, IA-2, IA-3, IA-5, IA-8, IA-9, IA-12, MA-4, PE-2, PE-3, PE-4, PL-4, PM-12, PS-3, PS-4, PS-5, SC-37

**Enhancements** (9):

- **IA-4.1** — Prohibit Account Identifiers as Public Identifiers
- **IA-4.2** — Supervisor Authorization
- **IA-4.3** — Multiple Forms of Certification
- **IA-4.4** — Identify User Status
- **IA-4.5** — Dynamic Management
- **IA-4.6** — Cross-organization Management
- **IA-4.7** — In-person Registration
- **IA-4.8** — Pairwise Pseudonymous Identifiers
- **IA-4.9** — Attribute Maintenance and Protection

### IA-5 — Authenticator Management

**Statement (OSCAL)**

```
Manage system authenticators by:
```

**Guidance (OSCAL)**

> Authenticators include passwords, cryptographic devices, biometrics, certificates, one-time password devices, and ID badges. Device authenticators include certificates and passwords. Initial authenticator content is the actual content of the authenticator (e.g., the initial password). In contrast, the requirements for authenticator content contain specific criteria or characteristics (e.g., minimum password length). Developers may deliver system components with factory default authentication credentials (i.e., passwords) to allow for initial installation and configuration. Default authentication credentials are often well known, easily discoverable, and present a significant risk. The requirement to protect individual authenticators may be implemented via control [PL-4](#pl-4) or [PS-6](#ps-6) for authenticators in the possession of individuals and by controls [AC-3](#ac-3), [AC-6](#ac-6) , and [SC-28](#sc-28) for authenticators stored in organizational systems, including passwords stored in hashed or encrypted formats or files containing encrypted or hashed passwords accessible with administrator privileges.

> Systems support authenticator management by organization-defined settings and restrictions for various authenticator characteristics (e.g., minimum password length, validation time window for time synchronous one-time tokens, and number of allowed rejections during the verification stage of biometric authentication). Actions can be taken to safeguard individual authenticators, including maintaining possession of authenticators, not sharing authenticators with others, and immediately reporting lost, stolen, or compromised authenticators. Authenticator management includes issuing and revoking authenticators for temporary access when no longer needed.

**Organisation-defined parameters**

- `ia-05_odp.01` (IA-05_ODP[01])
- `ia-05_odp.02` (IA-05_ODP[02])

**Related controls**: AC-3, AC-6, CM-6, IA-2, IA-4, IA-7, IA-8, IA-9, MA-4, PE-2, PL-4, SC-12, SC-13

**Enhancements** (18):

- **IA-5.1** — Password-based Authentication
- **IA-5.2** — Public Key-based Authentication
- **IA-5.3** — In-person or Trusted External Party Registration
- **IA-5.4** — Automated Support for Password Strength Determination
- **IA-5.5** — Change Authenticators Prior to Delivery
- **IA-5.6** — Protection of Authenticators
- **IA-5.7** — No Embedded Unencrypted Static Authenticators
- **IA-5.8** — Multiple System Accounts
- **IA-5.9** — Federated Credential Management
- **IA-5.10** — Dynamic Credential Binding
- **IA-5.11** — Hardware Token-based Authentication
- **IA-5.12** — Biometric Authentication Performance
- **IA-5.13** — Expiration of Cached Authenticators
- **IA-5.14** — Managing Content of PKI Trust Stores
- **IA-5.15** — GSA-approved Products and Services
- **IA-5.16** — In-person or Trusted External Party Authenticator Issuance
- **IA-5.17** — Presentation Attack Detection for Biometric Authenticators
- **IA-5.18** — Password Managers

### IA-6 — Authentication Feedback

**Statement (OSCAL)**

```
Obscure feedback of authentication information during the authentication process to protect the information from possible exploitation and use by unauthorized individuals.
```

**Guidance (OSCAL)**

> Authentication feedback from systems does not provide information that would allow unauthorized individuals to compromise authentication mechanisms. For some types of systems, such as desktops or notebooks with relatively large monitors, the threat (referred to as shoulder surfing) may be significant. For other types of systems, such as mobile devices with small displays, the threat may be less significant and is balanced against the increased likelihood of typographic input errors due to small keyboards. Thus, the means for obscuring authentication feedback is selected accordingly. Obscuring authentication feedback includes displaying asterisks when users type passwords into input devices or displaying feedback for a very limited time before obscuring it.

**Related controls**: AC-3

### IA-7 — Cryptographic Module Authentication

**Statement (OSCAL)**

```
Implement mechanisms for authentication to a cryptographic module that meet the requirements of applicable laws, executive orders, directives, policies, regulations, standards, and guidelines for such authentication.
```

**Guidance (OSCAL)**

> Authentication mechanisms may be required within a cryptographic module to authenticate an operator accessing the module and to verify that the operator is authorized to assume the requested role and perform services within that role.

**Related controls**: AC-3, IA-5, SA-4, SC-12, SC-13

### IA-8 — Identification and Authentication (Non-organizational Users)

**Statement (OSCAL)**

```
Uniquely identify and authenticate non-organizational users or processes acting on behalf of non-organizational users.
```

**Guidance (OSCAL)**

> Non-organizational users include system users other than organizational users explicitly covered by [IA-2](#ia-2) . Non-organizational users are uniquely identified and authenticated for accesses other than those explicitly identified and documented in [AC-14](#ac-14) . Identification and authentication of non-organizational users accessing federal systems may be required to protect federal, proprietary, or privacy-related information (with exceptions noted for national security systems). Organizations consider many factors—including security, privacy, scalability, and practicality—when balancing the need to ensure ease of use for access to federal information and systems with the need to protect and adequately mitigate risk.

**Related controls**: AC-2, AC-6, AC-14, AC-17, AC-18, AU-6, IA-2, IA-4, IA-5, IA-10, IA-11, IA-13, MA-4, RA-3, SA-4, SC-8

**Enhancements** (6):

- **IA-8.1** — Acceptance of PIV Credentials from Other Agencies
- **IA-8.2** — Acceptance of External Authenticators
- **IA-8.3** — Use of FICAM-approved Products
- **IA-8.4** — Use of Defined Profiles
- **IA-8.5** — Acceptance of PIV-I Credentials
- **IA-8.6** — Disassociability

### IA-9 — Service Identification and Authentication

**Statement (OSCAL)**

```
Uniquely identify and authenticate {{ insert: param, ia-09_odp }} before establishing communications with devices, users, or other services or applications.
```

**Guidance (OSCAL)**

> Services that may require identification and authentication include web applications using digital certificates or services or applications that query a database. Identification and authentication methods for system services and applications include information or code signing, provenance graphs, and electronic signatures that indicate the sources of services. Decisions regarding the validity of identification and authentication claims can be made by services separate from the services acting on those decisions. This can occur in distributed system architectures. In such situations, the identification and authentication decisions (instead of actual identifiers and authentication data) are provided to the services that need to act on those decisions.

**Organisation-defined parameters**

- `ia-09_odp` (IA-09_ODP)

**Related controls**: IA-3, IA-4, IA-5, IA-13, SC-8

**Enhancements** (2):

- **IA-9.1** — Information Exchange
- **IA-9.2** — Transmission of Decisions

### IA-10 — Adaptive Authentication

**Statement (OSCAL)**

```
Require individuals accessing the system to employ {{ insert: param, ia-10_odp.01 }} under specific {{ insert: param, ia-10_odp.02 }}.
```

**Guidance (OSCAL)**

> Adversaries may compromise individual authentication mechanisms employed by organizations and subsequently attempt to impersonate legitimate users. To address this threat, organizations may employ specific techniques or mechanisms and establish protocols to assess suspicious behavior. Suspicious behavior may include accessing information that individuals do not typically access as part of their duties, roles, or responsibilities; accessing greater quantities of information than individuals would routinely access; or attempting to access information from suspicious network addresses. When pre-established conditions or triggers occur, organizations can require individuals to provide additional authentication information. Another potential use for adaptive authentication is to increase the strength of mechanism based on the number or types of records being accessed. Adaptive authentication does not replace and is not used to avoid the use of multi-factor authentication mechanisms but can augment implementations of multi-factor authentication.

**Organisation-defined parameters**

- `ia-10_odp.01` (IA-10_ODP[01])
- `ia-10_odp.02` (IA-10_ODP[02])

**Related controls**: IA-2, IA-8

### IA-11 — Re-authentication

**Statement (OSCAL)**

```
Require users to re-authenticate when {{ insert: param, ia-11_odp }}.
```

**Guidance (OSCAL)**

> In addition to the re-authentication requirements associated with device locks, organizations may require re-authentication of individuals in certain situations, including when roles, authenticators or credentials change, when security categories of systems change, when the execution of privileged functions occurs, after a fixed time period, or periodically.

**Organisation-defined parameters**

- `ia-11_odp` (IA-11_ODP)

**Related controls**: AC-3, AC-11, IA-2, IA-3, IA-4, IA-8

### IA-12 — Identity Proofing

**Statement (OSCAL)**

```
a. Identity proof users that require accounts for logical access to systems based on appropriate identity assurance level requirements as specified in applicable standards and guidelines;
b. Resolve user identities to a unique individual; and
c. Collect, validate, and verify identity evidence.
```

**Guidance (OSCAL)**

> Identity proofing is the process of collecting, validating, and verifying a user’s identity information for the purposes of establishing credentials for accessing a system. Identity proofing is intended to mitigate threats to the registration of users and the establishment of their accounts. Standards and guidelines specifying identity assurance levels for identity proofing include [SP 800-63-3](#737513fa-6758-403f-831d-5ddab5e23cb3) and [SP 800-63A](#9099ed2c-922a-493d-bcb4-d896192243ff) . Organizations may be subject to laws, executive orders, directives, regulations, or policies that address the collection of identity evidence. Organizational personnel consult with the senior agency official for privacy and legal counsel regarding such requirements.

**Related controls**: AC-5, IA-1, IA-2, IA-3, IA-4, IA-5, IA-6, IA-8, IA-13

**Enhancements** (6):

- **IA-12.1** — Supervisor Authorization
- **IA-12.2** — Identity Evidence
- **IA-12.3** — Identity Evidence Validation and Verification
- **IA-12.4** — In-person Validation and Verification
- **IA-12.5** — Address Confirmation
- **IA-12.6** — Accept Externally-proofed Identities

### IA-13 — Identity Providers and Authorization Servers

**Statement (OSCAL)**

```
Employ identity providers and authorization servers to manage user, device, and non-person entity (NPE) identities, attributes, and access rights supporting authentication and authorization decisions in accordance with {{ insert: param, ia-13_odp.01 }} using {{ insert: param, ia-13_odp.02 }}.
```

**Guidance (OSCAL)**

> Identity providers, both internal and external to the organization, manage the user, device, and NPE authenticators and issue statements, often called identity assertions, attesting to identities of other systems or systems components. Authorization servers create and issue access tokens to identified and authenticated users and devices that can be used to gain access to system or information resources. For example, single sign-on (SSO) provides identity provider and authorization server functions. Authenticator management (to include credential management) is covered by IA-05.

**Organisation-defined parameters**

- `ia-13_odp.01` (IA-13_ODP[01])
- `ia-13_odp.02` (IA-13_ODP[02])

**Related controls**: AC-3, IA-2, IA-3, IA-8, IA-9, IA-12

**Enhancements** (3):

- **IA-13.1** — Protection of Cryptographic Keys
- **IA-13.2** — Verification of Identity Assertions and Access Tokens
- **IA-13.3** — Token Management


---

## SC — System and Communications Protection

*47 base controls (enhancements listed per-control).*

### SC-1 — Policy and Procedures

**Statement (OSCAL)**

```
a. Develop, document, and disseminate to {{ insert: param, sc-1_prm_1 }}:
b. Designate an {{ insert: param, sc-01_odp.04 }} to manage the development, documentation, and dissemination of the system and communications protection policy and procedures; and
c. Review and update the current system and communications protection:
```

**Guidance (OSCAL)**

> System and communications protection policy and procedures address the controls in the SC family that are implemented within systems and organizations. The risk management strategy is an important factor in establishing such policies and procedures. Policies and procedures contribute to security and privacy assurance. Therefore, it is important that security and privacy programs collaborate on the development of system and communications protection policy and procedures. Security and privacy program policies and procedures at the organization level are preferable, in general, and may obviate the need for mission- or system-specific policies and procedures. The policy can be included as part of the general security and privacy policy or be represented by multiple policies that reflect the complex nature of organizations. Procedures can be established for security and privacy programs, for mission or business processes, and for systems, if needed. Procedures describe how the policies or controls are implemented and can be directed at the individual or role that is the object of the procedure. Procedures can be documented in system security and privacy plans or in one or more separate documents. Events that may precipitate an update to system and communications protection policy and procedures include assessment or audit findings, security incidents or breaches, or changes in applicable laws, executive orders, directives, regulations, policies, standards, and guidelines. Simply restating controls does not constitute an organizational policy or procedure.

**Organisation-defined parameters**

- `sc-1_prm_1` ()
- `sc-01_odp.01` (SC-01_ODP[01])
- `sc-01_odp.02` (SC-01_ODP[02])
- `sc-01_odp.03` (SC-01_ODP[03])
- `sc-01_odp.04` (SC-01_ODP[04])
- `sc-01_odp.05` (SC-01_ODP[05])
- `sc-01_odp.06` (SC-01_ODP[06])
- `sc-01_odp.07` (SC-01_ODP[07])
- `sc-01_odp.08` (SC-01_ODP[08])

**Related controls**: PM-9, PS-8, SA-8, SI-12

### SC-2 — Separation of System and User Functionality

**Statement (OSCAL)**

```
Separate user functionality, including user interface services, from system management functionality.
```

**Guidance (OSCAL)**

> System management functionality includes functions that are necessary to administer databases, network components, workstations, or servers. These functions typically require privileged user access. The separation of user functions from system management functions is physical or logical. Organizations may separate system management functions from user functions by using different computers, instances of operating systems, central processing units, or network addresses; by employing virtualization techniques; or some combination of these or other methods. Separation of system management functions from user functions includes web administrative interfaces that employ separate authentication methods for users of any other system resources. Separation of system and user functions may include isolating administrative interfaces on different domains and with additional access controls. The separation of system and user functionality can be achieved by applying the systems security engineering design principles in [SA-8](#sa-8) , including [SA-8(1)](#sa-8.1), [SA-8(3)](#sa-8.3), [SA-8(4)](#sa-8.4), [SA-8(10)](#sa-8.10), [SA-8(12)](#sa-8.12), [SA-8(13)](#sa-8.13), [SA-8(14)](#sa-8.14) , and [SA-8(18)](#sa-8.18).

**Related controls**: AC-6, SA-4, SA-8, SC-3, SC-7, SC-22, SC-32, SC-39

**Enhancements** (2):

- **SC-2.1** — Interfaces for Non-privileged Users
- **SC-2.2** — Disassociability

### SC-3 — Security Function Isolation

**Statement (OSCAL)**

```
Isolate security functions from nonsecurity functions.
```

**Guidance (OSCAL)**

> Security functions are isolated from nonsecurity functions by means of an isolation boundary implemented within a system via partitions and domains. The isolation boundary controls access to and protects the integrity of the hardware, software, and firmware that perform system security functions. Systems implement code separation in many ways, such as through the provision of security kernels via processor rings or processor modes. For non-kernel code, security function isolation is often achieved through file system protections that protect the code on disk and address space protections that protect executing code. Systems can restrict access to security functions using access control mechanisms and by implementing least privilege capabilities. While the ideal is for all code within the defined security function isolation boundary to only contain security-relevant code, it is sometimes necessary to include nonsecurity functions as an exception. The isolation of security functions from nonsecurity functions can be achieved by applying the systems security engineering design principles in [SA-8](#sa-8) , including [SA-8(1)](#sa-8.1), [SA-8(3)](#sa-8.3), [SA-8(4)](#sa-8.4), [SA-8(10)](#sa-8.10), [SA-8(12)](#sa-8.12), [SA-8(13)](#sa-8.13), [SA-8(14)](#sa-8.14) , and [SA-8(18)](#sa-8.18).

**Related controls**: AC-3, AC-6, AC-25, CM-2, CM-4, SA-4, SA-5, SA-8, SA-15, SA-17, SC-2, SC-7, SC-32, SC-39, SI-16

**Enhancements** (5):

- **SC-3.1** — Hardware Separation
- **SC-3.2** — Access and Flow Control Functions
- **SC-3.3** — Minimize Nonsecurity Functionality
- **SC-3.4** — Module Coupling and Cohesiveness
- **SC-3.5** — Layered Structures

### SC-4 — Information in Shared System Resources

**Statement (OSCAL)**

```
Prevent unauthorized and unintended information transfer via shared system resources.
```

**Guidance (OSCAL)**

> Preventing unauthorized and unintended information transfer via shared system resources stops information produced by the actions of prior users or roles (or the actions of processes acting on behalf of prior users or roles) from being available to current users or roles (or current processes acting on behalf of current users or roles) that obtain access to shared system resources after those resources have been released back to the system. Information in shared system resources also applies to encrypted representations of information. In other contexts, control of information in shared system resources is referred to as object reuse and residual information protection. Information in shared system resources does not address information remanence, which refers to the residual representation of data that has been nominally deleted; covert channels (including storage and timing channels), where shared system resources are manipulated to violate information flow restrictions; or components within systems for which there are only single users or roles.

**Related controls**: AC-3, AC-4, SA-8

**Enhancements** (2):

- **SC-4.1** — Security Levels
- **SC-4.2** — Multilevel or Periods Processing

### SC-5 — Denial-of-service Protection

**Statement (OSCAL)**

```
a. {{ insert: param, sc-05_odp.02 }} the effects of the following types of denial-of-service events: {{ insert: param, sc-05_odp.01 }} ; and
b. Employ the following controls to achieve the denial-of-service objective: {{ insert: param, sc-05_odp.03 }}.
```

**Guidance (OSCAL)**

> Denial-of-service events may occur due to a variety of internal and external causes, such as an attack by an adversary or a lack of planning to support organizational needs with respect to capacity and bandwidth. Such attacks can occur across a wide range of network protocols (e.g., IPv4, IPv6). A variety of technologies are available to limit or eliminate the origination and effects of denial-of-service events. For example, boundary protection devices can filter certain types of packets to protect system components on internal networks from being directly affected by or the source of denial-of-service attacks. Employing increased network capacity and bandwidth combined with service redundancy also reduces the susceptibility to denial-of-service events.

**Organisation-defined parameters**

- `sc-05_odp.01` (SC-05_ODP[01])
- `sc-05_odp.02` (SC-05_ODP[02])
- `sc-05_odp.03` (SC-05_ODP[03])

**Related controls**: CP-2, IR-4, SC-6, SC-7, SC-40

**Enhancements** (3):

- **SC-5.1** — Restrict Ability to Attack Other Systems
- **SC-5.2** — Capacity, Bandwidth, and Redundancy
- **SC-5.3** — Detection and Monitoring

### SC-6 — Resource Availability

**Statement (OSCAL)**

```
Protect the availability of resources by allocating {{ insert: param, sc-06_odp.01 }} by {{ insert: param, sc-06_odp.02 }}.
```

**Guidance (OSCAL)**

> Priority protection prevents lower-priority processes from delaying or interfering with the system that services higher-priority processes. Quotas prevent users or processes from obtaining more than predetermined amounts of resources.

**Organisation-defined parameters**

- `sc-06_odp.01` (SC-06_ODP[01])
- `sc-06_odp.02` (SC-06_ODP[02])
- `sc-06_odp.03` (SC-06_ODP[03])

**Related controls**: SC-5

### SC-7 — Boundary Protection

**Statement (OSCAL)**

```
a. Monitor and control communications at the external managed interfaces to the system and at key internal managed interfaces within the system;
b. Implement subnetworks for publicly accessible system components that are {{ insert: param, sc-07_odp }} separated from internal organizational networks; and
c. Connect to external networks or systems only through managed interfaces consisting of boundary protection devices arranged in accordance with an organizational security and privacy architecture.
```

**Guidance (OSCAL)**

> Managed interfaces include gateways, routers, firewalls, guards, network-based malicious code analysis, virtualization systems, or encrypted tunnels implemented within a security architecture. Subnetworks that are physically or logically separated from internal networks are referred to as demilitarized zones or DMZs. Restricting or prohibiting interfaces within organizational systems includes restricting external web traffic to designated web servers within managed interfaces, prohibiting external traffic that appears to be spoofing internal addresses, and prohibiting internal traffic that appears to be spoofing external addresses. [SP 800-189](#f5edfe51-d1f2-422e-9b27-5d0e90b49c72) provides additional information on source address validation techniques to prevent ingress and egress of traffic with spoofed addresses. Commercial telecommunications services are provided by network components and consolidated management systems shared by customers. These services may also include third party-provided access lines and other service elements. Such services may represent sources of increased risk despite contract security provisions. Boundary protection may be implemented as a common control for all or part of an organizational network such that the boundary to be protected is greater than a system-specific boundary (i.e., an authorization boundary).

**Organisation-defined parameters**

- `sc-07_odp` (SC-07_ODP)

**Related controls**: AC-4, AC-17, AC-18, AC-19, AC-20, AU-13, CA-3, CM-2, CM-4, CM-7, CM-10, CP-8, CP-10, IR-4, MA-4, PE-3, PL-8, PM-12, SA-8, SA-17, SC-5, SC-26, SC-32, SC-35, SC-43

**Enhancements** (29):

- **SC-7.1** — Physically Separated Subnetworks
- **SC-7.2** — Public Access
- **SC-7.3** — Access Points
- **SC-7.4** — External Telecommunications Services
- **SC-7.5** — Deny by Default — Allow by Exception
- **SC-7.6** — Response to Recognized Failures
- **SC-7.7** — Split Tunneling for Remote Devices
- **SC-7.8** — Route Traffic to Authenticated Proxy Servers
- **SC-7.9** — Restrict Threatening Outgoing Communications Traffic
- **SC-7.10** — Prevent Exfiltration
- **SC-7.11** — Restrict Incoming Communications Traffic
- **SC-7.12** — Host-based Protection
- **SC-7.13** — Isolation of Security Tools, Mechanisms, and Support Components
- **SC-7.14** — Protect Against Unauthorized Physical Connections
- **SC-7.15** — Networked Privileged Accesses
- **SC-7.16** — Prevent Discovery of System Components
- **SC-7.17** — Automated Enforcement of Protocol Formats
- **SC-7.18** — Fail Secure
- **SC-7.19** — Block Communication from Non-organizationally Configured Hosts
- **SC-7.20** — Dynamic Isolation and Segregation
- **SC-7.21** — Isolation of System Components
- **SC-7.22** — Separate Subnets for Connecting to Different Security Domains
- **SC-7.23** — Disable Sender Feedback on Protocol Validation Failure
- **SC-7.24** — Personally Identifiable Information
- **SC-7.25** — Unclassified National Security System Connections
- **SC-7.26** — Classified National Security System Connections
- **SC-7.27** — Unclassified Non-national Security System Connections
- **SC-7.28** — Connections to Public Networks
- **SC-7.29** — Separate Subnets to Isolate Functions

### SC-8 — Transmission Confidentiality and Integrity

**Statement (OSCAL)**

```
Protect the {{ insert: param, sc-08_odp }} of transmitted information.
```

**Guidance (OSCAL)**

> Protecting the confidentiality and integrity of transmitted information applies to internal and external networks as well as any system components that can transmit information, including servers, notebook computers, desktop computers, mobile devices, printers, copiers, scanners, facsimile machines, and radios. Unprotected communication paths are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of information can be accomplished by physical or logical means. Physical protection can be achieved by using protected distribution systems. A protected distribution system is a wireline or fiber-optics telecommunications system that includes terminals and adequate electromagnetic, acoustical, electrical, and physical controls to permit its use for the unencrypted transmission of classified information. Logical protection can be achieved by employing encryption techniques.

> Organizations that rely on commercial providers who offer transmission services as commodity services rather than as fully dedicated services may find it difficult to obtain the necessary assurances regarding the implementation of needed controls for transmission confidentiality and integrity. In such situations, organizations determine what types of confidentiality or integrity services are available in standard, commercial telecommunications service packages. If it is not feasible to obtain the necessary controls and assurances of control effectiveness through appropriate contracting vehicles, organizations can implement appropriate compensating controls.

**Organisation-defined parameters**

- `sc-08_odp` (SC-08_ODP)

**Related controls**: AC-17, AC-18, AU-10, IA-3, IA-8, IA-9, MA-4, PE-4, SA-4, SA-8, SC-7, SC-16, SC-20, SC-23, SC-28

**Enhancements** (5):

- **SC-8.1** — Cryptographic Protection
- **SC-8.2** — Pre- and Post-transmission Handling
- **SC-8.3** — Cryptographic Protection for Message Externals
- **SC-8.4** — Conceal or Randomize Communications
- **SC-8.5** — Protected Distribution System

### SC-10 — Network Disconnect

**Statement (OSCAL)**

```
Terminate the network connection associated with a communications session at the end of the session or after {{ insert: param, sc-10_odp }} of inactivity.
```

**Guidance (OSCAL)**

> Network disconnect applies to internal and external networks. Terminating network connections associated with specific communications sessions includes de-allocating TCP/IP address or port pairs at the operating system level and de-allocating the networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. Periods of inactivity may be established by organizations and include time periods by type of network access or for specific network accesses.

**Organisation-defined parameters**

- `sc-10_odp` (SC-10_ODP)

**Related controls**: AC-17, SC-23

### SC-11 — Trusted Path

**Statement (OSCAL)**

```
a. Provide a {{ insert: param, sc-11_odp.01 }} isolated trusted communications path for communications between the user and the trusted components of the system; and
b. Permit users to invoke the trusted communications path for communications between the user and the following security functions of the system, including at a minimum, authentication and re-authentication: {{ insert: param, sc-11_odp.02 }}.
```

**Guidance (OSCAL)**

> Trusted paths are mechanisms by which users can communicate (using input devices such as keyboards) directly with the security functions of systems with the requisite assurance to support security policies. Trusted path mechanisms can only be activated by users or the security functions of organizational systems. User responses that occur via trusted paths are protected from modification by and disclosure to untrusted applications. Organizations employ trusted paths for trustworthy, high-assurance connections between security functions of systems and users, including during system logons. The original implementations of trusted paths employed an out-of-band signal to initiate the path, such as using the <BREAK> key, which does not transmit characters that can be spoofed. In later implementations, a key combination that could not be hijacked was used (e.g., the <CTRL> + <ALT> + <DEL> keys). Such key combinations, however, are platform-specific and may not provide a trusted path implementation in every case. The enforcement of trusted communications paths is provided by a specific implementation that meets the reference monitor concept.

**Organisation-defined parameters**

- `sc-11_odp.01` (SC-11_ODP[01])
- `sc-11_odp.02` (SC-11_ODP[02])

**Related controls**: AC-16, AC-25, SC-12, SC-23

**Enhancements** (1):

- **SC-11.1** — Irrefutable Communications Path

### SC-12 — Cryptographic Key Establishment and Management

**Statement (OSCAL)**

```
Establish and manage cryptographic keys when cryptography is employed within the system in accordance with the following key management requirements: {{ insert: param, sc-12_odp }}.
```

**Guidance (OSCAL)**

> Cryptographic key management and establishment can be performed using manual procedures or automated mechanisms with supporting manual procedures. Organizations define key management requirements in accordance with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines and specify appropriate options, parameters, and levels. Organizations manage trust stores to ensure that only approved trust anchors are part of such trust stores. This includes certificates with visibility external to organizational systems and certificates related to the internal operations of systems. [NIST CMVP](#1acdc775-aafb-4d11-9341-dc6a822e9d38) and [NIST CAVP](#84dc1b0c-acb7-4269-84c4-00dbabacd78c) provide additional information on validated cryptographic modules and algorithms that can be used in cryptographic key management and establishment.

**Organisation-defined parameters**

- `sc-12_odp` (SC-12_ODP)

**Related controls**: AC-17, AU-9, AU-10, CM-3, IA-3, IA-7, IA-13, SA-4, SA-8, SA-9, SC-8, SC-11, SC-13, SC-17, SC-20, SC-37, SC-40, SI-3, SI-7

**Enhancements** (6):

- **SC-12.1** — Availability
- **SC-12.2** — Symmetric Keys
- **SC-12.3** — Asymmetric Keys
- **SC-12.4** — PKI Certificates
- **SC-12.5** — PKI Certificates / Hardware Tokens
- **SC-12.6** — Physical Control of Keys

### SC-13 — Cryptographic Protection

**Statement (OSCAL)**

```
a. Determine the {{ insert: param, sc-13_odp.01 }} ; and
b. Implement the following types of cryptography required for each specified cryptographic use: {{ insert: param, sc-13_odp.02 }}.
```

**Guidance (OSCAL)**

> Cryptography can be employed to support a variety of security solutions, including the protection of classified information and controlled unclassified information, the provision and implementation of digital signatures, and the enforcement of information separation when authorized individuals have the necessary clearances but lack the necessary formal access approvals. Cryptography can also be used to support random number and hash generation. Generally applicable cryptographic standards include FIPS-validated cryptography and NSA-approved cryptography. For example, organizations that need to protect classified information may specify the use of NSA-approved cryptography. Organizations that need to provision and implement digital signatures may specify the use of FIPS-validated cryptography. Cryptography is implemented in accordance with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines.

**Organisation-defined parameters**

- `sc-13_odp.01` (SC-13_ODP[01])
- `sc-13_odp.02` (SC-13_ODP[02])

**Related controls**: AC-2, AC-3, AC-7, AC-17, AC-18, AC-19, AU-9, AU-10, CM-11, CP-9, IA-3, IA-5, IA-7, IA-13, MA-4, MP-2, MP-4, MP-5, SA-4, SA-8, SA-9, SC-8, SC-12, SC-20, SC-23, SC-28, SC-40, SI-3, SI-7

**Enhancements** (4):

- **SC-13.1** — FIPS-validated Cryptography
- **SC-13.2** — NSA-approved Cryptography
- **SC-13.3** — Individuals Without Formal Access Approvals
- **SC-13.4** — Digital Signatures

### SC-15 — Collaborative Computing Devices and Applications

**Statement (OSCAL)**

```
a. Prohibit remote activation of collaborative computing devices and applications with the following exceptions: {{ insert: param, sc-15_odp }} ; and
b. Provide an explicit indication of use to users physically present at the devices.
```

**Guidance (OSCAL)**

> Collaborative computing devices and applications include remote meeting devices and applications, networked white boards, cameras, and microphones. The explicit indication of use includes signals to users when collaborative computing devices and applications are activated.

**Organisation-defined parameters**

- `sc-15_odp` (SC-15_ODP)

**Related controls**: AC-21, SC-42

**Enhancements** (4):

- **SC-15.1** — Physical or Logical Disconnect
- **SC-15.2** — Blocking Inbound and Outbound Communications Traffic
- **SC-15.3** — Disabling and Removal in Secure Work Areas
- **SC-15.4** — Explicitly Indicate Current Participants

### SC-16 — Transmission of Security and Privacy Attributes

**Statement (OSCAL)**

```
Associate {{ insert: param, sc-16_prm_1 }} with information exchanged between systems and between system components.
```

**Guidance (OSCAL)**

> Security and privacy attributes can be explicitly or implicitly associated with the information contained in organizational systems or system components. Attributes are abstractions that represent the basic properties or characteristics of an entity with respect to protecting information or the management of personally identifiable information. Attributes are typically associated with internal data structures, including records, buffers, and files within the system. Security and privacy attributes are used to implement access control and information flow control policies; reflect special dissemination, management, or distribution instructions, including permitted uses of personally identifiable information; or support other aspects of the information security and privacy policies. Privacy attributes may be used independently or in conjunction with security attributes.

**Organisation-defined parameters**

- `sc-16_prm_1` ()
- `sc-16_odp.01` (SC-16_ODP[01])
- `sc-16_odp.02` (SC-16_ODP[02])

**Related controls**: AC-3, AC-4, AC-16

**Enhancements** (3):

- **SC-16.1** — Integrity Verification
- **SC-16.2** — Anti-spoofing Mechanisms
- **SC-16.3** — Cryptographic Binding

### SC-17 — Public Key Infrastructure Certificates

**Statement (OSCAL)**

```
a. Issue public key certificates under an {{ insert: param, sc-17_odp }} or obtain public key certificates from an approved service provider; and
b. Include only approved trust anchors in trust stores or certificate stores managed by the organization.
```

**Guidance (OSCAL)**

> Public key infrastructure (PKI) certificates are certificates with visibility external to organizational systems and certificates related to the internal operations of systems, such as application-specific time services. In cryptographic systems with a hierarchical structure, a trust anchor is an authoritative source (i.e., a certificate authority) for which trust is assumed and not derived. A root certificate for a PKI system is an example of a trust anchor. A trust store or certificate store maintains a list of trusted root certificates.

**Organisation-defined parameters**

- `sc-17_odp` (SC-17_ODP)

**Related controls**: AU-10, IA-5, SC-12

### SC-18 — Mobile Code

**Statement (OSCAL)**

```
a. Define acceptable and unacceptable mobile code and mobile code technologies; and
b. Authorize, monitor, and control the use of mobile code within the system.
```

**Guidance (OSCAL)**

> Mobile code includes any program, application, or content that can be transmitted across a network (e.g., embedded in an email, document, or website) and executed on a remote system. Decisions regarding the use of mobile code within organizational systems are based on the potential for the code to cause damage to the systems if used maliciously. Mobile code technologies include Java applets, JavaScript, HTML5, WebGL, and VBScript. Usage restrictions and implementation guidelines apply to both the selection and use of mobile code installed on servers and mobile code downloaded and executed on individual workstations and devices, including notebook computers and smart phones. Mobile code policy and procedures address specific actions taken to prevent the development, acquisition, and introduction of unacceptable mobile code within organizational systems, including requiring mobile code to be digitally signed by a trusted source.

**Related controls**: AU-2, AU-12, CM-2, CM-6, SI-3

**Enhancements** (5):

- **SC-18.1** — Identify Unacceptable Code and Take Corrective Actions
- **SC-18.2** — Acquisition, Development, and Use
- **SC-18.3** — Prevent Downloading and Execution
- **SC-18.4** — Prevent Automatic Execution
- **SC-18.5** — Allow Execution Only in Confined Environments

### SC-20 — Secure Name/Address Resolution Service (Authoritative Source)

**Statement (OSCAL)**

```
a. Provide additional data origin authentication and integrity verification artifacts along with the authoritative name resolution data the system returns in response to external name/address resolution queries; and
b. Provide the means to indicate the security status of child zones and (if the child supports secure resolution services) to enable verification of a chain of trust among parent and child domains, when operating as part of a distributed, hierarchical namespace.
```

**Guidance (OSCAL)**

> Providing authoritative source information enables external clients, including remote Internet clients, to obtain origin authentication and integrity verification assurances for the host/service name to network address resolution information obtained through the service. Systems that provide name and address resolution services include domain name system (DNS) servers. Additional artifacts include DNS Security Extensions (DNSSEC) digital signatures and cryptographic keys. Authoritative data includes DNS resource records. The means for indicating the security status of child zones include the use of delegation signer resource records in the DNS. Systems that use technologies other than the DNS to map between host and service names and network addresses provide other means to assure the authenticity and integrity of response data.

**Related controls**: AU-10, SC-8, SC-12, SC-13, SC-21, SC-22

**Enhancements** (2):

- **SC-20.1** — Child Subspaces
- **SC-20.2** — Data Origin and Integrity

### SC-21 — Secure Name/Address Resolution Service (Recursive or Caching Resolver)

**Statement (OSCAL)**

```
Request and perform data origin authentication and data integrity verification on the name/address resolution responses the system receives from authoritative sources.
```

**Guidance (OSCAL)**

> Each client of name resolution services either performs this validation on its own or has authenticated channels to trusted validation providers. Systems that provide name and address resolution services for local clients include recursive resolving or caching domain name system (DNS) servers. DNS client resolvers either perform validation of DNSSEC signatures, or clients use authenticated channels to recursive resolvers that perform such validations. Systems that use technologies other than the DNS to map between host and service names and network addresses provide some other means to enable clients to verify the authenticity and integrity of response data.

**Related controls**: SC-20, SC-22

**Enhancements** (1):

- **SC-21.1** — Data Origin and Integrity

### SC-22 — Architecture and Provisioning for Name/Address Resolution Service

**Statement (OSCAL)**

```
Ensure the systems that collectively provide name/address resolution service for an organization are fault-tolerant and implement internal and external role separation.
```

**Guidance (OSCAL)**

> Systems that provide name and address resolution services include domain name system (DNS) servers. To eliminate single points of failure in systems and enhance redundancy, organizations employ at least two authoritative domain name system servers—one configured as the primary server and the other configured as the secondary server. Additionally, organizations typically deploy the servers in two geographically separated network subnetworks (i.e., not located in the same physical facility). For role separation, DNS servers with internal roles only process name and address resolution requests from within organizations (i.e., from internal clients). DNS servers with external roles only process name and address resolution information requests from clients external to organizations (i.e., on external networks, including the Internet). Organizations specify clients that can access authoritative DNS servers in certain roles (e.g., by address ranges and explicit lists).

**Related controls**: SC-2, SC-20, SC-21, SC-24

### SC-23 — Session Authenticity

**Statement (OSCAL)**

```
Protect the authenticity of communications sessions.
```

**Guidance (OSCAL)**

> Protecting session authenticity addresses communications protection at the session level, not at the packet level. Such protection establishes grounds for confidence at both ends of communications sessions in the ongoing identities of other parties and the validity of transmitted information. Authenticity protection includes protecting against "man-in-the-middle" attacks, session hijacking, and the insertion of false information into sessions.

**Related controls**: AU-10, SC-8, SC-10, SC-11

**Enhancements** (5):

- **SC-23.1** — Invalidate Session Identifiers at Logout
- **SC-23.2** — User-initiated Logouts and Message Displays
- **SC-23.3** — Unique System-generated Session Identifiers
- **SC-23.4** — Unique Session Identifiers with Randomization
- **SC-23.5** — Allowed Certificate Authorities

### SC-24 — Fail in Known State

**Statement (OSCAL)**

```
Fail to a {{ insert: param, sc-24_odp.02 }} for the following failures on the indicated components while preserving {{ insert: param, sc-24_odp.03 }} in failure: {{ insert: param, sc-24_odp.01 }}.
```

**Guidance (OSCAL)**

> Failure in a known state addresses security concerns in accordance with the mission and business needs of organizations. Failure in a known state prevents the loss of confidentiality, integrity, or availability of information in the event of failures of organizational systems or system components. Failure in a known safe state helps to prevent systems from failing to a state that may cause injury to individuals or destruction to property. Preserving system state information facilitates system restart and return to the operational mode with less disruption of mission and business processes.

**Organisation-defined parameters**

- `sc-24_odp.01` (SC-24_ODP[01])
- `sc-24_odp.02` (SC-24_ODP[02])
- `sc-24_odp.03` (SC-24_ODP[03])

**Related controls**: CP-2, CP-4, CP-10, CP-12, SA-8, SC-7, SC-22, SI-13

### SC-25 — Thin Nodes

**Statement (OSCAL)**

```
Employ minimal functionality and information storage on the following system components: {{ insert: param, sc-25_odp }}.
```

**Guidance (OSCAL)**

> The deployment of system components with minimal functionality reduces the need to secure every endpoint and may reduce the exposure of information, systems, and services to attacks. Reduced or minimal functionality includes diskless nodes and thin client technologies.

**Organisation-defined parameters**

- `sc-25_odp` (SC-25_ODP)

**Related controls**: SC-30, SC-44

### SC-26 — Decoys

**Statement (OSCAL)**

```
Include components within organizational systems specifically designed to be the target of malicious attacks for detecting, deflecting, and analyzing such attacks.
```

**Guidance (OSCAL)**

> Decoys (i.e., honeypots, honeynets, or deception nets) are established to attract adversaries and deflect attacks away from the operational systems that support organizational mission and business functions. Use of decoys requires some supporting isolation measures to ensure that any deflected malicious code does not infect organizational systems. Depending on the specific usage of the decoy, consultation with the Office of the General Counsel before deployment may be needed.

**Related controls**: RA-5, SC-7, SC-30, SC-35, SC-44, SI-3, SI-4

**Enhancements** (1):

- **SC-26.1** — Detection of Malicious Code

### SC-27 — Platform-independent Applications

**Statement (OSCAL)**

```
Include within organizational systems the following platform independent applications: {{ insert: param, sc-27_odp }}.
```

**Guidance (OSCAL)**

> Platforms are combinations of hardware, firmware, and software components used to execute software applications. Platforms include operating systems, the underlying computer architectures, or both. Platform-independent applications are applications with the capability to execute on multiple platforms. Such applications promote portability and reconstitution on different platforms. Application portability and the ability to reconstitute on different platforms increase the availability of mission-essential functions within organizations in situations where systems with specific operating systems are under attack.

**Organisation-defined parameters**

- `sc-27_odp` (SC-27_ODP)

**Related controls**: SC-29

### SC-28 — Protection of Information at Rest

**Statement (OSCAL)**

```
Protect the {{ insert: param, sc-28_odp.01 }} of the following information at rest: {{ insert: param, sc-28_odp.02 }}.
```

**Guidance (OSCAL)**

> Information at rest refers to the state of information when it is not in process or in transit and is located on system components. Such components include internal or external hard disk drives, storage area network devices, or databases. However, the focus of protecting information at rest is not on the type of storage device or frequency of access but rather on the state of the information. Information at rest addresses the confidentiality and integrity of information and covers user information and system information. System-related information that requires protection includes configurations or rule sets for firewalls, intrusion detection and prevention systems, filtering routers, and authentication information. Organizations may employ different mechanisms to achieve confidentiality and integrity protections, including the use of cryptographic mechanisms and file share scanning. Integrity protection can be achieved, for example, by implementing write-once-read-many (WORM) technologies. When adequate protection of information at rest cannot otherwise be achieved, organizations may employ other controls, including frequent scanning to identify malicious code at rest and secure offline storage in lieu of online storage.

**Organisation-defined parameters**

- `sc-28_odp.01` (SC-28_ODP[01])
- `sc-28_odp.02` (SC-28_ODP[02])

**Related controls**: AC-3, AC-4, AC-6, AC-19, CA-7, CM-3, CM-5, CM-6, CP-9, MP-4, MP-5, PE-3, SC-8, SC-12, SC-13, SC-34, SI-3, SI-7, SI-16

**Enhancements** (3):

- **SC-28.1** — Cryptographic Protection
- **SC-28.2** — Offline Storage
- **SC-28.3** — Cryptographic Keys

### SC-29 — Heterogeneity

**Statement (OSCAL)**

```
Employ a diverse set of information technologies for the following system components in the implementation of the system: {{ insert: param, sc-29_odp }}.
```

**Guidance (OSCAL)**

> Increasing the diversity of information technologies within organizational systems reduces the impact of potential exploitations or compromises of specific technologies. Such diversity protects against common mode failures, including those failures induced by supply chain attacks. Diversity in information technologies also reduces the likelihood that the means adversaries use to compromise one system component will be effective against other system components, thus further increasing the adversary work factor to successfully complete planned attacks. An increase in diversity may add complexity and management overhead that could ultimately lead to mistakes and unauthorized configurations.

**Organisation-defined parameters**

- `sc-29_odp` (SC-29_ODP)

**Related controls**: AU-9, PL-8, SC-27, SC-30, SR-3

**Enhancements** (1):

- **SC-29.1** — Virtualization Techniques

### SC-30 — Concealment and Misdirection

**Statement (OSCAL)**

```
Employ the following concealment and misdirection techniques for {{ insert: param, sc-30_odp.02 }} at {{ insert: param, sc-30_odp.03 }} to confuse and mislead adversaries: {{ insert: param, sc-30_odp.01 }}.
```

**Guidance (OSCAL)**

> Concealment and misdirection techniques can significantly reduce the targeting capabilities of adversaries (i.e., window of opportunity and available attack surface) to initiate and complete attacks. For example, virtualization techniques provide organizations with the ability to disguise systems, potentially reducing the likelihood of successful attacks without the cost of having multiple platforms. The increased use of concealment and misdirection techniques and methods—including randomness, uncertainty, and virtualization—may sufficiently confuse and mislead adversaries and subsequently increase the risk of discovery and/or exposing tradecraft. Concealment and misdirection techniques may provide additional time to perform core mission and business functions. The implementation of concealment and misdirection techniques may add to the complexity and management overhead required for the system.

**Organisation-defined parameters**

- `sc-30_odp.01` (SC-30_ODP[01])
- `sc-30_odp.02` (SC-30_ODP[02])
- `sc-30_odp.03` (SC-30_ODP[03])

**Related controls**: AC-6, SC-25, SC-26, SC-29, SC-44, SI-14

**Enhancements** (5):

- **SC-30.1** — Virtualization Techniques
- **SC-30.2** — Randomness
- **SC-30.3** — Change Processing and Storage Locations
- **SC-30.4** — Misleading Information
- **SC-30.5** — Concealment of System Components

### SC-31 — Covert Channel Analysis

**Statement (OSCAL)**

```
a. Perform a covert channel analysis to identify those aspects of communications within the system that are potential avenues for covert {{ insert: param, sc-31_odp }} channels; and
b. Estimate the maximum bandwidth of those channels.
```

**Guidance (OSCAL)**

> Developers are in the best position to identify potential areas within systems that might lead to covert channels. Covert channel analysis is a meaningful activity when there is the potential for unauthorized information flows across security domains, such as in the case of systems that contain export-controlled information and have connections to external networks (i.e., networks that are not controlled by organizations). Covert channel analysis is also useful for multilevel secure systems, multiple security level systems, and cross-domain systems.

**Organisation-defined parameters**

- `sc-31_odp` (SC-31_ODP)

**Related controls**: AC-3, AC-4, SA-8, SI-11

**Enhancements** (3):

- **SC-31.1** — Test Covert Channels for Exploitability
- **SC-31.2** — Maximum Bandwidth
- **SC-31.3** — Measure Bandwidth in Operational Environments

### SC-32 — System Partitioning

**Statement (OSCAL)**

```
Partition the system into {{ insert: param, sc-32_odp.01 }} residing in separate {{ insert: param, sc-32_odp.02 }} domains or environments based on {{ insert: param, sc-32_odp.03 }}.
```

**Guidance (OSCAL)**

> System partitioning is part of a defense-in-depth protection strategy. Organizations determine the degree of physical separation of system components. Physical separation options include physically distinct components in separate racks in the same room, critical components in separate rooms, and geographical separation of critical components. Security categorization can guide the selection of candidates for domain partitioning. Managed interfaces restrict or prohibit network access and information flow among partitioned system components.

**Organisation-defined parameters**

- `sc-32_odp.01` (SC-32_ODP[01])
- `sc-32_odp.02` (SC-32_ODP[02])
- `sc-32_odp.03` (SC-32_ODP[03])

**Related controls**: AC-4, AC-6, SA-8, SC-2, SC-3, SC-7, SC-36

**Enhancements** (1):

- **SC-32.1** — Separate Physical Domains for Privileged Functions

### SC-34 — Non-modifiable Executable Programs

**Statement (OSCAL)**

```
For {{ insert: param, sc-34_odp.01 }} , load and execute:
```

**Guidance (OSCAL)**

> The operating environment for a system contains the code that hosts applications, including operating systems, executives, or virtual machine monitors (i.e., hypervisors). It can also include certain applications that run directly on hardware platforms. Hardware-enforced, read-only media include Compact Disc-Recordable (CD-R) and Digital Versatile Disc-Recordable (DVD-R) disk drives as well as one-time, programmable, read-only memory. The use of non-modifiable storage ensures the integrity of software from the point of creation of the read-only image. The use of reprogrammable, read-only memory can be accepted as read-only media provided that integrity can be adequately protected from the point of initial writing to the insertion of the memory into the system, and there are reliable hardware protections against reprogramming the memory while installed in organizational systems.

**Organisation-defined parameters**

- `sc-34_odp.01` (SC-34_ODP[01])
- `sc-34_odp.02` (SC-34_ODP[02])

**Related controls**: AC-3, SI-7, SI-14

**Enhancements** (3):

- **SC-34.1** — No Writable Storage
- **SC-34.2** — Integrity Protection on Read-only Media
- **SC-34.3** — Hardware-based Protection

### SC-35 — External Malicious Code Identification

**Statement (OSCAL)**

```
Include system components that proactively seek to identify network-based malicious code or malicious websites.
```

**Guidance (OSCAL)**

> External malicious code identification differs from decoys in [SC-26](#sc-26) in that the components actively probe networks, including the Internet, in search of malicious code contained on external websites. Like decoys, the use of external malicious code identification techniques requires some supporting isolation measures to ensure that any malicious code discovered during the search and subsequently executed does not infect organizational systems. Virtualization is a common technique for achieving such isolation.

**Related controls**: SC-7, SC-26, SC-44, SI-3, SI-4

### SC-36 — Distributed Processing and Storage

**Statement (OSCAL)**

```
Distribute the following processing and storage components across multiple {{ insert: param, sc-36_prm_1 }}: {{ insert: param, sc-36_prm_2 }}.
```

**Guidance (OSCAL)**

> Distributing processing and storage across multiple physical locations or logical domains provides a degree of redundancy or overlap for organizations. The redundancy and overlap increase the work factor of adversaries to adversely impact organizational operations, assets, and individuals. The use of distributed processing and storage does not assume a single primary processing or storage location. Therefore, it allows for parallel processing and storage.

**Organisation-defined parameters**

- `sc-36_prm_1` ()
- `sc-36_prm_2` ()
- `sc-36_odp.01` (SC-36_ODP[01])
- `sc-36_odp.02` (SC-36_ODP[02])
- `sc-36_odp.03` (SC-36_ODP[03])
- `sc-36_odp.04` (SC-36_ODP[04])

**Related controls**: CP-6, CP-7, PL-8, SC-32

**Enhancements** (2):

- **SC-36.1** — Polling Techniques
- **SC-36.2** — Synchronization

### SC-37 — Out-of-band Channels

**Statement (OSCAL)**

```
Employ the following out-of-band channels for the physical delivery or electronic transmission of {{ insert: param, sc-37_odp.02 }} to {{ insert: param, sc-37_odp.03 }}: {{ insert: param, sc-37_odp.01 }}.
```

**Guidance (OSCAL)**

> Out-of-band channels include local, non-network accesses to systems; network paths physically separate from network paths used for operational traffic; or non-electronic paths, such as the U.S. Postal Service. The use of out-of-band channels is contrasted with the use of in-band channels (i.e., the same channels) that carry routine operational traffic. Out-of-band channels do not have the same vulnerability or exposure as in-band channels. Therefore, the confidentiality, integrity, or availability compromises of in-band channels will not compromise or adversely affect the out-of-band channels. Organizations may employ out-of-band channels in the delivery or transmission of organizational items, including authenticators and credentials; cryptographic key management information; system and data backups; configuration management changes for hardware, firmware, or software; security updates; maintenance information; and malicious code protection updates. For example, cryptographic keys for encrypted files are delivered using a different channel than the file.

**Organisation-defined parameters**

- `sc-37_odp.01` (SC-37_ODP[01])
- `sc-37_odp.02` (SC-37_ODP[02])
- `sc-37_odp.03` (SC-37_ODP[03])

**Related controls**: AC-2, CM-3, CM-5, CM-7, IA-2, IA-4, IA-5, MA-4, SC-12, SI-3, SI-4, SI-7

**Enhancements** (1):

- **SC-37.1** — Ensure Delivery and Transmission

### SC-38 — Operations Security

**Statement (OSCAL)**

```
Employ the following operations security controls to protect key organizational information throughout the system development life cycle: {{ insert: param, sc-38_odp }}.
```

**Guidance (OSCAL)**

> Operations security (OPSEC) is a systematic process by which potential adversaries can be denied information about the capabilities and intentions of organizations by identifying, controlling, and protecting generally unclassified information that specifically relates to the planning and execution of sensitive organizational activities. The OPSEC process involves five steps: identification of critical information, analysis of threats, analysis of vulnerabilities, assessment of risks, and the application of appropriate countermeasures. OPSEC controls are applied to organizational systems and the environments in which those systems operate. OPSEC controls protect the confidentiality of information, including limiting the sharing of information with suppliers, potential suppliers, and other non-organizational elements and individuals. Information critical to organizational mission and business functions includes user identities, element uses, suppliers, supply chain processes, functional requirements, security requirements, system design specifications, testing and evaluation protocols, and security control implementation details.

**Organisation-defined parameters**

- `sc-38_odp` (SC-38_ODP)

**Related controls**: CA-2, CA-7, PL-1, PM-9, PM-12, RA-2, RA-3, RA-5, SC-7, SR-3, SR-7

### SC-39 — Process Isolation

**Statement (OSCAL)**

```
Maintain a separate execution domain for each executing system process.
```

**Guidance (OSCAL)**

> Systems can maintain separate execution domains for each executing process by assigning each process a separate address space. Each system process has a distinct address space so that communication between processes is performed in a manner controlled through the security functions, and one process cannot modify the executing code of another process. Maintaining separate execution domains for executing processes can be achieved, for example, by implementing separate address spaces. Process isolation technologies, including sandboxing or virtualization, logically separate software and firmware from other software, firmware, and data. Process isolation helps limit the access of potentially untrusted software to other system resources. The capability to maintain separate execution domains is available in commercial operating systems that employ multi-state processor technologies.

**Related controls**: AC-3, AC-4, AC-6, AC-25, SA-8, SC-2, SC-3, SI-16

**Enhancements** (2):

- **SC-39.1** — Hardware Separation
- **SC-39.2** — Separate Execution Domain Per Thread

### SC-40 — Wireless Link Protection

**Statement (OSCAL)**

```
Protect external and internal {{ insert: param, sc-40_prm_1 }} from the following signal parameter attacks: {{ insert: param, sc-40_prm_2 }}.
```

**Guidance (OSCAL)**

> Wireless link protection applies to internal and external wireless communication links that may be visible to individuals who are not authorized system users. Adversaries can exploit the signal parameters of wireless links if such links are not adequately protected. There are many ways to exploit the signal parameters of wireless links to gain intelligence, deny service, or spoof system users. Protection of wireless links reduces the impact of attacks that are unique to wireless systems. If organizations rely on commercial service providers for transmission services as commodity items rather than as fully dedicated services, it may not be possible to implement wireless link protections to the extent necessary to meet organizational security requirements.

**Organisation-defined parameters**

- `sc-40_prm_1` ()
- `sc-40_prm_2` ()
- `sc-40_odp.01` (SC-40_ODP[01])
- `sc-40_odp.02` (SC-40_ODP[02])
- `sc-40_odp.03` (SC-40_ODP[03])
- `sc-40_odp.04` (SC-40_ODP[04])

**Related controls**: AC-18, SC-5

**Enhancements** (4):

- **SC-40.1** — Electromagnetic Interference
- **SC-40.2** — Reduce Detection Potential
- **SC-40.3** — Imitative or Manipulative Communications Deception
- **SC-40.4** — Signal Parameter Identification

### SC-41 — Port and I/O Device Access

**Statement (OSCAL)**

```
{{ insert: param, sc-41_odp.02 }} disable or remove {{ insert: param, sc-41_odp.01 }} on the following systems or system components: {{ insert: param, sc-41_odp.03 }}.
```

**Guidance (OSCAL)**

> Connection ports include Universal Serial Bus (USB), Thunderbolt, and Firewire (IEEE 1394). Input/output (I/O) devices include compact disc and digital versatile disc drives. Disabling or removing such connection ports and I/O devices helps prevent the exfiltration of information from systems and the introduction of malicious code from those ports or devices. Physically disabling or removing ports and/or devices is the stronger action.

**Organisation-defined parameters**

- `sc-41_odp.01` (SC-41_ODP[01])
- `sc-41_odp.02` (SC-41_ODP[02])
- `sc-41_odp.03` (SC-41_ODP[03])

**Related controls**: AC-20, MP-7

### SC-42 — Sensor Capability and Data

**Statement (OSCAL)**

```
a. Prohibit {{ insert: param, sc-42_odp.01 }} ; and
b. Provide an explicit indication of sensor use to {{ insert: param, sc-42_odp.05 }}.
```

**Guidance (OSCAL)**

> Sensor capability and data applies to types of systems or system components characterized as mobile devices, such as cellular telephones, smart phones, and tablets. Mobile devices often include sensors that can collect and record data regarding the environment where the system is in use. Sensors that are embedded within mobile devices include microphones, cameras, Global Positioning System (GPS) mechanisms, and accelerometers. While the sensors on mobiles devices provide an important function, if activated covertly, such devices can potentially provide a means for adversaries to learn valuable information about individuals and organizations. For example, remotely activating the GPS function on a mobile device could provide an adversary with the ability to track the movements of an individual. Organizations may prohibit individuals from bringing cellular telephones or digital cameras into certain designated facilities or controlled areas within facilities where classified information is stored or sensitive conversations are taking place.

**Organisation-defined parameters**

- `sc-42_odp.01` (SC-42_ODP[01])
- `sc-42_odp.02` (SC-42_ODP[02])
- `sc-42_odp.03` (SC-42_ODP[03])
- `sc-42_odp.04` (SC-42_ODP[04])
- `sc-42_odp.05` (SC-42_ODP[05])

**Related controls**: SC-15

**Enhancements** (5):

- **SC-42.1** — Reporting to Authorized Individuals or Roles
- **SC-42.2** — Authorized Use
- **SC-42.3** — Prohibit Use of Devices
- **SC-42.4** — Notice of Collection
- **SC-42.5** — Collection Minimization

### SC-43 — Usage Restrictions

**Statement (OSCAL)**

```
a. Establish usage restrictions and implementation guidelines for the following system components: {{ insert: param, sc-43_odp }} ; and
b. Authorize, monitor, and control the use of such components within the system.
```

**Guidance (OSCAL)**

> Usage restrictions apply to all system components including but not limited to mobile code, mobile devices, wireless access, and wired and wireless peripheral components (e.g., copiers, printers, scanners, optical devices, and other similar technologies). The usage restrictions and implementation guidelines are based on the potential for system components to cause damage to the system and help to ensure that only authorized system use occurs.

**Organisation-defined parameters**

- `sc-43_odp` (SC-43_ODP)

**Related controls**: AC-18, AC-19, CM-6, SC-7, SC-18

### SC-44 — Detonation Chambers

**Statement (OSCAL)**

```
Employ a detonation chamber capability within {{ insert: param, sc-44_odp }}.
```

**Guidance (OSCAL)**

> Detonation chambers, also known as dynamic execution environments, allow organizations to open email attachments, execute untrusted or suspicious applications, and execute Universal Resource Locator requests in the safety of an isolated environment or a virtualized sandbox. Protected and isolated execution environments provide a means of determining whether the associated attachments or applications contain malicious code. While related to the concept of deception nets, the employment of detonation chambers is not intended to maintain a long-term environment in which adversaries can operate and their actions can be observed. Rather, detonation chambers are intended to quickly identify malicious code and either reduce the likelihood that the code is propagated to user environments of operation or prevent such propagation completely.

**Organisation-defined parameters**

- `sc-44_odp` (SC-44_ODP)

**Related controls**: SC-7, SC-18, SC-25, SC-26, SC-30, SC-35, SC-39, SI-3, SI-7

### SC-45 — System Time Synchronization

**Statement (OSCAL)**

```
Synchronize system clocks within and between systems and system components.
```

**Guidance (OSCAL)**

> Time synchronization of system clocks is essential for the correct execution of many system services, including identification and authentication processes that involve certificates and time-of-day restrictions as part of access control. Denial of service or failure to deny expired credentials may result without properly synchronized clocks within and between systems and system components. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. The granularity of time measurements refers to the degree of synchronization between system clocks and reference clocks, such as clocks synchronizing within hundreds of milliseconds or tens of milliseconds. Organizations may define different time granularities for system components. Time service can be critical to other security capabilities—such as access control and identification and authentication—depending on the nature of the mechanisms used to support the capabilities.

**Related controls**: AC-3, AU-8, IA-2, IA-8

**Enhancements** (2):

- **SC-45.1** — Synchronization with Authoritative Time Source
- **SC-45.2** — Secondary Authoritative Time Source

### SC-46 — Cross Domain Policy Enforcement

**Statement (OSCAL)**

```
Implement a policy enforcement mechanism {{ insert: param, sc-46_odp }} between the physical and/or network interfaces for the connecting security domains.
```

**Guidance (OSCAL)**

> For logical policy enforcement mechanisms, organizations avoid creating a logical path between interfaces to prevent the ability to bypass the policy enforcement mechanism. For physical policy enforcement mechanisms, the robustness of physical isolation afforded by the physical implementation of policy enforcement to preclude the presence of logical covert channels penetrating the security domain may be needed. Contact [ncdsmo@nsa.gov](mailto:ncdsmo@nsa.gov) for more information.

**Organisation-defined parameters**

- `sc-46_odp` (SC-46_ODP)

**Related controls**: AC-4, SC-7

### SC-47 — Alternate Communications Paths

**Statement (OSCAL)**

```
Establish {{ insert: param, sc-47_odp }} for system operations organizational command and control.
```

**Guidance (OSCAL)**

> An incident, whether adversarial- or nonadversarial-based, can disrupt established communications paths used for system operations and organizational command and control. Alternate communications paths reduce the risk of all communications paths being affected by the same incident. To compound the problem, the inability of organizational officials to obtain timely information about disruptions or to provide timely direction to operational elements after a communications path incident, can impact the ability of the organization to respond to such incidents in a timely manner. Establishing alternate communications paths for command and control purposes, including designating alternative decision makers if primary decision makers are unavailable and establishing the extent and limitations of their actions, can greatly facilitate the organization’s ability to continue to operate and take appropriate actions during an incident.

**Organisation-defined parameters**

- `sc-47_odp` (SC-47_ODP)

**Related controls**: CP-2, CP-8

### SC-48 — Sensor Relocation

**Statement (OSCAL)**

```
Relocate {{ insert: param, sc-48_odp.01 }} to {{ insert: param, sc-48_odp.02 }} under the following conditions or circumstances: {{ insert: param, sc-48_odp.03 }}.
```

**Guidance (OSCAL)**

> Adversaries may take various paths and use different approaches as they move laterally through an organization (including its systems) to reach their target or as they attempt to exfiltrate information from the organization. The organization often only has a limited set of monitoring and detection capabilities, and they may be focused on the critical or likely infiltration or exfiltration paths. By using communications paths that the organization typically does not monitor, the adversary can increase its chances of achieving its desired goals. By relocating its sensors or monitoring capabilities to new locations, the organization can impede the adversary’s ability to achieve its goals. The relocation of the sensors or monitoring capabilities might be done based on threat information that the organization has acquired or randomly to confuse the adversary and make its lateral transition through the system or organization more challenging.

**Organisation-defined parameters**

- `sc-48_odp.01` (SC-48_ODP[01])
- `sc-48_odp.02` (SC-48_ODP[02])
- `sc-48_odp.03` (SC-48_ODP[03])

**Related controls**: AU-2, SC-7, SI-4

**Enhancements** (1):

- **SC-48.1** — Dynamic Relocation of Sensors or Monitoring Capabilities

### SC-49 — Hardware-enforced Separation and Policy Enforcement

**Statement (OSCAL)**

```
Implement hardware-enforced separation and policy enforcement mechanisms between {{ insert: param, sc-49_odp }}.
```

**Guidance (OSCAL)**

> System owners may require additional strength of mechanism and robustness to ensure domain separation and policy enforcement for specific types of threats and environments of operation. Hardware-enforced separation and policy enforcement provide greater strength of mechanism than software-enforced separation and policy enforcement.

**Organisation-defined parameters**

- `sc-49_odp` (SC-49_ODP)

**Related controls**: AC-4, SA-8, SC-50

### SC-50 — Software-enforced Separation and Policy Enforcement

**Statement (OSCAL)**

```
Implement software-enforced separation and policy enforcement mechanisms between {{ insert: param, sc-50_odp }}.
```

**Guidance (OSCAL)**

> System owners may require additional strength of mechanism to ensure domain separation and policy enforcement for specific types of threats and environments of operation.

**Organisation-defined parameters**

- `sc-50_odp` (SC-50_ODP)

**Related controls**: AC-3, AC-4, SA-8, SC-2, SC-3, SC-49

### SC-51 — Hardware-based Protection

**Statement (OSCAL)**

```
a. Employ hardware-based, write-protect for {{ insert: param, sc-51_odp.01 }} ; and
b. Implement specific procedures for {{ insert: param, sc-51_odp.02 }} to manually disable hardware write-protect for firmware modifications and re-enable the write-protect prior to returning to operational mode.
```

**Guidance (OSCAL)**

> None.

**Organisation-defined parameters**

- `sc-51_odp.01` (SC-51_ODP[01])
- `sc-51_odp.02` (SC-51_ODP[02])

