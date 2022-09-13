# workatastartup-api

This api uses [NixOs](https://nixos.org/) to install the dependencies, first [follow their instructions to install](https://nixos.org/download.html#download-nix).

### Install

To install, run the following commands.

```
git@github.com:jwc20/workatastartup-api.git
cd workatastartup-api
nix-build
```

### Usage

To use the api, run the nix shell (or venv).

```
nix-shell
```

Inside the shell, you can run the example.py.

### Log In

Set your username and password.

```
username = "example_username"
password = "example_password"
```

Once set, create a client and log in using the following method.

```
client = waasu.WorkAtAStartUp()
client.log_in(username=username, password=password)
```

### Scrape

To scrape for companies, you can add queries (keywords) and add additional filter parameters.

```
query = ["python", "javascript", "data", "typescript"]
client.get_companies(query=query, jobType="contract", role="eng", scroll_delay=10)


#=> [
#     {
#         'about': 'Our mission is to take cars off the road by making it safe and easy to vanpool in the post Covid world.',
#         'company_url': 'magicbus.io',
#         'founders': ['Jason Kraft', 'Chris Upjohn'],
#         'jobs': [
#             {
#                 'details': 'Remote fulltime  Visa Required 3+ years',
#                 'job_name': 'Software Developer - DevOps',
#                 'job_url': 'https://www.workatastartup.com/jobs/43098',
#             },
#             {
#                 'details': 'Remote contract 6+ years',
#                 'job_name': 'Software Developer - Frontend',
#                 'job_url': 'https://www.workatastartup.com/jobs/16340',
#             },
#         ],
#         'location': 'Los Angeles, CA',
#         'name': 'MagicBus',
#         'size': '18 people',
#         'tech': "We're working on problems related to geospatial route optimization, machine learning, and natural language processing in addition to mobile web and app development.",
#         'waasu_url': 'https://www.workatastartup.com/companies/magicbus',
#     },
#     {
#         'about': "Tenjin manages mobile growth infrastructure for our clients by organizing, analyzing, and securing the rush of data generated by mobile devices and marketing channels. We're reshaping mobile marketing by breaking down data silos and building an integrated data platform to replace the detached services in use today.",
#         'company_url': 'tenjin.com',
#         ...
# ]
```

### Optional Filters

```
hasEquity=("any", "true", "false") ("any" same as "false")
demographic=("any", "black-founders", "women-founders", "latinx-founders")
hasSalary=("any", "true", "false")
industry=("any", "B2B Software and Services", "Consumer", "Education", "Healthcare", "Financial Technology and Services", "Real Estate and Construction", "Industrials", "Government", "Unspecified")
interviewProcess=("any", "true", "false")
jobType=("any", "fulltime", "contract", "intern")
remote=("any", "only", "yes", "no")
sortBy=("keyword"(default), "recommended", "most_active", "created_desc", "company_created_desc", "size", "size_desc", "name", "name_desc")
usVisaNotRequired=("any", "true", "false")
query=query
companySize=("any", "seed", "small", "medium", "large")
expo=("any")
```

#### Roles Filters

For some roles, there are addtional role_type filters.

```
role=("any", "eng", "design", "product", "science", "sales", "marketing", "support", "recruiting", "operations", "finance", "legal")

# role_type
"eng" => role_type=("android", "be", "data_sci", "devops", "embedded", "eng_mgmt", "fe", "ios", "fs", "ml", "robotics", "qa", "electrical", "hw", "mechanical", "bio", "chemical")
"design" => role_type("web", "mobile", "ui_ux", "brand_graphic", "animation", "hardware", "user_research", "illustration", "ar_vr", "design_mgmt")
"science" => role_type("bio", "biotech", "chem", "genetics", "health", "immuno", "lab", "onc", "pharma", "process", "research")
```

### Dependencies

```
beautifulsoup4
lxml
requests
selenium
pprintpp
```

### See Also

- [hnjobs](https://hnjobs.emilburzo.com/)
- [Who Is Hiring?](https://kennytilton.github.io/whoishiring/)
- [hn_search](https://news.ycombinator.com/item?id=10313519)

### TODO

- [x] **_(high)_** Add filtering.
- [x] **_(high)_** Get company details and available jobs from the companies search result.
- [ ] **_(medium)_** Add scroll down feature.
- [ ] **_(low)_** Convert job details into dictionary. (?)
- [ ] **_(medium)_** Add "(New Grads Ok)" option.
- [ ] **_(high)_** Add export to csv feature.
- [ ] **_(medium)_** Add more to README instructions.
- [ ] **_(low)_** AND and OR support for queries. [(Example)](https://news.ycombinator.com/item?id=10313519)
- [ ] **_(medium)_** Add role type filter parameter.
- [ ] **_(high)_** Return total number of search result and jobs available.

### FIXME

~~**_(low)_** Fix log in url~~ \
 ~~**_(low)_** Fix scroll down timer, display the total time (?).~~\
~~**_(high)_** Fix search query url.~~

- [ ] **_(high)_** Get all texts for "about". (See d["about"] in companies.py)
- [ ] **_(high)_** Use typing.
- [ ] **_(high)_** Query not using all element in the list.

