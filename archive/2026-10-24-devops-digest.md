# DevOps Digest — 2026-10-24

> Cybersecurity · AI News & Tools · DevSecOps · SRE
> Generated 2026-10-24 03:09 UTC

## 🛡️ Cybersecurity

### 1. [PHP2Shell Exploit Attempts Hit Millions as Attackers Try to Deploy Mirai Malware](https://thehackernews.com/2026/10/php2shell-exploit-attempts-hit-millions.html)
*The Hacker News* · 2026-10-23

Threat actors have been observed unsuccessfully attempting to exploit the newly disclosed PHP2Shell vulnerabilities to rope infected systems into a Mirai botnet variant called Potassium, as it emerges that weaponizing the flaws may be harder than previously thought. The attacks aim to exploit CVE-2026-109618 and CVE-2026-109619 (CVSS scores: 9.2), which can result in unauthenticated remote

**LinkedIn angle:** A reminder that the attack surface keeps shifting — here's the takeaway.

<sub>matched: botnet, cve-, cvss, exploit, malware, vulnerabilities</sub>

### 2. [Using AWS WAF to apply mitigations for PHP2Shell RCE vulnerabilities (CVE-2026-109618 and CVE-2026-109619)](https://aws.amazon.com/blogs/security/using-aws-waf-to-apply-mitigations-for-php2shell-rce-vulnerabilities-cve-2026-109618-and-cve-2026-109619/)
*AWS Security Blog* · 2026-10-22

October 23, 2026-2: The PHP project disclosed CVE-2026-115560, a separate remote code execution issue that the October 21 releases don’t fix. The PHP2Shell_BODY rule in the PHP application managed rule group, version 2.4 and later, already blocks POST requests that carry […]

**LinkedIn angle:** Directly relevant to AWS work — a strong hook for a post tying this to real-world AWS experience.

<sub>matched: cve-, rce, vulnerabilities</sub>

### 3. [CISA Adds One Known Exploited Vulnerability to Catalog](https://www.cisa.gov/news-events/alerts/2026/10/23/cisa-adds-one-known-exploited-vulnerability-catalog-0)
*CISA Advisories* · 2026-10-23

CISA has added one new vulnerability to its Known Exploited Vulnerabilities (KEV) Catalog , based on evidence of active exploitation. While BOD 26-04 applies only to FCEB agencies, CISA encourages all organizations to adopt risk-based

**LinkedIn angle:** A reminder that the attack surface keeps shifting — here's the takeaway.

<sub>matched: cisa, cve-, vulnerabilities, vulnerability</sub>

### 4. [CISA Adds One Known Exploited Vulnerability to Catalog](https://www.cisa.gov/news-events/alerts/2026/10/23/cisa-adds-one-known-exploited-vulnerability-catalog)
*CISA Advisories* · 2026-10-23

CISA has added one new vulnerability to its Known Exploited Vulnerabilities (KEV) Catalog , based on evidence of active exploitation. While BOD 26-04 applies only to FCEB agencies, CISA encourages all organizations to adopt risk-based vulnerability man

**LinkedIn angle:** If you own security posture, this is worth a 2-minute read.

<sub>matched: cisa, cve-, vulnerabilities, vulnerability</sub>

### 5. [LiteLLM Compromised in Supply Chain Attack Delivering Credential Stealer and Backdoor](https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html)
*The Hacker News* · 2026-10-21

The popular LiteLLM Python package has been compromised as part of a software supply chain attack that delivered a credential stealer and a backdoor, according to reports from SafeDep, Socket, StepSecurity, and Upwind. The Python package has since been quarantined on Python Package Index (PyPI), and the

**LinkedIn angle:** Security teams: here's what this means for your threat model.

<sub>matched: backdoor, credential, supply chain, supply chain attack</sub>

## 🤖 AI News & Tools

### 1. [Donating Agent Skills to the Agentic AI Foundation](https://simonwillison.net/2026/Oct/22/donating-agent-skills/)
*Simon Willison* · 2026-10-22

