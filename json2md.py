json_file = "data.json"
md_file = "README.md"

import json

prefix_str = (
    "# Awesome-MLLM-Safety\n"
    "A **continual** collection of papers related to safety of Multimodal Large Language Models (MLLMs).\n\n"
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
    "## Corresponding Papers (MLLM Safety)\n"
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

if __name__ == "__main__":
    with open(json_file, "r") as jf:
        json_data = json.load(jf)
    with open(md_file,"w+") as mf:
        pass
    with open(md_file,"a+") as mf:
        mf.write(prefix_str)
        for paper in json_data['Main']:
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
            mf.write(paper_str)
