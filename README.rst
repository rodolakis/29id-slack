APS Slack bot
=============


Read the `Getting started with Bolt for Python <https://slack.dev/bolt-python/tutorial/getting-started>`_  guide and `create a Slack app <https://api.slack.com/apps/new>`_ 

.. image:: docs/source/img/create_app.png
    :width: 50%
    :align: center

Select **From scratch** and follow the on-screen instructions.


Scopes
------

Once the Slack app is created you need to set the Slack app capabilities and permissions. These are called `scopes <https://api.slack.com/scopes>`_ and can be set accessing the Bot Token Scopes under the  **OAuth&Permissions** tab at:

.. image:: docs/source/img/features.png
    :width: 50%
    :align: center

and selecting the following:

.. image:: docs/source/img/scopes.png
    :width: 50%
    :align: center

Once this is done, select the **Install to Workspace** to obtain the **Bot User OAuth Token** = xoxb-xxxxxx-xxxxxxx-xxxxxxxxxxxx

Finally you need invite the Slack app to a specific slack channel:

.. image:: docs/source/img/invite.png
    :width: 50%
    :align: center

Security
--------

It is important to treat the **Bot User OAuth Token** as a password and never include it in your code. One option is to set it as and environment variable SLACK_TOKEN=xoxb-xxxxxx-xxxxxxx-xxxxxxxxxxxx.
