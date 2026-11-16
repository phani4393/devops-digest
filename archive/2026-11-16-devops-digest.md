# DevOps Digest — 2026-11-16

> Cybersecurity · AI News & Tools · DevSecOps · SRE
> Generated 2026-11-16 05:54 UTC

## 🛡️ Cybersecurity

### 🔴 ACT · 1. [Attackers Exploit UnrealIRCd Flaw That Enables Server-Level Command Injection](https://thehackernews.com/2026/11/attackers-exploit-unrealircd-flaw-that.html)
*The Hacker News* · 2026-11-14

Cybersecurity and Infrastructure Security Agency (CISA) on Friday added a high-severity security flaw impacting UnrealIRCd, an open-source Internet Relay Chat (IRC) server, to its Known Exploited Vulnerabilities (KEV) catalog, following reports of active exploitation. The vulnerability, tracked as CVE-2026-114713 (CVSS score: 8.6), is a case of improper neutralization of delimiters

**🎯 Why it matters:** Time-sensitive: likely needs a decision or action soon.

**LinkedIn angle:** Security teams: here's what this means for your threat model.

<sub>matched: cisa, cve-, cvss, exploit, vulnerabilities, vulnerability</sub>

### 🟡 WATCH · 2. [Hackers Exploit PHP2Shell Flaws in Check Point Gateways to Deploy TSGA Backdoor and Wipe ESXi Files](https://thehackernews.com/2026/11/hackers-exploit-php2shell-flaws-in.html)
*The Hacker News* · 2026-11-13

An unknown threat actor has been observed targeting unpatched Check Point Security Gateways to obtain initial access via the PHP2Shell vulnerabilities and then a previously unreported local privilege escalation flaw in Gaia OS to deploy a backdoor called TSGA. The activity, detailed by Check Point, began on October 30, 2026, and targeted Israeli organizations, with a broader follow-up

**🎯 Why it matters:** Worth a scan if you own patching or security posture.

**LinkedIn angle:** A reminder that the attack surface keeps shifting — here's the takeaway.

<sub>matched: backdoor, exploit, privilege escalation, threat actor, vulnerabilities</sub>

### 🔴 ACT · 3. [CISA Adds Two Known Exploited Vulnerabilities to Catalog](https://www.cisa.gov/news-events/alerts/2026/11/13/cisa-adds-two-known-exploited-vulnerabilities-catalog)
*CISA Advisories* · 2026-11-13

CISA has added two new vulnerabilities to its Known Exploited Vulnerabilities (KEV) Catalog , based on evidence of active exploitation. BOD 26-04 reinforces the importance of the KEV Catalog and requires federal agencies to prioritize rapid remediation of high-risk vulnerabilities, specifically those identified by Common Vulnerabilities and Exposures (CVEs) listed in CISA’s KEV Catalog on publicly exposed assets that grant total control of the asset post-exploitation, while deferring action for lower-risk vulnerabilities.

**🎯 Why it matters:** Time-sensitive: likely needs a decision or action soon.

**LinkedIn angle:** If you own security posture, this is worth a 2-minute read.

<sub>matched: cisa, cve-, vulnerabilities, vulnerability</sub>

### 🟡 WATCH · 4. [Critical Zoom Workplace Flaw Could Allow Unauthenticated Remote Privilege Escalation](https://thehackernews.com/2026/11/critical-zoom-workplace-flaw-could.html)
*The Hacker News* · 2026-11-11

Zoom has released software updates to address two security flaws impacting Zoom Workplace for Windows, including a critical bug that could result in privilege escalation on affected systems. The vulnerabilities are listed below - CVE-2026-108186 (CVSS score: 9.6) - An improper input validation vulnerability that could allow an unauthenticated user to conduct an escalation of privilege via

**🎯 Why it matters:** Signals where attacker attention is heading next.

**LinkedIn angle:** If you own security posture, this is worth a 2-minute read.

<sub>matched: cve-, cvss, privilege escalation, vulnerabilities, vulnerability</sub>

### 🟡 WATCH · 5. [Attackers Exploit AhsayCBS Flaws to Deploy Sandbox-Evading Python Backdoor](https://thehackernews.com/2026/11/attackers-exploit-ahsaycbs-flaws-to.html)
*The Hacker News* · 2026-11-10

Cybersecurity researchers have disclosed details of an attack that exploited two now-patched vulnerabilities in AhsayCBS to deliver a Python-based implant. Patches for the two

**🎯 Why it matters:** Worth a scan if you own patching or security posture.

**LinkedIn angle:** A reminder that the attack surface keeps shifting — here's the takeaway.

<sub>matched: backdoor, cve-, exploit, vulnerabilities</sub>

## 🤖 AI News & Tools

### 🟡 WATCH · 1. [llm-gemini 0.36](https://simonwillison.net/2026/Nov/10/llm-gemini/)
*Simon Willison* · 2026-11-10

