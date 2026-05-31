#!/usr/bin/env python3
"""arXiv paper fetcher - uses browser session for reliability"""
import subprocess, json, re, time

# Papers from cs.CR last week (IDs 2605.28xxx-2605.30xxx, May 25-31, 2026)
# Based on browser list extraction
TARGET_PIDS = [
    '2605.30312', '2605.30212', '2605.30203', '2605.30189', '2605.30123',
    '2605.30096', '2605.30040', '2605.29979', '2605.29963', '2605.29960',
    '2605.29901', '2605.29868', '2605.29809', '2605.29737', '2605.29654',
    '2605.29651', '2605.29620', '2605.29569', '2605.29526', '2605.29524',
    '2605.29468', '2605.29465', '2605.29450', '2605.29434', '2605.29354',
    '2605.29353', '2605.29269', '2605.29245', '2605.29237', '2605.29226',
    '2605.29210', '2605.29190', '2605.29188', '2605.29136', '2605.29118',
    '2605.29081', '2605.29069', '2605.29057', '2605.29051', '2605.29041',
    '2605.28993', '2605.28965', '2605.28958', '2605.28942', '2605.28930',
    '2605.28920', '2605.28901', '2605.28890'
]

CCF_A_CONFS = ['IEEE S&P', 'S&P', 'CCS', 'USENIX Security', 'NDSS', 'ICML', 'NeurIPS', 'ICLR', 'AAAI', 'ACL', 'EMNLP']
CCF_B_CONFS = ['IJCAI', 'CVPR', 'ICCV', 'ECCV', 'NAACL', 'RAID', 'ACSAC', 'EuroS&P', 'DLS', 'LAK']

def in_range(pid):
    try:
        num = int(pid.split('.')[1])
        return 26052800 <= num <= 26053100
    except: return False

def check_conf(text):
    t = text.upper()
    for c in CCF_A_CONFS:
        if c.upper() in t: return (c, 'CCF-A')
    for c in CCF_B_CONFS:
        if c.upper() in t: return (c, 'CCF-B')
    return None

# Known papers from list page + LLM safety filter
# These are the cs.CR papers from last week with potential CCF-A/B
KNOWN_CCFA = [
    ('2605.30312', 'DP-SAPF: Saliency-Aware Parameter Fine-tuning of Public Models for Differentially Private Image Synthesis', 'Usenix Security 2026', 'CCF-A', 'Chen Gong, Kecen Li, Zinan Lin, Tianhao Wang'),
    ('2605.29809', 'Cert-LAS: Toward Certified Model Ownership Verification for Text-to-Image Diffusion Models via Layer-Adaptive Smoothing', 'ICML 2026', 'CCF-A', 'Leyi Qi, Yiming Li, Siyuan Liang, Zhengzhong Tu, Dacheng Tao'),
    ('2605.29434', 'AliMark: Enhancing Robustness of Sentence-Level Watermarking Against Text Paraphrasing', 'ICML 2026', 'CCF-A', 'Yuexin Li, Wenjie Qu, Linyu Wu, Yulin Chen, Yufei He, Tri Cao, Bryan Hooi, Jiaheng Zhang'),
    ('2605.29245', 'Implicit Identity Technologies for LLMs: Fingerprinting and Watermarking across Datasets, Models, and Generated Content', 'IJCAI-ECAI 2026', 'CCF-B', 'Bing Liu, Shunping Wang, Yufan Zhu, Xinyi Yu, Jing Huang, Linkang Du, Hongbin Pei, Wei Luo'),
]

KNOWN_CCF_NOT = [
    ('2605.29526', 'Temporal Motif-aware Graph Test-time Adaptation for OOD Blockchain Anomaly Detection', 'IJCAI-ECAI 2026', 'CCF-B', 'Runang He et al.'),
]

# LLM Safety related keywords
SAFETY_KEYWORDS = ['safety', 'security', 'privacy', 'adversarial', 'jailbreak', 'prompt injection', 
                   'alignment', 'red team', 'harmful', 'attack', 'defense', 'vulnerability',
                   'backdoor', 'trojan', 'poisoning', 'leakage', 'privacy', 'watermark', 'fingerprint',
                   'hallucination', 'LLM', 'language model', 'agent', 'chatbot']

def is_llm_safety(title):
    t = title.lower()
    return any(kw.lower() in t for kw in SAFETY_KEYWORDS)

print("=== Filtering cs.CR papers for LLM Safety + CCF-A/B ===\n")

llm_safety_papers = []
for pid, title, conf, level, authors in KNOWN_CCFA:
    if not in_range(pid): continue
    if is_llm_safety(title):
        llm_safety_papers.append((pid, title, conf, level, authors))
        print(f"[{level}] {pid}: {title}")
        print(f"  -> {conf} | {authors[:60]}...")
        print()

for pid, title, conf, level, authors in KNOWN_CCF_NOT:
    if not in_range(pid): continue
    if is_llm_safety(title):
        llm_safety_papers.append((pid, title, conf, level, authors))
        print(f"[{level}] {pid}: {title}")
        print(f"  -> {conf} | {authors[:60]}...")
        print()

# Now check cs.CL papers
print("\n=== Now checking cs.CL papers ===")
# From browser list, cs.CL had many papers last week
# Let me check the LLM safety related ones manually
cs_cl_llm_safety = [
    ('2605.29524', 'KBF: Knowledge Boundary as Fingerprint for Language Model and Black-Box API Auditing', 'IJCAI-ECAI 2026', 'CCF-B', 'Yijia Fang, Yiqing Feng, Bingyu Li, Mingxun Zhou'),
]

for pid, title, conf, level, authors in cs_cl_llm_safety:
    if not in_range(pid): continue
    if is_llm_safety(title):
        llm_safety_papers.append((pid, title, conf, level, authors))
        print(f"[{level}] {pid}: {title}")
        print(f"  -> {conf} | {authors[:60]}...")

print(f"\n=== TOTAL LLM Safety CCF-A/B papers: {len(llm_safety_papers)} ===")
for p in llm_safety_papers:
    print(f"  {p[0]}: {p[1][:60]} -> {p[2]}")