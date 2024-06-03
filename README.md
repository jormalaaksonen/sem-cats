# sem-cats

**Semantic categories of prepositions in English and case marking and adpositions in Finnish**

This repository relates to the book:

Pirkko Suihkonen & Jorma Laaksonen (2024): Syntax and Semantics of
Adpositions and Case Marking: Description of Prepositions in English
and Adpositions and Case Marking in Finnish within the Framework of a
Parallel Database. LINCOM Studies in Theoretical Linguistics. ISBN
978-3-96939-171-6. 332 pages.


## 1 directories

`script` - The Perl scripts used in the data-driven analysis.

`spec` - Specifications of the linguistic rules.

`data` - The used data.


## 2 data

The input data consists of the Finnish and English translations of the Holy Bible. The Finnish translation is from the 1933 (the Old Testament) and 1938 (the New Testament) of The Finnish Church Bible. The English translation is the Project Gutenberg edition of the King James Bible (Second Version, 10th Edition) published in 1611.

The books of each translation have been stored in separate files.  The naming of the files follows the pattern `38-<NN>-<BB>` for the Finnish books and `eng-<NN>-<BB>` for the English ones.  Here, `<NN>` is a two-digit numerical index of the books (from 01 to 39 in the Old Testament and from 40 to 66 in the New Testament) and `<BB>` is a two-letter acronym for the book (e.g. "gn" for Genesis and "rv" for Revelation) common in both languages.  The input file names do not have any extensions.

The character encoding of the books in English is ASCII.  The books in Finnish are encoded in the CP437 ("IBM PC") character set.  As this encoding is deprecated, the Finnish files are provided for the convenience of inspection also in the UTF-8 encoding with the `.utf8` file name extension.

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

### 3.2 listing all rules

```
./kwic -rlist=fin
```
The output should be like:

<blockquote>
C<br>
CC<br>
CCC<br>
...<br>
TW-AD-OUT-EXCL<br>
TW-TRNS-EXCL<br>
TW-ALL-EXCL<br>
</blockquote>

```
./kwic -rlist=eng
```
The output should be like:

<blockquote>
VERBS<br>
VERBS-PRES-3SG<br>
VERBS-PAST<br>
...<br>
TW-TRNS-EXCL<br>
TW-ALL-EXCL<br>
TW-PRP-CMPL-EXCL<br>
</blockquote>



### 3.3 other runs

*TBW*


## 4 contacts

Jorma Laaksonen <<jorma.laaksonen@aalto.fi>>

## 5 copyright

© 2006–2024 Pirkko Suihkonen & Jorma Laaksonen

