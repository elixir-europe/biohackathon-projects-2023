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
for F in exampleURLcontent/* ; do 
    xmllint --html --nowarning \
        --xpath '//html/*/script[@type="application/ld+json"]/text()' \
        "$F" 2>/dev/null |\
    sed -e 's/<!\[CDATA\[//g; s/\]\]>//g' |\
    jq '[getpath(paths(. == "DefinedTerm")[:-1])]' >"./DefinedTermsOnly/$(basename $F).json"
done

# Concatenate all JSON-LD into one array
jq -s 'add' DefinedTermsOnly/*.json >all.DefinedTerms
```

## Some Analysis:

There are ~135 DefinedTerms in the example URLs:
```
grep -c '"DefinedTerm"' all.DefinedTerms 
135
```

So far, only `@id, @type, termCode, name, url` are used in `DefinedTerm`s we see:
```
jq 'del(..|objects|.inDefinedTermSet)' <all.DefinedTerms | cut -d: -f 1 | grep -v "[]{[}]" | sort | uniq -c | sort -n 
      2     "termCode"
      2     "url"
      7     "name"
    130     "@id"
    135     "@type"
```
Some entries with `"@type": "DefinedTerm"` omit `@id`, which is an error. 

There was no proper analysis of the `inDefinedTermSet` yet, but it ranges from just giving a URL, to specifying `"@type": "DefinedTermSet"`, its name and url.



