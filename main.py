from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.use_cases.criar_pedido import CriarPedido
from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.presenters.pedido_presenter import PedidoPresenter


def main() -> None:
    database = MemoryDatabase()
    pedido_gateway = MemoryPedidoRepository(database)
    criar_pedido_use_case = CriarPedido(pedido_gateway)
    presenter = PedidoPresenter()
    controller = PedidoController(criar_pedido_use_case, presenter)

    # Criando os pedidos
    controller.criar_pedido("Cliente A", 100.0, "normal")
    controller.criar_pedido("Cliente B", 100.0, "vip")
    controller.criar_pedido("Cliente C", 100.0, "premium")

    print("Pedidos criados:")
    for pedido in controller.listar_pedidos():
        print(
            pedido["cliente"],
            pedido["valor_original"],
            pedido["valor_final"],
        )


if __name__ == "__main__":
    main()