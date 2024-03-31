json_file = "data.json"
md_file = "README.md"

import json

prefix_str = (
    "# Awesome-MLLM-Safety\n"
    "A **continual** collection of papers related to safety of Multimodal Large Language Models (MLLMs).\n\n"
    "<details>\n"
    "  <summary>The scope of our collection.</summary>\n"
    "  <ul>\n"
    "    <li>\n"
    "      We follow the definition of safety from the paper <b><q>Safety-Tuned LLaMAs: Lessons From Improving the Safety of Large Language Models that Follow Instructions</q></b>: <blockquote>Safety is defined as stopping models from following malicious instructions and generating toxic content.</blockquote>\n"
    "    </li>\n"
    "    <li>\n"
    "      Therefore, robustness-related wrong prediction and downstream applications (e.g., robotic/medical/legal/financial domains, anomalies detection, fake news detection) are not involved.\n"
    "    </li>\n"
    "    <li>\n"
    "      We care about the safety of <b>MLLMs</b>, excluding other models like text-to-image models.\n"
    "    </li>\n"
    "    <li>\n"
    "      We mainly focus on <b>images and text</b>, and few about other modalities like audio and videos.\n"
    "    </li>\n"
    "  </ul>\n"
    "</details>\n\n\n"
    "> If you find some important work missed, it would be super helpful to let me know (`isXinLiu@gmail.com`). Thanks!\n\n"
    "> If you find our survey useful for your research, please consider citing:\n\n"
    "```\n"
    "@article{liu:arxiv2024,\n"
    "  title={Safety of Multimodal Large Language Models on Images and Text},\n"
    "  author={Liu, Xin and Zhu, Yichen and Lan, Yunshi and Yang, Chao and Qiao, Yu},\n"
    "  journal={arXiv preprint arXiv:2402.00357},\n"
    "  year={2024}\n"
    "}\n"
    "```\n\n"
    "Common terminologies related to safety:\n"
    "<img src='./assets/terminology.jpeg' width='100%'>\n"
    "Taxonomy----safety of MLLMs on images and text:\n"
    "<img src='./assets/taxonomy.jpg' width='100%'>\n\n"
    "**Table of Contents**\n"
    "- [Benchmark(Evaluation)](#Benchmark)\n"
    "- [Attack](#Attack)\n"
    "- [Defense](#Defense)\n"
    "- [Other](#Other)\n"
    "---\n\n"
)

paper_str_template = (
    "* **{paper_title}**\n"
    "  * {paper_author}\n"
    "  * {paper_affiliation}\n"
    "  * [{paper_date}] {paper_link}\n"
    "  * {paper_notes}\n"
)

paper_str_template_code = (
    "* **{paper_title}** | [Github]({paper_code_link}) ![Star](https://img.shields.io/github/stars/{paper_code_keyphrase}.svg?style=social&label=Star)\n"
    "  * {paper_author}\n"
    "  * {paper_affiliation}\n"
    "  * [{paper_date}] {paper_link}\n"
    "  * {paper_notes}\n"
)

def get_paper_str(paper):
    if paper['Code'] == "":
        paper_str = paper_str_template.format(
                    paper_date=paper['Date'],
                    paper_notes=paper['Notes'],
                    paper_link=paper['Link'],
                    paper_title=paper['Title'],
                    paper_author=paper['Author'],
                    paper_affiliation=paper['Affiliation'],
                )
    else:
        paper_str = paper_str_template_code.format(
                    paper_date=paper['Date'],
                    paper_notes=paper['Notes'],
                    paper_link=paper['Link'],
                    paper_title=paper['Title'],
                    paper_author=paper['Author'],
                    paper_affiliation=paper['Affiliation'],
                    paper_code_link=paper['Code'],
                    paper_code_keyphrase=paper['Code'].split('github.com/')[1]
                )
    return paper_str

if __name__ == "__main__":
    with open(json_file, "r") as jf:
        json_data = json.load(jf)
    with open(md_file,"w+") as mf:
        pass
    with open(md_file,"a+") as mf:
        mf.write(prefix_str)
        mf.write("## Benchmark\n")
        for paper in json_data['Main']:
            if 'benchmark' not in paper['Notes'].lower():
                continue
            paper_str = get_paper_str(paper)
            mf.write(paper_str)
        
        mf.write("## Attack\n")
        for paper in json_data['Main']:
            if 'attack' not in paper['Notes'].lower():
                continue
            paper_str = get_paper_str(paper)
            mf.write(paper_str)
        
        mf.write("## Defense\n")
        for paper in json_data['Main']:
            if 'defense' not in paper['Notes'].lower():
                continue
            paper_str = get_paper_str(paper)
            mf.write(paper_str)
        
        mf.write("## Other\n")
        for paper in json_data['Main']:
            if 'benchmark' in paper['Notes'].lower():
                continue
            if 'attack' in paper['Notes'].lower():
                continue
            if 'defense' in paper['Notes'].lower():
                continue
            paper_str = get_paper_str(paper)
            mf.write(paper_str)
