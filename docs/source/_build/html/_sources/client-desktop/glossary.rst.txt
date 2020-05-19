Glossary
########

.. glossary::
   :sorted:

   Actions
      An *action* is a function which is triggered by a user intervention.
      *Actions* are called from activating menu items or pushing buttons.
      Actions often provide :term:`Wizards`.

   Board
      The *board* is a type of :term:`Views` able to handle other views. This
      view type is not documented or not used for now.

   Character Encoding
      See [WP-ENCOD]_

   CSV
      File format for Comma Separated Values. See [WP-CSV]_

   Data
      *Data* means information content produced by users.


   Dialog
      A *dialog* is a :term:`Popup` window, which overlays other windows and
      request user interaction. *Dialogs* are used to set up special
      :term:`Actions`.

   Fields
      *Fields* are attributes of a *data object*. *Fields* are
      represented as table fields in relational databases.

   Form View
      The *form* is a mode of :term:`Views`, which displays single
      :term:`Records` of data.

   Form
      The *form* is the general type of :term:`Views` used in Tryton. The
      *form* provides several modes for presenting :term:`Data`:

      * :term:`Form View`
      * :term:`Tree View`
      * :term:`Graph View`

   Graph View
      *Graph view* is a mode of :term:`Views` to show sets of data in a
      diagram. *Graph views* can be pie-charts or bar-charts.

   Main Frame
      The *main frame* is a huge part arranged in the center of the
      :term:`Tryton Client`. *Using the Tryton client* means mainly using the
      *main frame* part. It contains :term:`Tabs` to organize and to show
      different :term:`Views`.

   Model
      A *model* describes how data is represented and accessed. Models
      formally define records and relationships for a certain domain
      of interest.

   Modules
      *Modules* are enclosed file packages for the :term:`Tryton Server`. A
      *Module* defines the :term:`Model`, the presentation of the
      information (:term:`Views`), functions, :term:`Actions` and default
      presets. Additionally *modules* may provide standardized data like ISO
      names for countries. *Modules* in Tryton are build up generically. That
      is, they are constructed as simple as possible to provide the
      desired functionality.

   Plugins
      A *plugin* is an add-on module for the :term:`Tryton Client`.

   Popup
      A small window which pops up the main window.

   Records
      A *record* is a singular dataset in a :term:`Model`. *Records* are
      represented as lines or *records* in a relational database table.

   Tabs
      *Tabs* are :term:`Widgets` to arrange different contents side by side.
      They are used to switch quickly between different domains of interest.
      Tryton uses *tabs* in two layer:

      * A tabbed :term:`Main Frame`.
      * Tabs inside :term:`Views`.

      The main frame consists of *tabs* that embed the main menu and all views
      to an appropriate :term:`Model`. The other type of *tabs* is used
      inside of :term:`Views` to split them into visual domains of the same
      model. These *tabs* are used for structuring contents of one model to
      different sub headings.

   Three-Tiers
      A *three-tiers* application framework like Tryton, is build up of three
      different software components:

      1. The storage or data tier.
      2. The logic or application tier.
      3. The presentation tier.

      The storage tier in the Tryton framework is provided by the PostgreSQL
      database engine. The application logic tier is provided by
      :term:`Tryton Server` and its :term:`Modules`. The presentation tier is
      mainly provided by the :term:`Tryton Client`. In a *three tiers*
      framework, the presentation tier (client) never connects directly to the
      storage tier. All communication is controlled by the application tier.

   Tree View
      *Tree view* is a mode of :term:`Views` showing sets of :term:`Data`.
      *Tree views* can be flat lists or tables as well as tree-like nested
      lists.

   Tryton Server
      The *Tryton server* is the application or logic tier in the
      :term:`Three-Tiers` application platform *Tryton*. The *Tryton server*
      connects the underlying application logic of the different
      :term:`Modules` with corresponding database records. The
      *Tryton server* provides different interfaces to present the
      generated information:

      * :term:`Tryton Client`: (graphical user interface GUI)
      * XMLRPC see [WP-XMLRPC]_
      * WebDAV see [WP-WebDAV]_
      * OpenOffice

   Tryton Client
      The *Tryton Client* application is the graphical user interface (GUI)
      of the :term:`Tryton Server`.

   Views
      A *view* is the visual presentation of :term:`Data`.
      *Views* resides inside :term:`Tabs` in the :term:`Main Frame` of the
      :term:`Tryton Client`. There are two general types of *views* in Tryton:

      1. :term:`Form`
      2. :term:`Board`

      Each of the view types has different modes to show data. *Views*
      are built of several :term:`Widgets` and provide often additional
      :term:`Actions`. It is also possible to present the same data in
      different view modes alternately.

   Widgets
      A *Widget* is a visual element of a graphical user interface (GUI). Some
      *Widgets* solely show information, others allow manipulation from user
      side. Example *Widgets* are buttons, check-boxes, entry-boxes, selection
      lists, tables, lists, trees, ...

   Wizards
      *Wizards* define stateful sequences of interaction to proceed
      complex :term:`Actions`. A *wizard* divides the complexity of some actions
      into several user guided steps.

References
**********

.. [WP-XMLRPC] http://en.wikipedia.org/wiki/Xmlrpc

.. [WP-WebDAV] http://en.wikipedia.org/wiki/Webdav

.. [WP-CSV] http://en.wikipedia.org/wiki/Comma-separated_values
.. [WP-ENCOD] http://en.wikipedia.org/wiki/Character_encoding


