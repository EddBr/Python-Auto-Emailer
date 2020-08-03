# Python-Auto-Emailer
Automatically sends emails at a certain time 
</br>
Currently running on my Raspberry Pi, not very intensive

<h2>
  To Use:
</h2>
<h3>
  Requires Python modules smtplib and datetime to be installed on device
  </br>
  Create a GMail account to send automatic emails from
  </br>
  </br>
  Enable Less Secure Apps for that GMail address https://myaccount.google.com/lesssecureapps
  </br>
  </br>
  Add GMail password, recipients and sender in sensitive.py
  </br>
  </br>
  Set the time you would like in timecheck.py
  </br>
  </br>
  To run : ~ python timecheck.py
</h3>

</br>
</br>
<h2>
  Extra:
<h4>
  I suggest using something similar to the Linux screen module, so that the device can be used with this running in the background
  </br>
  The emails are likely to be blocked as they are deemed high risk by Google for good reason, as SMTP scripts are commonly used for spam. So check the spam folder if you cannot find it.
</h4>
</br>
<p>
  <b>
    DO NOT USE THIS REPOSITARY FOR ANY ILLEGITIMATE, UNETHICAL OR ILLEGAL PURPOSES. THIS WAS CREATED ONLY AS AN EDUCATIONAL AND USEFUL TOOL FOR TIMED EMAIL REMINDERS OR ALERTS, I DO NOT CLAIM RESPONSIBILITY IN ANY WAY FOR OTHERS WHO USE THIS SCRIPT IN ANY OTHER FORM. 
   </b>
</p>
</br>
<h6>
  This was produced solely by me, EddBr
</h6>
