Managing redirects
##################

By implementing redirects, you can retain the SEO rankings and authority of the old URL, transferring it to the new one. This helps to ensure that your website maintains its search engine visibility.

Django CMS supports redirects as part of the :ref:`Page settings <page-settings>`. It happens on a per-language level. This means you can select different redirect targets for the different language contents of a page.

The simplest way to set redirects is:

1. **Accessing the Page Admin Interface:**
   Select "Pages..." in the page menu of the toolbar.

2. **Opening the page settings:**

   * Find the page you want to redirect in the page tree.

     .. image:: ../tutorial/images/05-pagetree-form.jpg
       :alt: django CMS page tree

   * If the page is published, select "Create new draft" from the dropdown menu of the page status indicator (number 7).
   * Click on the page settings icon (number 9: three horizontal sliders),

3. **Changing the redirect setting:**

   .. image:: ./images/redirect-settings.jpg
      :alt: django CMS page settings

   * Find the "URL options" section.
   * Click "Show" to open the "URL options" section
   * Change the "Redirect" setting by selecting the page which the current one should be redirected to
   * Close the setting by clicking "Save" at the bottom

4. **Publishing the change:**

   * Select "Publish" from the dropdown menu of the page status indicator (number 7)

.. note::

  Changes can only be made to draft page contents and will only take effect once published.


Managing redirects in Django CMS happens on page level. The system is designed to provide a user-friendly interface for content editors to manage redirects and thereby ensure keeping SEO rankings.

