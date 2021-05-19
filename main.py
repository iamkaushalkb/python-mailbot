from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail_settings = {
  "MAIL_SERVER" : 'smtp.gmail.com',
  "MAIL_USE_TLS" : False,
  "MAIL_USE_SSL" : True,
  "MAIL_PORT" : 465,
  "MAIL_USERNAME" : 'your-email',
  "MAIL_PASSWORD" : 'your-password'
}

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
    with app.app_context():
        msg = Message(sender=app.config.get("MAIL_USERNAME"),
                      recipients = ["sender-mail"]
        )
        msg.subject = " About OJT "
        msg.html = """
        <head>
            <!--[if gte mso 9]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
            <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
            <meta content="width=device-width" name="viewport" />
            <!--[if !mso]><!-->
            <meta content="IE=edge" http-equiv="X-UA-Compatible" />
            <!--<![endif]-->
            <title></title>
            <!--[if !mso]><!-->
            <!--<![endif]-->
            <style type="text/css">
                body {
                    margin: 0;
                    padding: 0;
                }
        
                table,
                td,
                tr {
                    vertical-align: top;
                    border-collapse: collapse;
                }
        
                * {
                    line-height: inherit;
                }
        
                a[x-apple-data-detectors=true] {
                    color: inherit !important;
                    text-decoration: none !important;
                }
            </style>
            <style id="media-query" type="text/css">
                @media (max-width: 645px) {
        
                    .block-grid,
                    .col {
                        min-width: 320px !important;
                        max-width: 100% !important;
                        display: block !important;
                    }
        
                    .block-grid {
                        width: 100% !important;
                    }
        
                    .col {
                        width: 100% !important;
                    }
        
                    .col_cont {
                        margin: 0 auto;
                    }
        
                    img.fullwidth,
                    img.fullwidthOnMobile {
                        max-width: 100% !important;
                    }
        
                    .no-stack .col {
                        min-width: 0 !important;
                        display: table-cell !important;
                    }
        
                    .no-stack.two-up .col {
                        width: 50% !important;
                    }
        
                    .no-stack .col.num2 {
                        width: 16.6% !important;
                    }
        
                    .no-stack .col.num3 {
                        width: 25% !important;
                    }
        
                    .no-stack .col.num4 {
                        width: 33% !important;
                    }
        
                    .no-stack .col.num5 {
                        width: 41.6% !important;
                    }
        
                    .no-stack .col.num6 {
                        width: 50% !important;
                    }
        
                    .no-stack .col.num7 {
                        width: 58.3% !important;
                    }
        
                    .no-stack .col.num8 {
                        width: 66.6% !important;
                    }
        
                    .no-stack .col.num9 {
                        width: 75% !important;
                    }
        
                    .no-stack .col.num10 {
                        width: 83.3% !important;
                    }
        
                    .video-block {
                        max-width: none !important;
                    }
        
                    .mobile_hide {
                        min-height: 0px;
                        max-height: 0px;
                        max-width: 0px;
                        display: none;
                        overflow: hidden;
                        font-size: 0px;
                    }
        
                    .desktop_hide {
                        display: block !important;
                        max-height: none !important;
                    }
                }
            </style>
            <style id="icon-media-query" type="text/css">
                @media (max-width: 645px) {
                    .icons-inner {
                        text-align: center;
                    }
        
                    .icons-inner td {
                        margin: 0 auto;
                    }
                }
            </style>
        </head>
        
        <body class="clean-body" style="margin: 0; padding: 0; -webkit-text-size-adjust: 100%; background-color: #f0f2f3;">
            <!--[if IE]><div class="ie-browser"><![endif]-->
            <table bgcolor="#f0f2f3" cellpadding="0" cellspacing="0" class="nl-container" role="presentation"
                style="table-layout: fixed; vertical-align: top; min-width: 320px; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f0f2f3; width: 100%;"
                valign="top" width="100%">
                <tbody>
                    <tr style="vertical-align: top;" valign="top">
                        <td style="word-break: break-word; vertical-align: top;" valign="top">
                            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color:#f0f2f3"><![endif]-->
                            <div style="background-color:transparent;">
                                <div class="block-grid"
                                    style="min-width: 320px; max-width: 625px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
                                    <div
                                        style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:625px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                        <!--[if (mso)|(IE)]><td align="center" width="625" style="background-color:transparent;width:625px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                                        <div class="col num12"
                                            style="min-width: 320px; max-width: 625px; display: table-cell; vertical-align: top; width: 625px;">
                                            <div class="col_cont" style="width:100% !important;">
                                                <!--[if (!mso)&(!IE)]><!-->
                                                <div
                                                    style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                                                    <!--<![endif]-->
                                                    <div align="center" class="img-container center autowidth"
                                                        style="padding-right: 0px;padding-left: 0px;">
                                                        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]--><img
                                                            align="center" border="0" class="center autowidth"
                                                            src="https://pbs.twimg.com/media/EtyrbnvXIAQ1YPE?format=png&amp;name=small"
                                                            style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 625px; display: block;"
                                                            width="625" />
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </div>
                                                    <!--[if (!mso)&(!IE)]><!-->
                                                </div>
                                                <!--<![endif]-->
                                            </div>
                                        </div>
                                        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                        <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                    </div>
                                </div>
                            </div>
                            <div style="background-color:transparent;">
                                <div class="block-grid"
                                    style="min-width: 320px; max-width: 625px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: #ffffff;">
                                    <div style="border-collapse: collapse;display: table;width: 100%;background-color:#ffffff;">
                                        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:625px"><tr class="layout-full-width" style="background-color:#ffffff"><![endif]-->
                                        <!--[if (mso)|(IE)]><td align="center" width="625" style="background-color:#ffffff;width:625px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                                        <div class="col num12"
                                            style="min-width: 320px; max-width: 625px; display: table-cell; vertical-align: top; width: 625px;">
                                            <div class="col_cont" style="width:100% !important;">
                                                <!--[if (!mso)&(!IE)]><!-->
                                                <div
                                                    style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                                                    <!--<![endif]-->
                                                    <table border="0" cellpadding="0" cellspacing="0" class="divider"
                                                        role="presentation"
                                                        style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;"
                                                        valign="top" width="100%">
                                                        <tbody>
                                                            <tr style="vertical-align: top;" valign="top">
                                                                <td class="divider_inner"
                                                                    style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;"
                                                                    valign="top">
                                                                    <table align="center" border="0" cellpadding="0"
                                                                        cellspacing="0" class="divider_content" height="5"
                                                                        role="presentation"
                                                                        style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 5px; width: 100%;"
                                                                        valign="top" width="100%">
                                                                        <tbody>
                                                                            <tr style="vertical-align: top;" valign="top">
                                                                                <td height="5"
                                                                                    style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;"
                                                                                    valign="top"><span></span></td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 40px; padding-left: 40px; padding-top: 10px; padding-bottom: 10px; font-family: Tahoma, Verdana, sans-serif"><![endif]-->
                                                    <div
                                                        style="color:#555555;font-family:Roboto, Tahoma, Verdana, Segoe, sans-serif;line-height:1.5;padding-top:10px;padding-right:40px;padding-bottom:10px;padding-left:40px;">
                                                        <div class="txtTinyMce-wrapper"
                                                            style="font-size: 14px; line-height: 1.5; color: #555555; font-family: Roboto, Tahoma, Verdana, Segoe, sans-serif; mso-line-height-alt: 21px;">
                                                            <p
                                                                style="font-size: 24px; line-height: 1.5; word-break: break-word; text-align: left; mso-line-height-alt: 36px; margin: 0;">
                                                                <span style="font-size: 24px;"> Hi Jenish,</span></p>
                                                            <p
                                                                style="font-size: 16px; line-height: 1.5; word-break: break-word; text-align: left; mso-line-height-alt: 24px; margin: 0;">
                                                                <span style="font-size: 16px;"> <strong><a
                                                                            href="#" rel="noopener"
                                                                            style="text-decoration: none; color: #796eff;"
                                                                            target="_blank">On-The-Job Training </a></strong><span
                                                                        style="color: #796eff;"><span style="color: #555555;">'s
                                                                        </span></span><span style="color: #796eff;"><span
                                                                            style="color: #555555;"<strong><a href="#" rel="noopener"
                                                                                    style="text-decoration: none; color: #796eff;"
                                                                                    target="_blank"></a></strong><span
                                                                                style="color: #796eff;"><strong> </strong><span
                                                                                    style="color: #555555;">(OJT) is one of the best practical course in which students can
                                                                                    experience working in the real work field. OJT makes student a bit mature that they
                                                                                    can make some of the decision by themselves and also provides a lot of practical
                                                                                    knowledge. On-the-job training (OJT) is one of the best training methods because it is
                                                                                    planned, organized, and conducted at the employee’s worksite. OJT will generally
                                                                                    help the students to become a young professional. This is one of the method by which
                                                                                    students are able to apply the theories and computations that they have learned from
                                                                                    school. It helps the students to acquire relevant knowledge and skill by performing in
                                                                                    actual work setting.</span></span></span></span></span><span
                                                                    style="font-size: 24px;"><span style=""><span
                                                                            style="color: #796eff;"><span
                                                                                style="color: #555555;"><span
                                                                                    style="color: #796eff;"></span></span></span></span></span>
                                                            </p>
                                                            <p
                                                                style="font-size: 24px; line-height: 1.5; word-break: break-word; text-align: left; mso-line-height-alt: 36px; margin: 0;">
                                                                <span style="font-size: 24px;"><span style=""><span
                                                                            style="color: #796eff;"><span
                                                                                style="color: #555555;"><span
                                                                                    style="color: #796eff;"><span
                                                                                        style="color: #555555;">Thank
                                                                                        You</span></span></span></span></span></span>
                                                            </p>
                                                        </div>
                                                    </div>
                                                    <!--[if mso]></td></tr></table><![endif]-->
                                                    <!--[if (!mso)&(!IE)]><!-->
                                                </div>
                                                <!--<![endif]-->
                                            </div>
                                        </div>
                                        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                        <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                    </div>
                                </div>
                            </div>
                            <div style="background-color:transparent;">
                                <div class="block-grid"
                                    style="min-width: 320px; max-width: 625px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
                                    <div
                                        style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:625px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                        <!--[if (mso)|(IE)]><td align="center" width="625" style="background-color:transparent;width:625px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                                        <div class="col num12"
                                            style="min-width: 320px; max-width: 625px; display: table-cell; vertical-align: top; width: 625px;">
                                            <div class="col_cont" style="width:100% !important;">
                                                <!--[if (!mso)&(!IE)]><!-->
                                                <div
                                                    style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                                                    <!--<![endif]-->
                                                    <table border="0" cellpadding="0" cellspacing="0" class="divider"
                                                        role="presentation"
                                                        style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;"
                                                        valign="top" width="100%">
                                                        <tbody>
                                                            <tr style="vertical-align: top;" valign="top">
                                                                <td class="divider_inner"
                                                                    style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;"
                                                                    valign="top">
                                                                    <table align="center" border="0" cellpadding="0"
                                                                        cellspacing="0" class="divider_content" height="0"
                                                                        role="presentation"
                                                                        style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 0px; width: 100%;"
                                                                        valign="top" width="100%">
                                                                        <tbody>
                                                                            <tr style="vertical-align: top;" valign="top">
                                                                                <td height="0"
                                                                                    style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;"
                                                                                    valign="top"><span></span></td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                    <!--[if (!mso)&(!IE)]><!-->
                                                </div>
                                                <!--<![endif]-->
                                            </div>
                                        </div>
                                        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                        <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                    </div>
                                </div>
                            </div>
                            <div style="background-color:transparent;">
                                <div class="block-grid"
                                    style="min-width: 320px; max-width: 625px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
                                    <div
                                        style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:625px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                        <!--[if (mso)|(IE)]><td align="center" width="625" style="background-color:transparent;width:625px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                                        <div class="col num12"
                                            style="min-width: 320px; max-width: 625px; display: table-cell; vertical-align: top; width: 625px;">
                                            <div class="col_cont" style="width:100% !important;">
                                                <!--[if (!mso)&(!IE)]><!-->
                                                <div
                                                    style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                                                    <!--<![endif]-->
                                                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 45px; padding-left: 45px; padding-top: 10px; padding-bottom: 10px; font-family: Tahoma, Verdana, sans-serif"><![endif]-->
                                                    <div
                                                        style="color:#c0c0c0;font-family:Roboto, Tahoma, Verdana, Segoe, sans-serif;line-height:1.5;padding-top:10px;padding-right:45px;padding-bottom:10px;padding-left:45px;">
                                                        <div class="txtTinyMce-wrapper"
                                                            style="font-size: 14px; line-height: 1.5; color: #c0c0c0; font-family: Roboto, Tahoma, Verdana, Segoe, sans-serif; mso-line-height-alt: 21px;">
                                                            <p
                                                                style="font-size: 14px; line-height: 1.5; word-break: break-word; text-align: center; mso-line-height-alt: 21px; margin: 0;">
                                                                Questions? I am always here to help. </p>
                                                        </div>
                                                    </div>
                                                    <!--[if mso]></td></tr></table><![endif]-->
                                                    <table border="0" cellpadding="0" cellspacing="0" class="divider"
                                                        role="presentation"
                                                        style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;"
                                                        valign="top" width="100%">
                                                        <tbody>
                                                            <tr style="vertical-align: top;" valign="top">
                                                                <td class="divider_inner"
                                                                    style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;"
                                                                    valign="top">
                                                                    <table align="center" border="0" cellpadding="0"
                                                                        cellspacing="0" class="divider_content" height="0"
                                                                        role="presentation"
                                                                        style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 0px; width: 100%;"
                                                                        valign="top" width="100%">
                                                                        <tbody>
                                                                            <tr style="vertical-align: top;" valign="top">
                                                                                <td height="0"
                                                                                    style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;"
                                                                                    valign="top"><span></span></td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" class="social_icons"
                                                        role="presentation"
                                                        style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        valign="top" width="100%">
                                                        <tbody>
                                                            <tr style="vertical-align: top;" valign="top">
                                                                <td style="word-break: break-word; vertical-align: top; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px;"
                                                                    valign="top">
                                                                    <table align="center" cellpadding="0" cellspacing="0"
                                                                        class="social_table" role="presentation"
                                                                        style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-tspace: 0; mso-table-rspace: 0; mso-table-bspace: 0; mso-table-lspace: 0;"
                                                                        valign="top">
                                                                        <tbody>
                                                                            <tr align="center"
                                                                                style="vertical-align: top; display: inline-block; text-align: center;"
                                                                                valign="top">
                                                                                <td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 15px; padding-left: 0;"
                                                                                    valign="top"><a
                                                                                        href="https://www.facebook.com/iamkaushalkb"
                                                                                        target="_blank"><img alt="Facebook"
                                                                                            height="32"
                                                                                            src="https://pbs.twimg.com/media/Ety0kmAXUAcq0v7?format=webp&name=tiny"
                                                                                            style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; display: block;"
                                                                                            title="Facebook" width="32" /></a>
                                                                                </td>
                                                                                <td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 15px; padding-left: 0;"
                                                                                    valign="top"><a
                                                                                        href="https://twitter.com/iamkaushalkb"
                                                                                        target="_blank"><img alt="Twitter"
                                                                                            height="32"
                                                                                            src="https://pbs.twimg.com/media/Ety0kmEXIAg7pZo?format=webp&name=tiny"
                                                                                            style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; display: block;"
                                                                                            title="Twitter" width="32" /></a>
                                                                                </td>
                                                                                <td style="word-break: break-word; vertical-align: top; padding-bottom: 5px; padding-right: 15px; padding-left: 0;"
                                                                                    valign="top"><a
                                                                                        href="https://instagram.com/iamkaushalkb"
                                                                                        target="_blank"><img alt="Instagram"
                                                                                            height="32"
                                                                                            src="https://pbs.twimg.com/media/Ety0kmBXcAQUJ1J?format=webp&name=tiny"
                                                                                            style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; display: block;"
                                                                                            title="Instagram" width="32" /></a>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                    <table border="0" cellpadding="0" cellspacing="0" class="divider"
                                                        role="presentation"
                                                        style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;"
                                                        valign="top" width="100%">
                                                        <tbody>
                                                            <tr style="vertical-align: top;" valign="top">
                                                                <td class="divider_inner"
                                                                    style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;"
                                                                    valign="top">
                                                                    <table align="center" border="0" cellpadding="0"
                                                                        cellspacing="0" class="divider_content" height="0"
                                                                        role="presentation"
                                                                        style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 0px; width: 100%;"
                                                                        valign="top" width="100%">
                                                                        <tbody>
                                                                            <tr style="vertical-align: top;" valign="top">
                                                                                <td height="0"
                                                                                    style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;"
                                                                                    valign="top"><span></span></td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                    <!--[if (!mso)&(!IE)]><!-->
                                                </div>
                                                <!--<![endif]-->
                                            </div>
                                        </div>
                                        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                        <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                    </div>
                                </div>
                            </div>
                            <div style="background-color:transparent;">
                                <div class="block-grid"
                                    style="min-width: 320px; max-width: 625px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
                                    <div
                                        style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                                        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:625px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                                        <!--[if (mso)|(IE)]><td align="center" width="625" style="background-color:transparent;width:625px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                                        <div class="col num12"
                                            style="min-width: 320px; max-width: 625px; display: table-cell; vertical-align: top; width: 625px;">
                                            <div class="col_cont" style="width:100% !important;">
                                                <!--[if (!mso)&(!IE)]><!-->
                                                <div
                                                    style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                                                    <!--<![endif]-->
                                                    <table cellpadding="0" cellspacing="0" role="presentation"
                                                        style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        valign="top" width="100%">
                                                        <tr style="vertical-align: top;" valign="top">
                                                            <td align="center"
                                                                style="word-break: break-word; vertical-align: top; padding-top: 5px; padding-right: 0px; padding-bottom: 5px; padding-left: 0px; text-align: center;"
                                                                valign="top">
                                                                <!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
                                                                <!--[if !vml]><!-->
        
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <!--[if (!mso)&(!IE)]><!-->
                                                </div>
                                                <!--<![endif]-->
                                            </div>
                                        </div>
                                        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                                        <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                                    </div>
                                </div>
                            </div>
                            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                        </td>
                    </tr>
                </tbody>
            </table>
            <!--[if (IE)]></div><![endif]-->
        </body>
        
        </html>
        """
        mail.send(msg)
        print("Sent..........")