Donating Agent Skills to the Agentic AI Foundation News today from Anthropic: We’re committed to keeping Agent Skills open, community-driven, and vendor-neutral. Tags: standards , ai , generative-ai , llms , anthropic , model-context-protocol , skills

**LinkedIn angle:** Another signal that the way we ship software is changing.

<sub>matched: agent, agentic, anthropic, claude, mcp, model context protocol, openai</sub>

### 2. [Announcing llm-d 1.0: Open distributed inference for agents on Google Cloud TPUs and GPUs](https://cloud.google.com/blog/topics/ai-infrastructure/llm-d-1-0-an-open-source-stack-for-distributed-inference/)
*Google Cloud Blog* · 2026-10-20

Today at the PyTorch Conference, we released llm-d 1.0, an open-source, Kubernetes-native stack for distributed LLM inference. During the PyTorch Conference k

**LinkedIn angle:** Worth bookmarking if you're wiring AI into real workflows.

<sub>matched: agent, inference, llm, prompt</sub>

### 3. [OpenAI donates Open Responses, its spec for a common LLM API, to the Agentic AI Foundation](https://thenewstack.io/openai-donates-open-responses/)
*The New Stack* · 2026-10-22

OpenAI on Thursday announced that it is donating the Open Responses API specification to the open source Agentic AI Foundation The post OpenAI donates Open Responses, its spec for a common LLM API, to the Agentic AI Foundation appeared first on The New Stack .

**LinkedIn angle:** The AI tooling landscape moved again — here's why it matters for builders.

<sub>matched: agentic, llm, openai</sub>

### 4. [OpenAI's GPT-6 Agent Removed Safety Monitoring, Then Falsely Denied Doing So](https://thehackernews.com/2026/10/openais-gpt-6-agent-removed-safety.html)
*The Hacker News* · 2026-10-21

OpenAI has revealed that two artificial intelligence (AI) agents powered by GPT-6.1 Sol and GPT-6 Astra weakened misalignment monitoring while making requested software changes during two internal coding tasks. "A GPT-6.1 Sol agent repairing an evaluation

**LinkedIn angle:** Another signal that the way we ship software is changing.

<sub>matched: agent, gpt, incident, openai</sub>

### 5. [Managed RAG search inside the sovereign perimeter: Gemini on GDC enterprise search](https://cloud.google.com/blog/topics/hybrid-cloud/managed-rag-search-inside-the-sovereign-perimeter-gemini-on-gdc-enterprise-search/)
*Google Cloud Blog* · 2026-10-20

Search and multimodal intelligence that’s available in the public cloud can help teams manage and analyze that data, but due to strict data sovereignty mandates, that data cannot leave the customer premises. Your teams can now upload

**LinkedIn angle:** The AI tooling landscape moved again — here's why it matters for builders.

<sub>matched: agentic, gemini, rag, retrieval-augmented</sub>

## 🔐 DevSecOps

### 1. [Beyond container image signing: How we enforce software supply chain policies at Datadog](https://www.datadoghq.com/blog/engineering/software-supply-chain-policy-enforcement/)
*Datadog Blog* · 2026-10-20

Datadog built Turnstile to evaluate signed attestations and enforce software supply chain policies before container images are deployed.

**LinkedIn angle:** Directly relevant to Datadog work — a strong hook for a post tying this to real-world Datadog experience.

<sub>matched: datadog, supply chain</sub>

### 2. [Google and AWS open new paths for PyTorch beyond Nvidia](https://thenewstack.io/pytorch-tpu-trainium-migration/)
*The New Stack* · 2026-10-22

At PyTorch Conference North America 2026 this week, Google open-sourced TorchTPU, a native PyTorch stack for Google TPUs, now available The post Google and AWS open new paths for PyTorch beyond Nvidia appeared first on The New Stack .

**LinkedIn angle:** Directly relevant to AWS work — a strong hook for a post tying this to real-world AWS experience.

### 3. [Best practices for integrating IAM Roles Anywhere with your PKI](https://aws.amazon.com/blogs/security/best-practices-for-integrating-iam-roles-anywhere-with-your-pki/)
*AWS Security Blog* · 2026-10-21

