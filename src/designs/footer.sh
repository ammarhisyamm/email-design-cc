footer () {
	cat <<EOF
 <div class="live" data-kind="text" data-bg="$1" data-pad="36px 32px 40px">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="text-align:center;">
   <a href="https://tomaau.com/?utm_source=email&amp;utm_medium=email&amp;utm_campaign=$2&amp;utm_content=footer_logo"><img src="images/$3" width="84" alt="TOMA" style="width:84px;height:auto;margin:0 auto;"></a>
   <p style="margin:14px 0 0;font-family:'DM Sans',Helvetica,Arial,sans-serif;font-size:13px;line-height:20px;color:$4;">Websites, Meta campaigns &amp; creative<br><a href="mailto:info.toma.au@gmail.com" style="color:$5;font-weight:700;text-decoration:none;">info.toma.au@gmail.com</a> &middot; <a href="https://tomaau.com/?utm_source=email&amp;utm_medium=email&amp;utm_campaign=$2&amp;utm_content=footer" style="color:$5;font-weight:700;text-decoration:none;">tomaau.com</a></p>
   <p style="margin:18px 0 0;font-family:'DM Sans',Helvetica,Arial,sans-serif;font-size:11.5px;line-height:17px;color:$4;">$6Visuals use fictional “YOUR BRAND” packaging for illustration only. They aren’t client work and don’t indicate Meta approval or ad eligibility.<br>TOMA &middot; [Business address] &middot; [ABN]<br><a href="{{privacy_policy_url}}" style="color:$4;text-decoration:underline;">Privacy</a> &nbsp;&middot;&nbsp; <a href="{{preferences_url}}" style="color:$4;text-decoration:underline;">Preferences</a> &nbsp;&middot;&nbsp; <a href="{{unsubscribe_url}}" style="color:$4;text-decoration:underline;">Unsubscribe</a></p>
  </td></tr></table>
 </div>
EOF
}
