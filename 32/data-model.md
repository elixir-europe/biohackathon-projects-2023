# Data model for project 32

This data model represents the data objects and links linking training and software tools as well as EDAM with bioschemas links. It summarizes have information can be linked in an interoperable way between bio.tools and TeSS, using EDAM and BioSchemas/schema.org.


```mermaid
    graph TD;

    %%classDef
    classDef training fill:darkGreen,color:white,stroke-width:0px;
    classDef trainingrel fill:white,color:darkGreen, stroke:darkGreen,stroke-width:4px;
    classDef tools fill:darkOrange,color:white,stroke-width:0px;
    classDef toolsrel fill:white,color:darkOrange, stroke:darkOrange,stroke-width:4px;
    classDef EDAM fill:teal,color:white,stroke-width:0px;
    classDef EDAMrel fill:white,color:teal, stroke:teal,stroke-width:4px;
    classDef BSrel fill:white,color:pink, stroke:pink,stroke-width:4px;
      C[Course];
      CI[CourseInstance];
      TM[TrainingMaterial];
      ET[EDAM Topic];
      EO[EDAM Operation];
      ED[EDAM Data];
      EF[EDAM Format];
      hT[hasTopic];
      hI[hasInput];
      hO[hasOutput];
      iFO[isFormatOf];
      SA[SoftwareApplication];
      aSC[applicationSubCategory];
      fL[featureList];
      in[input];
      ou[output];
      hCI[hasCourseInstance];
      hP[hasPart];
      a[about];
      m[mentions];
      wF[workFeatured];
      t[teaches];
      C-->hCI;
      hCI-->CI;
      C-->hP;
      TM-->hP;
      hP-->TM;
      C-->a;
      TM-->a;
      a-->ET;
      SA-->aSC;
      aSC-->ET;
      SA-->fL;
      fL-->EO;
      SA-->in;
      in-->ED;
      SA-->ou;
      ou-->ED;
      ED-->hT;
      hT-->ET;
      EO-->hT;
      EF-->iFO;
      iFO-->ED;
      EO-->hI;
      hI-->ED;
      EO-->hO;
      hO-->ED;
      C-->t;
      C-->m;
      t-->SA;
      TM-->m;
      TM-->t;
      m-->SA;
      CI-->wF;
      wF-->SA;
    %%Style
    class C training;
    class CI training;
    class TM training;
    class SA tools;
    class ET EDAM;
    class ED EDAM;
    class EF EDAM;
    class EO EDAM;
    class hT EDAM;
    class iFO EDAM;
    class hI EDAM;
    class hO EDAM;
    class a trainingrel;
    class hP trainingrel;
    class hCI trainingrel;
    class in toolsrel;
    class ou toolsrel;
    class fL toolsrel;
    class aSC toolsrel;
    class hT EDAMrel;
    class iFO EDAMrel;
    class hI EDAMrel;
    class hO EDAMrel;
    class m BSrel;
    class t BSrel;
    class wF BSrel;
```