Here are three pelicans for the low, medium and high thinking efforts (it defaults to medium). I then screen-captured that as a video: Update : Huh, just saw this on YouTube (and tweeted by Google CEO Sundar Pichai ): Using Google Antigravity’s /swarm feature, Carbon built an open-world 3D game where you explore Google’s

**🎯 Why it matters:** Changes what's possible (or cheaper) in your AI tooling.

**LinkedIn angle:** The AI tooling landscape moved again — here's why it matters for builders.

<sub>matched: claude, gemini, gpt, llm, prompt</sub>

### 🟡 WATCH · 2. [datasette-llm 0.1a11](https://simonwillison.net/2026/Nov/14/datasette-llm/)
*Simon Willison* · 2026-11-14

Release: datasette-llm 0.1a11 datasette-llm is the intermediate plugin for Datasette that supports configuring LLMs for use with other Datasette plugins. Tags: uv , datasette-agent , llm , datasette , llms , ai , generative-ai

**🎯 Why it matters:** A shift in the LLM/agent stack worth tracking for your builds.

**LinkedIn angle:** Another signal that the way we ship software is changing.

<sub>matched: agent, llama, llm, ollama, openai</sub>

### 🔴 ACT · 3. [Anthropic's IPO roadshow video](https://simonwillison.net/2026/Nov/11/anthropic-ipo-roadshow/)
*Simon Willison* · 2026-11-11

Anthropic's IPO roadshow video Anthropic kicked off their IPO roadshow yesterday, and their roadshow video has some previously unreleased information about how their business works. [...] As an example, this year, we started working with AMD GPUs for the first time.

**🎯 Why it matters:** Touches your AWS stack — likely actionable, not just interesting.

**LinkedIn angle:** Directly relevant to AWS work — a strong hook for a post tying this to real-world AWS experience.

<sub>matched: anthropic, claude, inference</sub>

### 🟡 WATCH · 4. [Anthropic’s Claude Fable 5.2 built a shooter in 1 prompt — and it only took 8 hours and $550](https://thenewstack.io/claude-fable-game-demos/)
*The New Stack* · 2026-11-11

An Anthropic engineer gave Claude Fable 5.2 one prompt to build a first-person shooter and let it run for eight The post Anthropic’s Claude Fable 5.2 built a shooter in 1 prompt — and it only took 8 hours and $550 appeared first on The New Stack .

**🎯 Why it matters:** May alter how you wire AI into real workflows.

**LinkedIn angle:** Worth bookmarking if you're wiring AI into real workflows.

<sub>matched: anthropic, claude, prompt</sub>

### 🟡 WATCH · 5. [Don’t just prompt AI — architect it: Introducing the Professional Agentic Architect Certification](https://cloud.google.com/blog/topics/training-certifications/google-cloud-agentic-architect-certification-dont-just-prompt-ai-design-it/)
*Google Cloud Blog* · 2026-11-11

Today, Google Cloud is introducing the Professional Agentic Architect certification as the latest milestone in our Gemini Agent Ready (GEAR) initiative. New Google Cloud Agentic A

**🎯 Why it matters:** Changes what's possible (or cheaper) in your AI tooling.

**LinkedIn angle:** The AI tooling landscape moved again — here's why it matters for builders.

<sub>matched: agent, agentic, gemini, prompt</sub>

## 🔐 DevSecOps

### 🔴 ACT · 1. [From insight to action: improving infrastructure risk posture with Terraform and Concert](https://www.hashicorp.com/blog/from-insight-to-action-improving-infrastructure-risk-posture-with-terraform-and-c)
*HashiCorp Blog* · 2026-11-10

Learn how Terraform and IBM Concert connect trusted infrastructure context, policy-driven governance, and vulnerability management to improve risk posture across the infrastructure lifecycle.

**🎯 Why it matters:** Touches your Terraform stack — likely actionable, not just interesting.

**LinkedIn angle:** Directly relevant to Terraform work — a strong hook for a post tying this to real-world Terraform experience.

<sub>matched: terraform, vulnerability</sub>

### 🔴 ACT · 2. [AWS Emulator proves agents need a verification loop. Realism is the hard part.](https://thenewstack.io/aws-emulator-verification-loops/)
*The New Stack* · 2026-11-14

This week, Amazon Web Services released AWS Emulator, a local copy of AWS that coding agents can test against. It The post AWS Emulator proves agents need a verification loop.

**🎯 Why it matters:** Touches your AWS stack — likely actionable, not just interesting.

**LinkedIn angle:** Directly relevant to AWS work — a strong hook for a post tying this to real-world AWS experience.

