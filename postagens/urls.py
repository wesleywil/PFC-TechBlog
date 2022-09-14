from django.urls import path

from .views import (
    ListarPosts,
    VerDetalhesPosts,
    ListarPostsPorCategoria,
    CriarPost,
    AtualizarPost,
    DeletarPost,
    ListarCategorias,
    VerDetalhesCategorias,
    CriarCategoria,
    AtualizarCategoria,
    DeletarCategoria
)

app_name = "blog"

urlpatterns = [
    path('', ListarPosts.as_view(), name="listar_posts"),
    path('<int:pk>/', VerDetalhesPosts.as_view(), name='detalhe_post'),
    path('por_categoria/<titulo>/', ListarPostsPorCategoria.as_view(), name='listar_posts_por_categoria'),
    path('criar/', CriarPost.as_view(), name="criar_post"),
    path('<int:pk>/atualizar/', AtualizarPost.as_view(), name='atualizar_post'),
    path('<int:pk>/deletar/', DeletarPost.as_view(), name='deletar_post'),
    path('categorias/', ListarCategorias.as_view(), name="listar_categorias"),
    path('categorias/<int:pk>/', VerDetalhesCategorias.as_view(), name='detalhe_categoria'),
    path('categorias/criar/', CriarCategoria.as_view(), name="criar_categoria"),
    path('categorias/<int:pk>/atualizar/', AtualizarCategoria.as_view(), name='atualizar_categoria'),
    path('categorias/<int:pk>/deletar/', DeletarCategoria.as_view(), name='deletar_categoria'),
]