<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>新闻检索系统</title>

    <meta name="description" content="Source code generated using layoutit.com">
    <meta name="author" content="LayoutIt!">

    <link href="/css/bootstrap.min.css" rel="stylesheet">
    <link href="/css/style.css" rel="stylesheet">

  </head>
  <body>

    <div class="container-fluid">
	<div class="row">
		<div class="col-md-12">
			<div class="row">
				<div class="col-md-2">
					 <!-- <span class="badge badge-default">Label</span> -->
				</div>
				<div class="col-md-8">
					<form role="form">
						<div class="form-group">

							<label for="exampleInputEmail1">
								输入关键词：
							</label>
							<input class="form-control" id="input">
						</div>

						<!-- <div class="form-group">

							<label for="exampleInputFile">
								File input
							</label>
							<input type="file" class="form-control-file" id="exampleInputFile">
							<p class="help-block">
								Example block-level help text here.
							</p>
						</div> -->
						<!-- <div class="checkbox">

							<label>
								<input type="checkbox"> Check me out
							</label>
						</div> -->
                        <!-- 没有加type=button出现了很多奇怪的结果 -->
                    <p>
						<button class="btn btn-primary" type="button" id="search">
							开始检索
						</button>
                      <button class="btn btn-primary" type="button" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
                          关键词分析
                      </button>
                    </p>
                    <div class="collapse" id="collapseExample">
                      <div class="card card-body">
                          <table class="table">
                          <thead>
                            <tr>
                              <th scope="col">关键词</th>
                              <th scope="col">出现总次数</th>
                              <th scope="col">出现的文档数</th>
                              <th scope="col">idf值</th>
                            </tr>
                          </thead>
                          <tbody>
                              %for word, word_summary in keywords_summary.items():
                            <tr>
                              <th scope="row">{{word}}</th>
                              <td>{{ word_summary['count'] }}</td>
                              <td>{{ word_summary['doc_count']}} </td>
                              <td>{{ word_summary['idf']}}</td>
                            </tr>
                            %end
                          </tbody>
                        </table>
                      </div>
                    </div>
                    <br>
					</form>

					<!-- <ul class="nav nav-pills">
						<li class="nav-item">
							 <a class="nav-link btn btn-primary" href="#">Home <span class="badge badge-light">42</span></a>
						</li>
						<li class="nav-item">
							 <a class="nav-link" href="#">More <span class="badge badge-secondary">16</span></a>
						</li>
					</ul> -->
                    <h5>下列是以关键词 <span style="color:blue;font-weight:bold">{{ query_string }}</span>进行检索返回的结果：</h5>
                    <h6>本次查询共用时
                        <span class="badge badge-info">{{ cost_time }}</span>
                        秒，为您找到
                        <span class="badge badge-info">{{ len(results) }}</span>
                        篇相关新闻，
                        <span class="badge badge-info">{{ highlight_count }}</span>
                        相关句子
                    </h6>

                    <br>

                    <!-- 主体部分 -->
                    %for result in results:
					<div class="card bg-default">
						<h5 class="card-header">
							新闻ID：{{ result.doc_id }}
                        <span class="badge badge-success">相似度：{{ result.score }}</span>
                        <span class="badge badge-info">相关句子：{{ len(result.highlights) }}</span>
						</h5>
						<div class="card-body">
                            <ul class="card-text">
                                %for h in result.highlights:
        						<li class="list-item">
        							{{!h}}
        						</li>
                                %end
        					</ul>
						</div>
						<div class="card-footer">
							其他信息：<a href="/news/{{ result.doc_id }}">该新闻(查看原文)</a>共有{{result.num_sents}}个句子，共计{{result.num_tokens}}个词。
						</div>
					<!-- </div><img alt="Bootstrap Image Preview" src="https://www.layoutit.com/img/sports-q-c-140-140-3.jpg"> -->
                    </div>
                    <br>
                    %end

                    <br>
                    <!-- <nav>
						<ul class="pagination">
							<li class="page-item">
								<a class="page-link" href="#">Previous</a>
							</li>
							<li class="page-item">
								<a class="page-link" href="#">1</a>
							</li>
							<li class="page-item">
								<a class="page-link" href="#">2</a>
							</li>
							<li class="page-item">
								<a class="page-link" href="#">3</a>
							</li>
							<li class="page-item">
								<a class="page-link" href="#">4</a>
							</li>
							<li class="page-item">
								<a class="page-link" href="#">5</a>
							</li>
							<li class="page-item">
								<a class="page-link" href="#">Next</a>
							</li>
						</ul>
					</nav> -->

				<div class="col-md-2">
				</div>
			</div>
		</div>
	</div>
</div>

    <script src="/js/jquery.min.js"></script>
    <script>
    $('#search').click(function(){
        var keywords = $.trim($('#input').val());
        if(keywords == ""){
            alert("关键词为空！");
            return ;
        }
        var url = "http://127.0.0.1:8080/search/" + keywords;
        $(location).attr('href',url);
    });
    //这里一直在加载  什么鬼啦！
    //window.location.href = "http://127.0.0.1:8080/search/win";
    </script>
    <script src="/js/bootstrap.min.js"></script>
    <script src="/js/scripts.js"></script>
  </body>
</html>