With AWS IAM Roles Anywhere, now your workloads outside of Amazon Web Services (AWS) will be able to access AWS resources by obtaining temporary security credentials in AWS Identity and Access Management (IAM). IAM Roles Anywhere relies on public […]

**LinkedIn angle:** Directly relevant to AWS work — a strong hook for a post tying this to real-world AWS experience.

### 4. [Managing identity source transition for AWS IAM Identity Center](https://aws.amazon.com/blogs/security/managing-identity-source-transition-for-aws-iam-identity-center/)
*AWS Security Blog* · 2026-10-20

October 20, 2026: This post was republished to reflect the new migration capability from Active Directory to an external identity provider (IdP) or the Identity Center directory, now available in IAM Identity Center. AWS IAM Identity Center […]

**LinkedIn angle:** Directly relevant to AWS work — a strong hook for a post tying this to real-world AWS experience.

### 5. [AI jobs are waiting while GPUs sit idle. Kubernetes has a new plan.](https://thenewstack.io/kubernetes-agentic-ai-inference/)
*The New Stack* · 2026-10-23

Kubernetes has a new plan. appeared first on The New Stack .

**LinkedIn angle:** Supply-chain and IaC security keep maturing. Here's the practical angle.

## 📈 SRE / Reliability

### 1. [Spend less time on operational busywork and resolve incidents faster with Grafana Workflows](https://grafana.com/blog/spend-less-time-on-operational-busywork-and-resolve-incidents-faster-with-grafana-workflows/)
*Grafana Blog* · 2026-10-21

Grafana Workflows , available in public preview, turns your team’s processes into automated steps across Grafana Cloud and your other tools. Get

**LinkedIn angle:** For the on-call crowd: a useful take on keeping systems healthy.

<sub>matched: grafana, incident, runbook</sub>

### 2. [ObservabilityCON 2026: A guide to all the announcements from Grafana Labs](https://grafana.com/blog/observabilitycon-2026-announcements/)
*Grafana Blog* · 2026-10-20

Today at ObservabilityCON 2026 in San Francisco, we unveiled a range of new Grafana Cloud capabilities designed to reshape cloud economics, bring richer context and deeper visibility across your systems and end-user experiences, and help teams move toward autonomous operations. Autonomous operations with the help of AI With Grafana Assistant in Grafana Cloud, you can bring more of your operational tasks together in one place so you can resolve incidents faster and get back to building.

**LinkedIn angle:** Reliability is a feature. Here's a pattern worth stealing.

<sub>matched: agent, agentic, grafana, incident, mcp, observability</sub>

### 3. [Break the link between data volume and your observability bill with Adaptive Telemetry](https://grafana.com/blog/cut-costs-keep-what-you-need-adaptive-telemetry/)
*Grafana Blog* · 2026-10-20

Your costs shouldn't scale with how much data you ingest. That’s what Adaptive Telemetry is built for, and organizations such as Rapid7 are already seeing the results.

**LinkedIn angle:** Observability and SLOs done right — a quick field note.

<sub>matched: agent, grafana, incident, observability</sub>

### 4. [Full-stack observability in Grafana Cloud: More connections, richer context, and faster investigations for users and agents](https://grafana.com/blog/full-stack-observability-with-knowledge-graph/)
*Grafana Blog* · 2026-10-20

Critical context about service dependencies, ownership, and past incidents often lives across tools, runbooks, and conversations between team members. Powering this experience is the Knowledge Graph , the runtime context layer in Grafana Cloud that brings together your system's components, their relationships, and health insights in one connected view.

**LinkedIn angle:** Observability and SLOs done right — a quick field note.

<sub>matched: grafana, observability</sub>

### 5. [An alignment assessment of the UK AISI cybertesting incident](https://www.anthropic.com/research/alignment-assessment-ukaisi)
*Hacker News* · 2026-10-23 · 17 pts

An alignment assessment of the UK AISI cybertesting incident

**LinkedIn angle:** For the on-call crowd: a useful take on keeping systems healthy.

<sub>matched: incident</sub>


---
*20 items · DevOps Digest*