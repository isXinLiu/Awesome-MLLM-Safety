json_file = "data.json"
md_file = "README.md"

import json

prefix_str = (
    "# MLLM-Safety-Collection\n"
    "A collection of papers related to safety of Multimodal Large Language Models (MLLMs).\n\n"
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
    "<table>\n"
    "  <tr>\n"
    "    <th>Date</th>\n"
    "    <th>Notes</th>\n"
    "    <th>Title</th>\n"
    "  </tr>\n"
)

mid_str = (
    "</table>\n\n"
    "## Others\n"
    "<table>\n"
    "  <tr>\n"
    "    <th>Date</th>\n"
    "    <th>Notes</th>\n"
    "    <th>Title</th>\n"
    "  </tr>\n"
)

suffix_str = (
    "</table>\n"
)

paper_str_template = (
    "  <tr>\n"
    "    <td>{paper_date}</td>\n"
    "    <td>{paper_notes}</td>\n"
    "    <td><a href='{paper_link}' target='_blank'>{paper_title}</a></td>\n"
    "  </tr>\n"
)

if __name__ == "__main__":
    with open(json_file, "r") as jf:
        json_data = json.load(jf)
    with open(md_file,"w+") as mf:
        pass
    with open(md_file,"a+") as mf:
        mf.write(prefix_str)
        for paper in json_data['Main']:
            paper_str = paper_str_template.format(
                paper_date=paper['Date'],
                paper_notes=paper['Notes'],
                paper_link=paper['Link'],
                paper_title=paper['Title']
            )
            mf.write(paper_str)
        mf.write(mid_str)
        for paper in json_data['Other']:
            paper_str = paper_str_template.format(
                paper_date=paper['Date'],
                paper_notes=paper['Notes'],
                paper_link=paper['Link'],
                paper_title=paper['Title']
            )
            mf.write(paper_str)
        mf.write(suffix_str)
