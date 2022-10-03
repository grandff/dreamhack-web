<html>
    <head></head>
    <link rel="stylesheet" href="/static/bulma.min.css" />
    <body>
        <div class="container card">
        <div class="card-content">
        <h1 class="title">Online Curl Request</h1>
    <?php
        if(isset($_GET['url'])){
            $url = $_GET['url'];
            if(strpos($url, 'http') !== 0 ){    // http만 받도록 하고 있음
                die('http only !');
            }else{
                // escapeshellcmd  함수를 통해  셸 메타 함수 사용 금지 처리
                $result = shell_exec('curl '. escapeshellcmd($_GET['url']));    // shell_exec 함수를 통해 curl 명령어를 실행. 
                
                $cache_file = './cache/'.md5($url);
                file_put_contents($cache_file, $result);
                echo "<p>cache file: <a href='{$cache_file}'>{$cache_file}</a></p>";
                echo '<pre>'. htmlentities($result) .'</pre>';
                return;
            }
        }else{
        ?>
            <form>
                <div class="field">
                    <label class="label">URL</label>
                    <input class="input" type="text" placeholder="url" name="url" required>
                </div>
                <div class="control">
                    <input class="button is-success" type="submit" value="submit">
                </div>
            </form>
        <?php
        }
    ?>
        </div>
        </div>
    </body>
</html>