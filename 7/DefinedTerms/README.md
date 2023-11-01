# Analysis of DefinedTerms in Bioschemas
As a first step towards harmonisation and improvement of how `DefinedTerm`s are used in Bioschemas, 
the following is an analysis of `DefinedTerm`s in the wild.

## Obtaining all DefinedTerms in Bioschemas live-deploy's exampleURLs
```
mkdir exampleURLcontent
mkdir DefinedTermsOnly

# Download all exampleURLs into exampleURLcontent
jq '.resources[].profiles[].exampleURL' live_deployments.json |\
    tr -d \" | sort | uniq |\
    parallel --joblog /tmp/parallel.log \
        wget -q --content-on-error --directory-prefix=./exampleURLcontent

# Extract all <script type=”application/ld+json”> from HTML pages
for F in * ; do 
    xmllint --html --nowarning \
        --xpath '//html/head/script[@type="application/ld+json"]/text()' \
        "$F" 2>/dev/null |\
    sed -e 's/<!\[CDATA\[//g; s/\]\]>//g' |\
    jq '[getpath(paths(. == "DefinedTerm")[:-1])]' >"../DefinedTermsOnly/$F.json"
done

# Concatenate all JSON-LD into one array
jq -s 'add' DefinedTermsOnly *.json >all.DefinedTerms
```

## Some Analysis:

