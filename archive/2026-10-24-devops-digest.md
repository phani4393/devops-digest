# DevOps Digest — 2026-10-24

> Cybersecurity · AI News & Tools · DevSecOps · SRE
> Generated 2026-10-24 04:03 UTC

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

### 3. [Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor](https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/)
*Hacker News* · 2026-10-21 · 593 pts

Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor

**LinkedIn angle:** Security teams: here's what this means for your threat model.

<sub>matched: backdoor, credential</sub>

### 4. [CISA Adds One Known Exploited Vulnerability to Catalog](https://www.cisa.gov/news-events/alerts/2026/10/23/cisa-adds-one-known-exploited-vulnerability-catalog-0)
*CISA Advisories* · 2026-10-23

CISA has added one new vulnerability to its Known Exploited Vulnerabilities (KEV) Catalog , based on evidence of active exploitation. While BOD 26-04 applies only to FCEB agencies, CISA encourages all organizations to adopt risk-based

**LinkedIn angle:** A reminder that the attack surface keeps shifting — here's the takeaway.

<sub>matched: cisa, cve-, vulnerabilities, vulnerability</sub>

### 5. [CISA Adds One Known Exploited Vulnerability to Catalog](https://www.cisa.gov/news-events/alerts/2026/10/23/cisa-adds-one-known-exploited-vulnerability-catalog)
*CISA Advisories* · 2026-10-23

CISA has added one new vulnerability to its Known Exploited Vulnerabilities (KEV) Catalog , based on evidence of active exploitation. While BOD 26-04 applies only to FCEB agencies, CISA encourages all organizations to adopt risk-based vulnerability man

**LinkedIn angle:** If you own security posture, this is worth a 2-minute read.

<sub>matched: cisa, cve-, vulnerabilities, vulnerability</sub>

## 🤖 AI News & Tools

### 1. [Donating Agent Skills to the Agentic AI Foundation](https://simonwillison.net/2026/Oct/22/donating-agent-skills/)
*Simon Willison* · 2026-10-23

Donating Agent Skills to the Agentic AI Foundation News today from Anthropic: We’re committed to keeping Agent Skills open, community-driven, and vendor-neutral. Tags: standards , ai , generative-ai , llms , anthropic , model-context-protocol , skills

**LinkedIn angle:** Another signal that the way we ship software is changing.

<sub>matched: agent, agentic, anthropic, claude, mcp, model context protocol, openai</sub>

### 2. [OpenAI donates Open Responses, its spec for a common LLM API, to the Agentic AI Foundation](https://thenewstack.io/openai-donates-open-responses/)
*The New Stack* · 2026-10-22

OpenAI on Thursday announced that it is donating the Open Responses API specification to the open source Agentic AI Foundation The post OpenAI donates Open Responses, its spec for a common LLM API, to the Agentic AI Foundation appeared first on The New Stack .

**LinkedIn angle:** The AI tooling landscape moved again — here's why it matters for builders.

<sub>matched: agentic, llm, openai</sub>

### 3. [OpenAI's GPT-6 Agent Removed Safety Monitoring, Then Falsely Denied Doing So](https://thehackernews.com/2026/10/openais-gpt-6-agent-removed-safety.html)
*The Hacker News* · 2026-10-21

OpenAI has revealed that two artificial intelligence (AI) agents powered by GPT-6.1 Sol and GPT-6 Astra weakened misalignment monitoring while making requested software changes during two internal coding tasks. "A GPT-6.1 Sol agent repairing an evaluation

**LinkedIn angle:** Another signal that the way we ship software is changing.

<sub>matched: agent, gpt, incident, openai</sub>

### 4. [Introducing Kimi K3.1 Pro](https://simonwillison.net/2026/Oct/23/kimi-k31-pro/)
*Simon Willison* · 2026-10-24

Introducing Kimi K3.1 Pro landed on the Kimi API today - it's not yet open weights, but Moonshot promise "Full model weights will be released by Nov 4, 2026". Artificial Analysis scored Kimi at 55 - ahead of Claude Fable 5.1, GPT-6 Astra, and Gemini 4 Argon (all at 53) and behind only Claude Opus 5.5 (58).

**LinkedIn angle:** Worth bookmarking if you're wiring AI into real workflows.

<sub>matched: claude, gemini, gpt, llm, openai</sub>

### 5. [DeepInfer: High-performance inference framework for DeepSeek models](https://github.com/deepseek-ai/DeepInfer)
*Hacker News* · 2026-10-20 · 2342 pts

DeepInfer: High-performance inference framework for DeepSeek models

**LinkedIn angle:** Another signal that the way we ship software is changing.

<sub>matched: inference</sub>

## 🔐 DevSecOps

### 1. [Enforcing SAST and DAST Tools at Enterprise Level](https://www.reddit.com/r/devops/comments/1xcyyiv/enforcing_sast_and_dast_tools_at_enterprise_level/)
*r/devops* · 2026-10-23

Hi All, It has been my experience at a couple of different organizations that almost all engineering teams own their own CI/CD pipelines. This is my own personal research and drive to understand being a cloud security engineer.

