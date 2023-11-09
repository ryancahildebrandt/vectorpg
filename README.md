# VectoRPG

---

[*Open*](https://gitpod.io/#https://github.com/ryancahildebrandt/vectorpg) *in gitpod*

## *Purpose*

This is a simple command line utility that indexes text from pdfs (and one git repo), aimed primarily at tabletop role playing game playbooks and guides to serve as a quick reference during play. It stores text entries from pdf guides into a vector database (chromadb) in this case, and allows fast and easy document searches from a persistent command line prompt.

---

## Data Sources

Vectorpg is designed to read text directly from pdf files (or json in the case of Archives of Nethys) and includes a couple examples to get you started

- [Simple World](https://buriedwithoutceremony.com/wp-content/uploads/2017/07/simple-world.pdf)
- [Basic Fantasy RPG](https://basicfantasy.org/download.cgi/Basic-Fantasy-RPG-Rules-r107.pdf)
- [Archives of Nethys Scraper Repo](https://github.com/LukeHagar/archives-of-nethys-scraper)

---

## Usage

```bash
#clone vectorpg repo
git clone https://github.com/ryancahildebrandt/vectorpg.git
cd vectorpg
conda env create -f vectorpg_env.yml
conda activate vectorpg_env

#load example collections from pdf
python3 simple.py
python3 basic.py

#load pathfinder collection from scraper repo
git clone https://github.com/LukeHagar/archives-of-nethys-scraper.git archives-of-nethys-scraper
python3 pathfinder.py

#load new collection from local pdf file
python3 from_pdf.py -f "data/temp_gameguide.pdf" -c "temp_collection"

#show all cli options and arguments
python3 vectorpg.py -h

#connect to collection and return 3 results for each query
#collection names : simple2017, basicr107, pathfinder2e
python3 vectorpg.py -c "simple2017" -n 3

```

---

## Notes

- The Archives of Nethys scraper provides game guide information in json format, with keys and values corresponding to different pieces of information. For the pathfinder2e collection, I converted each key value pair to a simple sentence to facilitate embedding based lookup. This format is likely to be the best performing out of the examples provided
- Because the formatting on pdf game guides can vary so widely, the current utilities focus on extracting available text as simply as possible. As such, information from headings and tables isn't readily accessible via the vector database
