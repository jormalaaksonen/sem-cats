# sem-cats

Semantic categories of adpositions in the English and Finnish languages.

This repository relates to the book:

Pirkko Suihkonen & Jorma Laaksonen (2023): Syntax and Semantics of
Adpositions and Case Marking: Description of Prepositions in English
and Adpositions and Case Marking in Finnish within the Framework of a
Parallel Database. LINCOM Studies in Theoretical Linguistics. ISBN
978-3-96939-171-6. 332 pages.


## 1 directories

`script` - The Perl scripts used in the data-driven analysis.

`spec` - Specifications of the linguistic rules.

`data` - The used data.


## 2 data

## 3 example runs

For all example runs, do first:

```
cd script
```

### 3.1 setup verification

```
./kwic -verify
```

The output should be like:

<blockquote>
Perl version v5.36.0 in /usr/bin/perl<br>
Verifying locale "en_US.UTF-8" ... good<br>
Verifying bug #12989 ... IS corrected<br>
Verifying <../spec/fin.spec><br>
&nbsp;&nbsp; Including <../spec/fin-disamb-ESS.spec><br>
&nbsp;&nbsp; ...<br>
Verifying <../spec/eng.spec><br>
&nbsp;&nbsp; Including list <../spec/eng-verbs.txt> as VERB-LIST and *undef*<br>
&nbsp;&nbsp; ...<br>
Verify ending<br>
</blockquote>

### 3.2 other runs

*TBW*


## 4 contacts

Jorma Laaksonen <<jorma.laaksonen@aalto.fi>>

## 5 copyright

© 2006–2024 Pirkko Suihkonen & Jorma Laaksonen



