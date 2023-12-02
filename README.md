# literary-review-app


Creating a book review App
Part 1. Proposal
Team (Names): Vijayanand Kandasamy, Olusina Ojewola, and Andrew poppelaars.
Our objective is to create a book review app. Using sentiment analysis and the data sources, we will create an app that will allow users to search for books based on how positive or negative their scores are.
There are services and sites that can aggregate a meta review of books and show the average score of a book based on its reviews. We hope to use sentiment analysis to make it easier for users to see if a reviewer actually liked a book, rather than just deconstructing it in a critical manner. Book readers with limited time or money would find this app useful for finding a book worth their time and money.
Our data set is described as “a dataset with complete multilingual review text but without spoiler tags. This dataset is relatively large and contains more than 15[million] reviews about [2 million] books and 465[thousand] users.
The data can be [split] into different genres, and that can be useful to explore the data for different book genres (Children, Comics & Graphic, Fantasy & Paranormal,History & Biography, “Mystery, Thriller & Crime”, Poetry, Romance, and Young Adult).
The datasets were collected in late 2017 from goodreads.com, where they only scraped users' public shelves, i.e. everyone can see it on the web without login. UserIDs and review IDs are anonymized. The datasets were collected for academic use.”(Wan et al.)
We will be using NLP functions to clean the data, remove stop words, stem the text, and tokenize them.We will be pulling from the Sklearn and NLTK python libraries. As well as embedding the words using Word2Vec or GloVe. We will evaluate the best model to use by testing multiple model functions including LogisticRegression, SVM, and RNNS. We will then use NLP Functions to train, evaluate, and tune our chosen model.
User interaction with the app will allow the user to filter and search through the list of reviews for books predicted to fit their selected interests. For project planning, we will be communicating through the Discord platform, with our data being hosted on a github repository(Github link: https://github.com/oojewola/Literary-Review-App). Andrew Poppelaars drafted the Project proposal (tasks 1 through 3) for group review, Vijayanand researched and gathered the data sets, and Olusina established the github repository to host our code.
Works Cited
Wan, Mengting, et al. Fine-Grained Spoiler Detection from Large-Scale Review Corpora. 13 May 2019.
Wan, Mengting, and Julian McAuley. “Item Recommendation on Monotonic Behavior Chains.” Proceedings of the 12th ACM Conference on Recommender Systems, 27 Sept. 2018, https://doi.org/10.1145/3240323.3240369. Accessed 20 Oct. 2023. ‌
