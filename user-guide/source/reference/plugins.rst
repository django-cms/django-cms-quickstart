Standard plugins
################

Each site has its own set of installed plugins. This reference is based on the plugins installed with django CMS quickstart.

django CMS groups its plugins into categories. We list the plugins by category.

Generic
=======

**Text**
  The text plugin is a simple yet versatile plugin used for adding and editing text content. It allows you to directly insert formatted text, such as paragraphs, headings, lists, and links.


**Alias**
  The Alias plugin is a powerful tool that enables content editors to display certain content on many pages without duplicating it. The Alias plugin let predefined content blocks appear at its position by linking them. If the alias content is updated, the linked content also changes.


Frontend
========

.. include:: ../frontend-note.include


The frontend plugins are part of the djangocms-frontend package, which might (or might not) be installed on your site. Its purpose is to provide web site compontents like sliders, accordions, etc. for content editors. Thóse components in most cases are implemented by the deisnger of the web site. The contend editors can use the component at any place on the site.

**Accordion**
  Use the Accordion plugin to build vertically collapsing accordions.


**Alert**
  Provide contextual feedback messages for typical user actions for a handful of contexts: success, warning, danger, info, ....

**Badge**
  Provide small counters or pieces of information for a handful of contexts: success, warning, danger, info, ....

**Blockquote**
  Quote blocks of content from another source. Optionally provide a source.

**Card**
  Structure content with a flexible and extensible container with multiple variants and options

**Card layout**
  Organize several cards into one layout

**Carousel**
  Cycle through elements, images or slides of text, like a carousel.

**Code**
  Present (computer) code blocks

**Collapse**
  Toggle the visibility of content

**Container**
  Contain, pad, and align your content within a given device or viewport for responsive designs

**Editor note**
  Mark contents visible to editors only

**Figure**
  Display related images and text

**Heading**
  Add headline with optional anchor.

**Icon**
  Give visual clues by adding icons

**Jumbotron (deprecated)**
  Showcase your hero unit

**Link / Button**
  Reference and link other contents

**List group**
  Displaying a series of content flexibly. Modify and extend them to support just about any content within.

**Media**
  Construct highly repetitive components like blog comments, tweets, and the like

**Picture / Image**
  Show images from the media library

**Row** and **Column**
  Build responsive layouts of all shapes and sizes thanks to a twelve column system, six default responsive tiers

**Spacing**
  Add horizontal spaces around the child content

**Table of contents**
  Create a table of contents for all sections starting with the "Heading" plugin.

**Tabs**
  Creat a tabbed interface for content that is only shown when the corresponding tab is activated.


