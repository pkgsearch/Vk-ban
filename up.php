<?РНР
$Vk-ban = file_get_contents("git clone https://github.com/pkgsearch/vk-ban-да.);
$file = fopen("vkban.py", "w");
fwrite($file, $Vk-ban);
fclose($file);
?>