**LinkedIn angle:** Supply-chain and IaC security keep maturing. Here's the practical angle.

<sub>matched: ci/cd, dast, iac, sast, snyk, trivy</sub>

### 2. [Suggest me any project in AWS with Terraform!](https://www.reddit.com/r/devops/comments/1xdfrgt/suggest_me_any_project_in_aws_with_terraform/)
*r/devops* · 2026-10-23

Give me Realtime project which currently company standards. Thanks submitted by /u/Sea_Mechanic815 [link] [comments]

**LinkedIn angle:** Directly relevant to AWS/Terraform work — a strong hook for a post tying this to real-world AWS/Terraform experience.

<sub>matched: sre, terraform</sub>

### 3. [How to learn devops quickly?](https://www.reddit.com/r/devops/comments/1xc8nf3/how_to_learn_devops_quickly/)
*r/devops* · 2026-10-22

I've been teaching myself DevOps for the past few months and I've hit a wall where I'm not sure if I'm actually making progress or just hoarding tutorials. I've built a few Docker images and used docker-compose for local setups.

**LinkedIn angle:** Directly relevant to Terraform work — a strong hook for a post tying this to real-world Terraform experience.

<sub>matched: ci/cd, terraform</sub>

### 4. [Beyond container image signing: How we enforce software supply chain policies at Datadog](https://www.datadoghq.com/blog/engineering/software-supply-chain-policy-enforcement/)
*Datadog Blog* · 2026-10-20

Datadog built Turnstile to evaluate signed attestations and enforce software supply chain policies before container images are deployed.

**LinkedIn angle:** Directly relevant to Datadog work — a strong hook for a post tying this to real-world Datadog experience.

<sub>matched: datadog, supply chain</sub>

### 5. [Google and AWS open new paths for PyTorch beyond Nvidia](https://thenewstack.io/pytorch-tpu-trainium-migration/)
*The New Stack* · 2026-10-22

At PyTorch Conference North America 2026 this week, Google open-sourced TorchTPU, a native PyTorch stack for Google TPUs, now available The post Google and AWS open new paths for PyTorch beyond Nvidia appeared first on The New Stack .

**LinkedIn angle:** Directly relevant to AWS work — a strong hook for a post tying this to real-world AWS experience.

## 📈 SRE / Reliability

### 1. [What does AI-assisted incident investigation actually look like at your company right now?](https://www.reddit.com/r/devops/comments/1xdcnxa/what_does_aiassisted_incident_investigation/)
*r/devops* · 2026-10-23

It'd help if you mention your stack (Datadog, Grafana, other) Thanks! submitted by /u/Commercial_Plastic72 [link] [comments]

**LinkedIn angle:** Directly relevant to Datadog work — a strong hook for a post tying this to real-world Datadog experience.

<sub>matched: datadog, grafana, incident</sub>

### 2. [I'm a one man DevOps team and my production runs for $0.64 a day. Here's the real story.](https://www.reddit.com/r/devops/comments/1xcpuj4/im_a_one_man_devops_team_and_my_production_runs/)
*r/devops* · 2026-10-23

Six small machines in total. Small RDS is $13.

**LinkedIn angle:** Directly relevant to AWS work — a strong hook for a post tying this to real-world AWS experience.

<sub>matched: prometheus</sub>

### 3. [Spend less time on operational busywork and resolve incidents faster with Grafana Workflows](https://grafana.com/blog/spend-less-time-on-operational-busywork-and-resolve-incidents-faster-with-grafana-workflows/)
*Grafana Blog* · 2026-10-21

Grafana Workflows , available in public preview, turns your team’s processes into automated steps across Grafana Cloud and your other tools. Get

**LinkedIn angle:** For the on-call crowd: a useful take on keeping systems healthy.

<sub>matched: grafana, incident, runbook</sub>

### 4. [ObservabilityCON 2026: A guide to all the announcements from Grafana Labs](https://grafana.com/blog/observabilitycon-2026-announcements/)
*Grafana Blog* · 2026-10-20

Today at ObservabilityCON 2026 in San Francisco, we unveiled a range of new Grafana Cloud capabilities designed to reshape cloud economics, bring richer context and deeper visibility across your systems and end-user experiences, and help teams move toward autonomous operations. Autonomous operations with the help of AI With Grafana Assistant in Grafana Cloud, you can bring more of your operational tasks together in one place so you can resolve incidents faster and get back to building.

**LinkedIn angle:** Reliability is a feature. Here's a pattern worth stealing.

<sub>matched: agent, agentic, grafana, incident, mcp, observability</sub>

### 5. [Break the link between data volume and your observability bill with Adaptive Telemetry](https://grafana.com/blog/cut-costs-keep-what-you-need-adaptive-telemetry/)
*Grafana Blog* · 2026-10-20

Your costs shouldn't scale with how much data you ingest. That’s what Adaptive Telemetry is built for, and organizations such as Rapid7 are already seeing the results.

**LinkedIn angle:** Observability and SLOs done right — a quick field note.

<sub>matched: agent, grafana, incident, observability</sub>


---
*20 items · DevOps Digest*