### 🔴 ACT · 3. [Ease of use and secure defaults in the new AWS experience](https://aws.amazon.com/blogs/security/ease-of-use-and-secure-defaults-in-the-new-aws-experience/)
*AWS Security Blog* · 2026-11-11

Starting on Amazon Web Services (AWS) is now more straightforward and more secure by default than it’s ever been. It brings together a set of sensible, secure defaults, and taken one at a time, it’s easy to […]

**🎯 Why it matters:** Touches your AWS stack — likely actionable, not just interesting.

**LinkedIn angle:** Directly relevant to AWS work — a strong hook for a post tying this to real-world AWS experience.

### 🔴 ACT · 4. [AWS had its agents build a free and open emulator for AWS. They now maintain it, too.](https://thenewstack.io/aws-emulator-ai-agents/)
*The New Stack* · 2026-11-11

AWS on Wednesday launched an emulator for AWS called AWS Emulator. That, by itself, is interesting and may raise some The post AWS had its agents build a free and open emulator for AWS.

**🎯 Why it matters:** Touches your AWS stack — likely actionable, not just interesting.

**LinkedIn angle:** Directly relevant to AWS work — a strong hook for a post tying this to real-world AWS experience.

### 🔴 ACT · 5. [AWS refreshes ProcessUnity Global Risk Exchange assessment to enhance customer’s third-party due diligence](https://aws.amazon.com/blogs/security/aws-refreshes-processunity-global-risk-exchange-assessment-to-enhance-customers-third-party-due-diligence/)
*AWS Security Blog* · 2026-11-10

Amazon Web Services (AWS) is pleased to announce renewal of the AWS ProcessUnity Global Risk Exchange assessment. What is the AWS ProcessUnity Global Risk Exchange assessment Many customers use third-party cyber risk management (TPCRM) […]

**🎯 Why it matters:** Touches your AWS stack — likely actionable, not just interesting.

**LinkedIn angle:** Directly relevant to AWS work — a strong hook for a post tying this to real-world AWS experience.

## 📈 SRE / Reliability

### 🔴 ACT · 1. [Detect and respond to PHP2Shell with Datadog](https://www.datadoghq.com/blog/detect-respond-php2shell-datadog/)
*Datadog Blog* · 2026-11-10

Learn how to identify vulnerable PHP deployments, prioritize patching, detect exploitation attempts, and investigate PHP2Shell activity with Datadog Security.

**🎯 Why it matters:** Touches your Datadog stack — likely actionable, not just interesting.

**LinkedIn angle:** Directly relevant to Datadog work — a strong hook for a post tying this to real-world Datadog experience.

<sub>matched: datadog</sub>

### 🔴 ACT · 2. [Monitor OCI workloads in US government clouds with Datadog](https://www.datadoghq.com/blog/monitor-oci-government-cloud-datadog/)
*Datadog Blog* · 2026-11-10

Datadog for Government supports monitoring for Oracle Cloud Infrastructure workloads across US Government Cloud (OC2) and US Defense Cloud (OC3).

**🎯 Why it matters:** Touches your Datadog stack — likely actionable, not just interesting.

**LinkedIn angle:** Directly relevant to Datadog work — a strong hook for a post tying this to real-world Datadog experience.

<sub>matched: datadog</sub>

### 🔴 ACT · 3. [Monitor and troubleshoot employee devices with Datadog End User Device Monitoring](https://www.datadoghq.com/blog/end-user-device-monitoring/)
*Datadog Blog* · 2026-11-10

Catch degrading devices before employees file tickets, trace issues across devices and networks, and resolve recurring problems with Datadog End User Device Monitoring.

**🎯 Why it matters:** Touches your Datadog stack — likely actionable, not just interesting.

**LinkedIn angle:** Directly relevant to Datadog work — a strong hook for a post tying this to real-world Datadog experience.

<sub>matched: datadog</sub>

### ⚪ FYI · 4. [Coles hit by a cybersecurity incident](https://www.colesgroup.com.au/updates/)
*Hacker News* · 2026-11-16 · 82 pts

Coles hit by a cybersecurity incident

**🎯 Why it matters:** Useful for on-call load, SLOs, or observability cost.

**LinkedIn angle:** Reliability is a feature. Here's a pattern worth stealing.

<sub>matched: incident</sub>

### 🔴 ACT · 5. [Investigate the person behind the risk with Cloud SIEM](https://www.datadoghq.com/blog/cloud-siem-investigate-user-entity-risks/)
*Datadog Blog* · 2026-11-13

Learn how to connect security signals to users, investigate linked account risks, and prioritize threats with Entity Risks in Datadog Cloud SIEM.

**🎯 Why it matters:** Touches your Datadog stack — likely actionable, not just interesting.

**LinkedIn angle:** Directly relevant to Datadog work — a strong hook for a post tying this to real-world Datadog experience.

<sub>matched: datadog</sub>


---
*20 items · DevOps Digest*