.. raw:: html

    <style>
        .row {
           clear: both;
        }

        .column img {border: 1px solid gray;}

        @media only screen and (min-width: 1000px),
               only screen and (min-width: 500px) and (max-width: 768px){

            .column {
                padding-left: 5px;
                padding-right: 5px;
                float: left;
            }

            .column3  {
                width: calc(33.3% - 10px);
            }

            .column2  {
                width: calc(50% - 11px);
                position: relative;
            }
            .column2:before {
                padding-top: 61.8%;
                content: "";
                display: block;
                float: left;
            }
            .top-left {
                border-right: 1px solid var(--color-background-border);
                border-bottom: 1px solid var(--color-background-border);
            }
            .top-right {
                border-bottom: 1px solid var(--color-background-border);
            }
            .bottom-left {
                border-right: 1px solid var(--color-background-border);
            }
        }
    </style>

.. _user-manual:

################
Using django CMS
################

.. note::

          This is a new section in the django CMS documentation, and a priority
          for the project. If you'd like to contribute to it, we'd love to hear
          from you - join us on `our friendly Slack group
          <https://www.django-cms.org/slack>`_.

Introduction
############

This is a user guide for django CMS. The intended audience for this guide are content creators and site administrators.

Django CMS sites are highly customisable and varied. The examples here follow the `quickstart project from Github <https://github.com/django-cms/django-cms-quickstart>`_. This provides certain features, which are entirely optional for your own site, and the features provided in the quickstart are used in this guide to demonstrate how django CMS can be used.

The origin of this document is a guide provided by `Kapt.mobi <https://support.kapt.mobi/index.php/docs/kapt-doc/>`_. It has been translated from the native French and extended.

Guide for content editors
#########################


.. rst-class:: clearfix row

.. rst-class:: column column2 top-left

:ref:`user-tutorial`
====================

**Start here as a new django CMS content editor**:

* Getting to know the user interface
* Understanding the page tree
* Creating content

.. rst-class:: column column2 top-right

:ref:`user-how-to`
==================

Practical **step-by-step guides** to get things done in the most simple way as a content editor

.. rst-class:: column column2 bottom-left

:ref:`user-explanation`
=======================

What's a placeholder? What's a plugin? Understand key concepts of django CMS.

.. rst-class:: column column2 bottom-right

:ref:`user-reference`
=====================

Reference material for installed plugins.


.. rst-class:: clearfix row

.. toctree::
    :maxdepth: 1
    :hidden:

    tutorial/index
    explanation/index
    how-to/index
    reference/index
