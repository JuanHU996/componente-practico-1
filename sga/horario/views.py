from django.shortcuts import render
# Create your views here.
def inicio(request):
    contexto = {}

    if request.method == 'POST':
        numeros_texto = request.POST.get('numeros', '')
        numeros = [int(n) for n in numeros_texto.split() if n.isdigit()]

        operaciones = request.POST.getlist('operaciones')

        if numeros:
            contexto['numeros'] = numeros

            if 'suma' in operaciones:
                contexto['suma'] = sum(numeros)
            if 'promedio' in operaciones:
                contexto['promedio'] = sum(numeros) / len(numeros)
            if 'mayor' in operaciones:
                contexto['mayor'] = max(numeros)
            if 'menor' in operaciones:
                contexto['menor'] = min(numeros)
            if 'pares' in operaciones:
                contexto['pares'] = list(filter(lambda x: x % 2 == 0, numeros))
            if 'impares' in operaciones:
                contexto['impares'] = list(filter(lambda x: x % 2 != 0, numeros))
            if 'cuadrados' in operaciones:
                contexto['cuadrados'] = list(map(lambda x: x ** 2, numeros))

    return render(request, 'base.html', contexto)